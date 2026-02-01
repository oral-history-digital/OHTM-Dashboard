"""
OHTM-Dash-Board
"""

import json
import os

from ohtm_dash_function import create_ohd_dash

input_folder = r""


if __name__ == "__main__":
    load_file_name = ""
    with open(os.path.join(input_folder, load_file_name)) as f:
        ohtm_file = json.load(f)
    chronologie_analyse = False
    pop_up_window = False
    axis_titel_option = False
    app = create_ohd_dash(ohtm_file, chronologie_analyse, pop_up_window, axis_titel_option)
    app.run(debug=False, port=3002)
