# Spec: SQLite backend for the OHTM dashboard

## Problem

`ohtm_dash_server.py` parses the whole `.ohtm` into Python dicts at import. Nested
dicts cost ~8× the file size in RAM: a 342 MB file measures 1258 MiB resident,
1599 MiB peak during load. Production sits at ~1.3 GB for the same reason.

The data is read-only and only ever accessed in small slices. Serving those slices
from a SQLite file instead measured **34 MiB** resident (~130 MiB with Dash loaded),
with per-query times of <1 ms for a heatmap, 0.7 ms for a topic's top words and
140 ms for a corpus-wide text scan.

## Schema

```sql
CREATE TABLE interview(
  iv         TEXT PRIMARY KEY,
  archive    TEXT,
  model_base TEXT,
  anonymized TEXT,
  chunk_ids  TEXT,   -- JSON list, defines row order of `weights`
  n_topics   INT,
  weights    BLOB    -- float32, (len(chunk_ids) × n_topics), C order
);

CREATE TABLE sent(
  iv TEXT, n INT, raw TEXT, cleaned TEXT,  -- cleaned: space-joined tokens
  speaker TEXT, chunk INT, time TEXT, tape TEXT
);
CREATE INDEX i_sent ON sent(iv, chunk);

CREATE TABLE words(topic INT, rank INT, weight REAL, word TEXT);
CREATE INDEX i_words ON words(topic, rank);

CREATE TABLE meta(key TEXT PRIMARY KEY, value TEXT);  -- JSON blobs
```

`meta` holds `settings`, `stopwords`, `topic_labels` and `correlation`. These are
small; load them into RAM at startup as today.

One interview's weights are a single blob, read with `np.frombuffer(...).reshape(...)`
— no copy, no per-chunk query.

## Build step

Conversion runs in `entrypoint.sh` at container start, reading `$OHTM_FILE` and
writing `/tmp/ohd.sqlite`. Took 9 s for 342 MB. Skip if the database is newer than
the source. This keeps the deployment interface unchanged — the operator still
mounts one `.ohtm` volume.

Peak RAM during conversion is the old peak (~1.6 GB) unless the converter streams.
Stream it with `ijson`, or accept a one-off spike before gunicorn starts.

## Access layer

Add `functions/basic_functions/store.py` with an `OhtmStore` class holding a
read-only connection (`file:/tmp/ohd.sqlite?mode=ro&immutable=1`). Connections are
thread-local — gunicorn runs 4 threads.

Methods, named after what callbacks actually need:

- `interview_weights(iv) -> (chunk_ids, np.ndarray)`
- `archive_weights(archive)` — iterate interviews, yielding the above
- `topic_words(topic, n)`
- `sentences(iv, chunk)`
- `search_cleaned(term)`
- `interviews()`, `settings`, `stopwords`, `topic_labels`

Callbacks receive the store in place of the `ohtm_file` dict.

## Migration order

1. **`weight`** — biggest win (628 of 1258 MiB in the profile). Touches
   `bar_graph.py`, `heat_maps.py`, `chronologie_heatmap_function.py`,
   `print_topic_search.py`, `print_sideboard_info.py`, `print_chunk_sents.py`.
2. **`corpus`** — sentence lookups and the text search.
3. **`words`** — smallest, mostly `print_topics.py`.

Each phase ships independently; keep the JSON path alive for the parts not yet moved.

## Risks

- **N+1 queries.** The nested loops in `bar_graph.py:177-334` currently index
  `[archive][interview][chunk][topic]` inside the innermost loop. Fetch the
  interview matrix once, then index the array. Getting this wrong turns a 1 ms
  callback into thousands of queries.
- **Text search.** `print_topic_search` scans the whole corpus. 140 ms with a
  `LIKE` on the synthetic data; move to FTS5 if real data is slower.
- **Float precision.** float32 rounds the stored weights. They are display and
  sort values, so this should be fine — confirm against a known heatmap.
- **Numbers are from a synthetic file** shaped to match the reported 1.3 GB, not
  from production. Run `profile_ohtm.py` against the real `ohd.ohtm` first to
  confirm `weight` really is the dominant key.

## Out of scope

Static site generation: Dash renders every interaction server-side and the inputs
are open-ended (free-text search, numeric fields, sliders), so there is no finite
set of pages to pregenerate without rewriting the app client-side.
