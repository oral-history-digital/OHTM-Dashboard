from OHDdash_function import ohd_dash
import json

workingfolder = "C:\\Users\\phili\\Nextcloud2\\Python\\Topic_Modeling\\"
#workingfolder = "C:\\Users\\bayerschmidt\\Nextcloud\\Python\\Project\\ohtm_dash\\OHDdash_files\\"



file_workingfolder = "C:\\Users\\phili\\sciebo - Bayerschmidt, Philipp (bayerschmidt@fernuni-hagen.de)@fernuni-hagen.sciebo.de\\Topic Modeling\\main test\\github_test\\"
#file_workingfolder = "C:\\Users\\bayerschmidt\\sciebo - Bayerschmidt, Philipp (bayerschmidt@fernuni-hagen.de)@fernuni-hagen.sciebo.de\\Topic Modeling\\main test\\"


image_filename = workingfolder + "OHD_Logo.png"

if __name__ == '__main__':
    load_file_name = "Test_1.ohtm"
    # load_file_name = "OHD_auswahl_pre_150c_80t"

    with open(file_workingfolder + load_file_name) as f:
        top_dic = json.load(f)
    ohd_dash(top_dic, image_filename)
