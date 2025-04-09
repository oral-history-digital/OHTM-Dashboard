"""
OHTM-Dash-Board server
"""
import json
import os
from pathlib import Path

from ohtm_dash_function import create_ohd_dash


ohtm_file = os.environ.get("OHTM_FILE")

if ohtm_file:
    with open(Path(ohtm_file)) as f:
        ohtm_json = json.load(f)
        app = create_ohd_dash(ohtm_json)
        # gunicorn ohtm_dash_server:server
        server = app.server
