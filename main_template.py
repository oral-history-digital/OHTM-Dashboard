"""
OHTM-Dash-Board
"""

import json
import os

from ohtm_dash_function import create_ohd_dash

input_folder = r"C:\Users\phili\sciebo - Bayerschmidt, Philipp (bayerschmidt@fernuni-hagen.de)@fernuni-hagen.sciebo.de\Topic Modeling\ohtm_files"


if __name__ == "__main__":
    load_file_name = "OHD_final_adg_sorted.ohtm"
    # load_file_name = "ohtm_100c_130t.ohtm"
    with open(os.path.join(input_folder, load_file_name)) as f:
        ohtm_file = json.load(f)
    chronologie_analyse = False
    tooltip_bool = True
    app = create_ohd_dash(ohtm_file, chronologie_analyse)
    app.run(debug=True, port=3002)
