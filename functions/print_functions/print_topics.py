
"""

"""
from dash import ctx
import pandas as pd
import dash_bootstrap_components as dbc
import json

def print_all_topics(words, nClicks, ohtm_file):
    if ctx.triggered[0]["prop_id"] == "enter_print_topics.n_clicks":
        number_of_words = words
        data = []
        for topic in ohtm_file["words"]:
            data_topic = []
            out_line = []
            for i in range(number_of_words):
                out_line.append((ohtm_file["words"][topic])[i][1] + ", ")
            data_topic = (topic, out_line)
            data.append(data_topic)
        df = pd.DataFrame(data)
        df.columns = ["Topic", "Words"]
        table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, color="light", responsive=True, )

        return table


def top_words(ohtm_file, top_dic):
    if type(top_dic) is not dict:
        top_dic = json.loads(top_dic)
    else:
        top_dic = top_dic
    word_dic = {}
    for top_words in top_dic["words"]:
        out_line = []
        for i in range(50):
            out_line.append((top_dic["words"][top_words])[i][1])
        word_dic[top_words] = out_line

    word_dic2 = {}
    for entry in word_dic:
        line = ""
        for out in word_dic[entry]:
            line += out + ", "
        word_dic2[entry] = line
    df1 = pd.DataFrame.from_dict(word_dic2, orient='index')
    df2 = df1.loc[str(ohtm_file)]
    return df2