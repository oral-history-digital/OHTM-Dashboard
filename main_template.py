"""
OHTM-Dash-Board

"""

import json
import os

from ohtm_dash_function import ohd_dash

input_folder = r"C:\Users\phili\sciebo - Bayerschmidt, Philipp (bayerschmidt@fernuni-hagen.de)@fernuni-hagen.sciebo.de\Topic Modeling\ohtm_files"


if __name__ == "__main__":
    load_file_name = r"OHD_final_100c_100T_A5_remade.ohtm"
    with open(os.path.join(input_folder, load_file_name)) as f:
        ohtm_file = json.load(f)
    chronologie_analyse = False
    ohd_dash(ohtm_file, chronologie_analyse)
