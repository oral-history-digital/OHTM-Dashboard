"""
This code clusters the bar graph and the heat maps to the cluster lists stored in
ohtm_file["topic_labels"]["clusters"].
It was coded with ChatGPT
"""

import ast
import pandas as pd


def df_regroup_clusters_bar(df, ohtm_cluster):
    groups_raw = []
    for entry in ohtm_cluster:
        groups_raw.append(ohtm_cluster[entry][1])
    groups = [ast.literal_eval(g) for g in groups_raw]
    mapping = {}
    for group_id, rows in enumerate(groups):
        for r in rows:
            mapping[r] = group_id

    # nur die Zeilen berücksichtigen, die auch im Mapping sind
    map_list = [mapping[i] for i in range(len(df)) if i in mapping]
    filtered_df = df.loc[list(mapping.keys())]
    new_df = filtered_df.groupby(map_list).sum()
    labels_dict = ohtm_cluster
    new_df["Label"] = new_df.index.map(lambda x: labels_dict.get(str(x), "unknown"))

    return new_df


def df_regroup_clusters_heat(df, ohtm_cluster):
    groups = ohtm_cluster
    grouped = pd.DataFrame(
        {
            key: df[
                [
                    str(c)
                    for c in (
                        cols if isinstance(cols, list) else ast.literal_eval(cols)
                    )
                ]
            ].sum(axis=1)
            for key, (_, cols) in groups.items()
        }
    )

    # Separate labels for hovertext
    labels = {key: f"{label} | Topics: {rows}" for key, (label, rows) in groups.items()}

    new_df = grouped

    return new_df, labels
