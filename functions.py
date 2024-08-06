import json

import pandas as pd
import plotly_express as px


def top_words(topic, top_dic):
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
    df2 = df1.loc[str(topic)]
    return df2


def time_graph(top_dic, topic_number):

    if type(top_dic) is not dict:
        top_dic = json.loads(top_dic)
    else:
        top_dic = top_dic

    if top_dic["settings"]["topic_modeling"]["trained"] == "True":
        weight = []
        for archive in top_dic["weight"]:
            for interview in top_dic["weight"][archive]:
                count = 0
                topic_weight = 0
                for chunk in top_dic["weight"][archive][interview]:
                    count += 1
                    topic_weight += top_dic["weight"][archive][interview][chunk][topic_number]
                weight.append((top_dic["corpus"][archive][interview]["year"], (topic_weight/count)))

    sorted(weight, key=lambda tupel: tupel[0])

    weight_2= []
    for entry in weight:
        try:
            if int(entry[0]):
                weight_2.append((int(entry[0]), entry[1]))
        except ValueError:
            next

    # Konvertierung der Liste von Tupeln in ein DataFrame
    df = pd.DataFrame(weight_2, columns=['X', 'Y'])
    df.index = pd.to_numeric(df.index)
    df.sort_index(inplace=True)

    print(df)

    fig = px.line(df)
    fig.update_xaxes(type = "category")

    # Anzeigen des Graphen
    return fig
