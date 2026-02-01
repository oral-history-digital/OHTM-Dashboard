""" """

import json

import dash_bootstrap_components as dbc
import pandas as pd
from dash import ctx
import ast


def print_all_topics(words, nClicks, ohtm_file, options: list = ""):
    if (
        ctx.triggered[0]["prop_id"] == "enter_print_topics.n_clicks"
        or "side_bar_menu_switch.value"
    ):
        number_of_words = words
        data = []
        for topic in ohtm_file["words"]:
            data_topic = []
            out_line = []
            for i in range(number_of_words):
                out_line.append((ohtm_file["words"][topic])[i][1] + ", ")
            data_topic = (int(topic), out_line)
            data.append(data_topic)
        df = pd.DataFrame(data)
        df.columns = ["Topic", "Words"]

        if (
            "topic_cluster_on" in options
            and ohtm_file["settings"]["labeling_options"]["clustering"] == True
        ):
            topic_groups = ohtm_file["topic_labels"]["clusters"]
            rows = []
            for _, (category, topics_str) in topic_groups.items():
                # String -> Liste -> Strings
                topics = [int(x) for x in ast.literal_eval(topics_str)]

                # Überschrift hinzufügen
                rows.append({"Topic": f"=== {category} ===", "Words": ""})

                # passende Zeilen aus df einfügen
                subset = df[df["Topic"].isin(topics)].sort_values("Topic")
                for _, row in subset.iterrows():
                    rows.append({"Topic": row["Topic"], "Words": row["Words"]})

            # Neues DataFrame
            df = pd.DataFrame(rows)
        if (
            "topic_labels_on" in options
            and ohtm_file["settings"]["labeling_options"]["labeling"] == True
        ):
            topic_labels = ohtm_file["topic_labels"]["labels"]

            def map_topic(value):
                try:
                    # Versuch, den Wert als int zu interpretieren
                    key = int(value)
                    return topic_labels.get(str(key), f"Unbekannt ({key})")
                except ValueError:
                    # Kein int → z.B. Überschrift, einfach behalten
                    return value

            df["Topic"] = df["Topic"].apply(map_topic)

        table = dbc.Table.from_dataframe(
            df,
            striped=True,
            bordered=True,
            hover=True,
            color="light",
            responsive=True,
        )

        return table


def top_words(ohtm_file, top_dic):
    if type(top_dic) is not dict:
        top_dic = json.loads(top_dic)
    else:
        top_dic = top_dic
    word_dic = {}
    for top_words in top_dic["words"]:
        out_line = []
        for i in range(30):
            out_line.append((top_dic["words"][top_words])[i][1])
        word_dic[top_words] = out_line

    word_dic2 = {}
    for entry in word_dic:
        line = ""
        for out in word_dic[entry]:
            line += out + ", "
        word_dic2[entry] = line
    df1 = pd.DataFrame.from_dict(word_dic2, orient="index")
    df2 = df1.loc[str(ohtm_file)]
    return df2
