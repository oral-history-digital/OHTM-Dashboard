"""
This function prints alle the sents, that are in one chunk, including the speakers.
"""
from dash import ctx
import pandas as pd

def chunk_sent_drawing(ohtm_file, click_data_input, chunk_number, interview_id, chronology_df, tc_indicator):
    if ctx.triggered[0]["prop_id"] == "+_button_frontpage.n_clicks":
        chunk_id = int(chunk_number) + 1
    elif ctx.triggered[0]["prop_id"] == "+_button_detail.n_clicks":
        chunk_id = int(chunk_number) + 1
    elif ctx.triggered[0]["prop_id"] == "-_button_frontpage.n_clicks":
        chunk_id = int(chunk_number) - 1
    elif ctx.triggered[0]["prop_id"] == "-_button_detail.n_clicks":
        chunk_id = int(chunk_number) - 1
    else:
        if tc_indicator:
            chronology_df = pd.read_json(chronology_df, orient='records')
            time_id = click_data_input["points"][0]["x"]
            try:
                row_index = chronology_df.index.get_loc(chronology_df[chronology_df["minute"] == time_id].index[0])
            except IndexError:
                # If due to rownding errors, the value is not found, we search for the next value near to the one.
                closest_match = chronology_df.iloc[(chronology_df["minute"] - time_id).abs().argmin()].name
                row_index = chronology_df.index.get_loc(closest_match)

            # die Information aus dem DF aus Chronology. Hier wird die Zeit und das zugehörige
            # DF gespeichert. Wir müssen zunächst den Index der Zeitangabe finden
            chunk_id = chronology_df.loc[row_index]["ind"]
            # mit dem Index der Zeitangabe kann hier der Chunkwert ausgelesen werden und als chunk_id übergeben werden
        else:
            chunk_id = click_data_input["points"][0]["x"]

    sent_example = []
    speaker = "None"
    for archive in ohtm_file["corpus"]:
        if interview_id in ohtm_file["corpus"][archive]:
            for sentence_number in ohtm_file["corpus"][archive][interview_id]["sent"]:
                if ohtm_file["corpus"][archive][interview_id]["sent"][sentence_number]["chunk"] == int(chunk_id):
                    if ohtm_file["corpus"][archive][interview_id]["sent"][sentence_number]["speaker"] == {}:
                        sent_example.append(ohtm_file["corpus"][archive][interview_id]["sent"][sentence_number]["raw"] + " ")
                    else:
                        if speaker == ohtm_file["corpus"][archive][interview_id]["sent"][sentence_number]["speaker"]:
                            sent_example.append(ohtm_file["corpus"][archive][interview_id]["sent"][sentence_number]["raw"] + ". ")
                        else:
                            sent_example.append("\n" + "*" + ohtm_file["corpus"][archive][interview_id]["sent"][sentence_number]["speaker"] + "*: ")
                            sent_example.append(ohtm_file["corpus"][archive][interview_id]["sent"][sentence_number]["raw"] + ". ")
                            speaker = ohtm_file["corpus"][archive][interview_id]["sent"][sentence_number]["speaker"]

    sent_id = "Chunk: " + str(chunk_id)
    return sent_example, sent_id, chunk_id
