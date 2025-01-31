"""

"""
import copy
from dash import ctx
import pandas as pd
import dash_bootstrap_components as dbc


def print_topic_search_weight(ohtm_file,
                              interview_id, t_1, t_2, t_3, t_4, text_search_options, topic_print, weight_print):
    if ctx.triggered[0]["prop_id"] == "enter_print.n_clicks":
        if text_search_options == "1":
            sent_final = []
            topic = topic_print
            weight = weight_print
            for archive in ohtm_file["weight"]:
                for interview in ohtm_file["weight"][archive]:
                    for chunks in ohtm_file["weight"][archive][interview]:
                        if str(ohtm_file["weight"][archive][interview][chunks][str(topic)]) >= str(weight):
                            if "e" in str(ohtm_file["weight"][archive][interview][chunks][str(topic)]):
                                next
                            else:
                                sent_id = interview
                                chunk_id = chunks
                                sent_current = []
                                for sents in ohtm_file["corpus"][archive][interview]["sent"]:
                                    int_sent = copy.deepcopy(
                                        ohtm_file["corpus"][archive][interview]["sent"][sents]["chunk"])
                                    if int(int_sent) == int(chunks):
                                        sent_current.append(
                                            str(ohtm_file["corpus"][archive][interview]["sent"][sents]["raw"]) + " ")
                                sent_current = " ".join(sent_current)
                                sent_current_2 = (str(ohtm_file["weight"][archive][interview][chunks][str(topic)]),
                                sent_id, chunk_id, sent_current)
                                sent_final.append(sent_current_2)
            sent_final.sort(reverse=True)
            df = pd.DataFrame(sent_final)
            df = df.round(3)
            df.columns = ["weight", "Interview", "Chunk Nr", "Chunk"]
            # data = df_rounded.to_dict('records')
            # columns = [{"name": i, "id": i} for i in df_rounded.columns]
            table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, color="light",
                                             responsive=True, )
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
                if str(ohtm_file["weight"][archive][interview][chunks][str(topic)]) >= str(weight):
                    if "e" in str(ohtm_file["weight"][archive][interview][chunks][str(topic)]):
                        next
                    else:
                        chunk_id = chunks
                        sent_current = []
                        for sents in ohtm_file["corpus"][archive][interview]["sent"]:
                            int_sent = copy.deepcopy(ohtm_file["corpus"][archive][interview]["sent"][sents]["chunk"])
                            if int(int_sent) == int(chunks):
                                sent_current.append(
                                    str(ohtm_file["corpus"][archive][interview]["sent"][sents]["raw"]) + " ")
                        sent_current = " ".join(sent_current)
                        sent_current_2 = (str(ohtm_file["weight"][archive][interview][chunks][str(topic)]),
                                          interview, chunk_id, sent_current)
                        sent_final.append(sent_current_2)
            sent_final.sort(reverse=True)
            df = pd.DataFrame(sent_final)

            df = df.round(3)
            df.columns = ["weight", "Interview", "Chunk Nr", "Chunk"]
            # data = df_rounded.to_dict('records')
            # columns = [{"name": i, "id": i} for i in df_rounded.columns]
            table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, color="dark",
                                             responsive=True, )
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