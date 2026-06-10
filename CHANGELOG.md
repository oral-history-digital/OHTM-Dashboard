# Changelog

All notable changes to this project will be documented in this file.

## [0.3.3] - 2026-06-10

### New Features

- **Favicon and tab title** — Added a favicon (`assets/favicon.ico`) shown in the browser tab.
- **Front-page chunk navigation tooltips** — New tooltips for the chunk display on the overview page (chunk number, previous/next buttons, interview ID input and display, heatmap marker switch).

### Improvements

- **Page-specific tooltips** — `tooltip_creation` now receives the current URL path and only renders the tooltips for the active page instead of all tooltips at once. The separate sidebar tooltip callback (`menu_tooltip`) was merged into a single callback that reacts to both the tooltip switch and page changes.
- **Scrollable sidebar** — The sidebar now scrolls (`overflowY: auto`) when its content exceeds the viewport height; sidebar row margins were tightened and the search-info badge now wraps long text instead of overflowing.
- **Text search layout** — The result table in the text search view now uses the full content width (removed the fixed 8-column width).
- **"Sammlung" wording** — The bar graph hover labels now read "Sammlung" instead of "Archiv", matching the legend titles introduced in 0.3.2.
- **Info page** — The "Weitere Informationen" reference is now a clickable link, and the closing quotation mark in "Archiv „Deutsches Gedächtnis"" was fixed.
- **Code cleanup** — Removed unused imports (`copy`, `deepcopy`, `json`, `plotly`, `html`) across several modules.

### Bug Fixes

- **Merge-conflict leftovers** — Removed remaining merge-conflict artifacts from the tooltip callback and a duplicated, nested sidebar row that broke the layout.

### Infrastructure

- The server (`ohtm_dash_server.py`) now starts the dashboard with `sideboard_start_settings=True`, so topic labels and tooltips are enabled by default.

## [0.3.2] - 2026-06-09

### New Features

- **Configurable start settings** — Added a `sideboard_start_settings` parameter to `create_ohd_dash`. When enabled, the dashboard starts with topic labels and tooltips switched on by default.
- **Linked logo** — The sidebar logo is now a clickable link to the Oral History Digital project.
- **Bar graph legend titles** — The corpus and chunk-view bar graphs now show "Sammlungen" as the legend title.

### Improvements

- **Reworked Info/Impressum page** — Rewrote the notice text with an updated project description (681 interviews across 24 collections), anonymization note, ICA mention, and project credits. Moved the collection abbreviations here (sorted alphabetically) and added links to the Archiv "Deutsches Gedächtnis", the interview portal, the project, and the legal notice. The "Impressum" button is now labeled "Info".
- **Reworked Glossar page** — Replaced the abbreviation list with explanations of the core concepts (Topic Modeling, Topic, Corpus, Sammlung, Chunk, Topic-Wort-Verteilung, Topic-Dokument-Verteilung).
- **Tooltip overhaul** — Corrected spelling, grammar, and hyphenation across all tooltips (e.g. "Topic-Verteilung"), switched to formal "Sie", and filled in the remaining placeholder/"To DO" tooltips, including the ICA threshold/outlier tooltips and new tooltips for the front-page chunk navigation.
- **UI styling** — Recolored the sidebar and content panels to a light theme (`#e6f0f1`), grouped the Info and Glossar buttons in a single row, and adjusted sidebar font sizes.

### Bug Fixes

- **ICA tooltip targets** — Fixed mismatched tooltip targets (`ihc_*` → `ica_*`) so the ICA threshold and outlier tooltips display correctly.
- **Tooltips on initial load** — Tooltips now render on first load instead of only after a switch toggle.

## [0.3.1] - 2026-05-13

### New Features

- **Glossar page** — Added a glossary view listing all archive abbreviations (SLB, VHSS, DVE, etc.) with their full names.
- **Impressum page** — Added a legal notice page with project description and links to the Oral History Digital project and archive portal.
- **ICA toggle in sidebar** — The ICA (Interview-Chronologie-Analyse) switch is now shown in the sidebar menu when `chronologie_analyse=True`, making it conditionally available based on the dataset.
- **Extended OHD link support** — `create_link_to_ohd` now resolves links for ~25 archive collections (previously only `adg`). All collections hosted at `deutsches-gedaechtnis.fernuni-hagen.de` are now supported.
- **New `create_ohd_dash` parameters** — Added `pop_up_window` and `axis_titel_option` flags for finer control over the dashboard layout.

### Bug Fixes

- **ICA float error** — Fixed a float conversion error in the chronology heatmap that caused crashes when processing certain time values.
- **ICA sentence drawing** — Fixed rendering issues in `print_chunk_sents` related to the ICA sentence-level display.
- **IHC compatibility** — Improved compatibility with the IHC data format; removed the now-redundant `sicherung_p1.py` backup file.

### Improvements

- **Sidebar options refactored** — Checklist options for the sidebar are now generated by `option_switch_sidebar_function`, making them dynamic based on analysis mode.
- **Code cleanup** — Removed large blocks of commented-out code (notes textarea, correlation accordion panel).

### Infrastructure

- Python updated from 3.13.8 → 3.13.13
- Dash updated from 3.2.0 → 3.4.0
- Gunicorn updated from 23.0.0 → 25.0.1
- Dependencies refreshed (`uv.lock`)
