"""
OHTM-Dash-Board server
"""

import json
import os
from pathlib import Path

from ohtm_dash_function import create_ohd_dash


ohtm_file = os.environ.get("OHTM_FILE")

# The corpus repeats a small set of strings across ~1M sentences: `speaker` has
# one distinct value, `tape` sixteen, `time` about 223k out of 1M. json builds a
# fresh str for every occurrence. Sharing them during the parse -- not after, or
# the allocator keeps the freed pages -- cuts resident memory by ~170 MiB.
_seen: dict[str, str] = {}


def _share_strings(pairs):
    return {k: (_seen.setdefault(v, v) if type(v) is str else v) for k, v in pairs}


if ohtm_file:
    with open(Path(ohtm_file)) as f:
        ohtm_json = json.load(f, object_pairs_hook=_share_strings)

        app = create_ohd_dash(
            ohtm_file=ohtm_json,
            chronologie_analyse=True,
            pop_up_window=True,
            axis_titel_option=True,
            sideboard_start_settings = True
        )
        # gunicorn ohtm_dash_server:server
        server = app.server
