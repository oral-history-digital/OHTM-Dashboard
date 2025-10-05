"""
OHTM-Dash-Board
"""

import json
import os

from ohtm_dash_function import create_ohd_dash

#Set input_folder to the path, where the ohtm_file is
input_folder = r"path_to_ohtm_file"


if __name__ == "__main__":
    load_file_name = "ohtm_file_name"
    with open(os.path.join(input_folder, load_file_name)) as f:
        ohtm_file = json.load(f)
    chronologie_analyse = False
    tooltip_bool = True
    app = create_ohd_dash(ohtm_file, chronologie_analyse)
    app.run(debug=True, port=3002)
