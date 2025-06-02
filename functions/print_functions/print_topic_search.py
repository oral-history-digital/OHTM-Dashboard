""" """

import copy
from copy import deepcopy
from functions.basic_functions.create_link_to_ohd import create_link
import dash_bootstrap_components as dbc
import pandas as pd
from dash import ctx, html


def print_topic_search_weight(
    ohtm_file,
    interview_id,
    t_1,
    t_2,
    t_3,
    t_4,
    text_search_options,
    topic_print,
    weight_print,
):
    anonymized_status = False
    if ctx.triggered[0]["prop_id"] == "enter_print.n_clicks":
        if text_search_options == "1":
            sent_final = []
            topic = topic_print
            weight = weight_print
            link_tape = "1"
            for archive in ohtm_file["weight"]:
                for interview in ohtm_file["weight"][archive]:
                    try:
                        if ohtm_file["corpus"][archive][interview]["anonymized"] == "True":
                            anonymized_status = True
                    except KeyError:
                        anonymized_status = False
                    for chunks in ohtm_file["weight"][archive][interview]:
                        chunk_start_marker = 0
                        speaker = "None"
                    for chunks in ohtm_file["weight"][archive][interview]:
                        if str(ohtm_file["weight"][archive][interview][chunks][str(topic)]) >= str(weight):
                            if "e" in str(ohtm_file["weight"][archive][interview][chunks][str(topic)]):
                                next
                            else:
                                sent_id = interview
                                chunk_id = chunks
                                sent_current = []
                                for number in ohtm_file["corpus"][archive][interview]["sent"]:
                                    int_sent = copy.deepcopy(ohtm_file["corpus"][archive][interview]["sent"][number ]["chunk"])
                                    if int(int_sent) == int(chunks):
                                        chunk_start_marker += 1
                                        if chunk_start_marker == 1:  # to mark the beginning of the chunk for the first timecode
                                            if ohtm_file["corpus"][archive][interview]["sent"][number]["time"] != {}:
                                                timcodes_available = True
                                                chunk_start_time = \
                                                    ohtm_file["corpus"][archive][interview]["sent"][number]["time"]
                                                link_tape = \
                                                    ohtm_file["corpus"][archive][interview]["sent"][number]["tape"]
                                            else:
                                                timcodes_available = False
                                                link_tape = "1"
                                                chunk_start_time = "False"
                                        if ohtm_file["corpus"][archive][interview]["sent"][number]["speaker"] == {}:
                                            sent_current.append(str(
                                                ohtm_file["corpus"][archive][interview]["sent"][number]["raw"]) + " ")
                                            chunk_end_time = \
                                                ohtm_file["corpus"][archive][interview]["sent"][number]["time"]
                                        else:
                                            if speaker == ohtm_file["corpus"][archive][interview]["sent"][number][
                                                "speaker"]:
                                                sent_current.append(str(
                                                    ohtm_file["corpus"][archive][interview]["sent"][number][
                                                        "raw"]) + " ")
                                                chunk_end_time = \
                                                    ohtm_file["corpus"][archive][interview]["sent"][number]["time"]
                                            else:
                                                sent_current.append(str("*" +
                                                                        ohtm_file["corpus"][archive][interview]["sent"][
                                                                            number]["speaker"]) + ":* ")
                                                sent_current.append(str(
                                                    ohtm_file["corpus"][archive][interview]["sent"][number][
                                                        "raw"]) + " ")
                                                speaker = ohtm_file["corpus"][archive][interview]["sent"][number][
                                                    "speaker"]
                                                chunk_end_time = \
                                                    ohtm_file["corpus"][archive][interview]["sent"][number]["time"]

                                sent_current = " ".join(sent_current)
                                top_ts = ohtm_file["weight"][archive][interview][chunks]
                                top_ts_sorted = sorted(top_ts.items(), key=lambda x: x[1], reverse=True)
                                final_topic_list = []
                                for entry in top_ts_sorted[:5]:
                                    final_topic_list.append(str(entry[0]) + ": " + str(entry[1]))
                                final_topic_list = " | ".join(final_topic_list)
                                if timcodes_available:
                                    sent_current += (
                                        "\n" + "\n" + "Timecode: " + str(chunk_start_time) + "–" + str(
                                            chunk_end_time))
                                else:
                                    chunk_start_time = "False"
                                    link_tape = "1"
                                if anonymized_status:
                                    link = create_link(archive.lower(), interview.lower(), chunk_start_time,
                                                       link_tape)
                                    sent_current = ("This interview is anonymized and can be found here: " + "\n",
                                                    html.A(link, href=link, target="_blank",
                                                           style={'color': 'blue'}))
                                else:
                                    link = create_link(archive.lower(), interview.lower(), chunk_start_time,
                                                       link_tape)
                                    sent_current = [sent_current, "\n",
                                                     html.A(link, href=link, target="_blank", style={'color': 'blue'})]

                                print(sent_current)

                                sent_current_2 = (str(ohtm_file["weight"][archive][interview][chunks][str(topic)]),
                                    sent_id,
                                    chunk_id,
                                    sent_current,
                                    final_topic_list,
                                )
                                print(sent_current_2)
                                sent_final.append(sent_current_2)
            sent_final.sort(reverse=True, key=lambda x: x[0])
            df = pd.DataFrame(sent_final)
            df = df.round(3)
            df.columns = ["weight", "Interview", "Chunk Nr", "Chunk", "Top 5 Topics"]
            # data = df_rounded.to_dict('records')
            # columns = [{"name": i, "id": i} for i in df_rounded.columns]
            table = dbc.Table.from_dataframe(
                df,
                striped=True,
                bordered=True,
                hover=True,
                color="light",
                responsive=True,
            )
            return table

        if text_search_options == "2":
            sent_final = []
            topic = topic_print
            weight = weight_print
            for archive in ohtm_file["corpus"]:
                if interview_id in ohtm_file["corpus"][archive]:
                    archive = archive
            interview = interview_id
            for chunks in ohtm_file["weight"][archive][interview]:
                if str(
                    ohtm_file["weight"][archive][interview][chunks][str(topic)]
                ) >= str(weight):
                    if "e" in str(
                        ohtm_file["weight"][archive][interview][chunks][str(topic)]
                    ):
                        next
                    else:
                        chunk_id = chunks
                        sent_current = []
                        for sents in ohtm_file["corpus"][archive][interview]["sent"]:
                            int_sent = copy.deepcopy(
                                ohtm_file["corpus"][archive][interview]["sent"][sents][
                                    "chunk"
                                ]
                            )
                            if int(int_sent) == int(chunks):
                                sent_current.append(
                                    str(
                                        ohtm_file["corpus"][archive][interview]["sent"][
                                            sents
                                        ]["raw"]
                                    )
                                    + " "
                                )
                        sent_current = " ".join(sent_current)
                        sent_current_2 = (
                            str(
                                ohtm_file["weight"][archive][interview][chunks][
                                    str(topic)
                                ]
                            ),
                            interview,
                            chunk_id,
                            sent_current,
                        )
                        sent_final.append(sent_current_2)
            sent_final.sort(reverse=True)
            df = pd.DataFrame(sent_final)

            df = df.round(3)
            df.columns = ["weight", "Interview", "Chunk Nr", "Chunk"]
            # data = df_rounded.to_dict('records')
            # columns = [{"name": i, "id": i} for i in df_rounded.columns]
            table = dbc.Table.from_dataframe(
                df,
                striped=True,
                bordered=True,
                hover=True,
                color="dark",
                responsive=True,
            )
            return table


# will be added with chronology_pipeline
# if text_search_options == "3":
#     a = global_vertical_correlation_search_json(ohtm_file, t1=t_1, t2=t_2, t3=t_3, t4=t_4, return_search=True)
#     df = pd.DataFrame(a)
#     df.columns = ["Interview", "Chunk Nr"]
#     table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, color="dark",
#                                      responsive=True, )
#     return table
#
# if text_search_options == "4":
#     a = global_horizontal_correlation_search_json(ohtm_file, t1=t_1, t2=t_2, return_search=True)
#     df = pd.DataFrame(a)
#     df.columns = ["Interview", "Chunk Nr"]
#     table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, color="dark",
#                                      responsive=True, )
#     return table
