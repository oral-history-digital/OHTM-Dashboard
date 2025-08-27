import pandas as pd
import plotly.express as px
from functions.basic_functions.convert_ohtm_file import convert_ohtm_file

def bar_graph_corpus(ohtm_file, show_fig: bool = True, return_fig: bool = False):
    ohtm_file = convert_ohtm_file(ohtm_file)
    if ohtm_file["settings"]["topic_modeling"]["trained"] == "True":
        interview_dic = {}
        for archive in ohtm_file["weight"]:
            if archive not in interview_dic:
                interview_dic[archive] = {}
            for interview in ohtm_file["weight"][archive]:
                interview_dic[archive][interview] = {}
                count = 0
                for c in ohtm_file["weight"][archive][interview]:
                    count += 1
                    for t in ohtm_file["weight"][archive][interview][c]:
                        if t not in interview_dic[archive][interview]:
                            interview_dic[archive][interview].update(
                                {t: ohtm_file["weight"][archive][interview][c][t]}
                            )
                        else:
                            interview_dic[archive][interview].update(
                                {
                                    t: interview_dic[archive][interview][t]
                                    + ohtm_file["weight"][archive][interview][c][t]
                                }
                            )
                for entry in interview_dic[archive][interview]:
                    interview_dic[archive][interview].update(
                        {entry: interview_dic[archive][interview][entry] / count}
                    )

        bar_dic = {}
        for archive in interview_dic:
            bar_dic[archive] = {}
            count = 0
            for interview in interview_dic[archive]:
                count += 1
                for t in interview_dic[archive][interview]:
                    if t not in bar_dic[archive]:
                        bar_dic[archive].update(
                            {t: interview_dic[archive][interview][t]}
                        )
                    else:
                        bar_dic[archive].update(
                            {
                                t: bar_dic[archive][t]
                                + interview_dic[archive][interview][t]
                            }
                        )
            for entry in bar_dic[archive]:
                bar_dic[archive].update({entry: bar_dic[archive][entry]})

        df = pd.DataFrame.from_dict(bar_dic)

        # Min-Max-Normalisierung: Skalieren Sie die Daten auf den Wertebereich [0, 1]
        min_val = df.min()
        max_val = df.max()
        normalized_data = (df - min_val) / (max_val - min_val)
        df.index = pd.to_numeric(df.index)

        fig = px.bar(df, color_discrete_sequence=px.colors.qualitative.G10)
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
        fig.update_layout(
            xaxis_title=None,  # Entfernt die X-Achsenbeschriftung
            yaxis_title=None,  # Entfernt die Y-Achsenbeschriftung
        )
        if show_fig:
            fig.show()
        if return_fig:
            return fig
    else:
        print("No Topic Model trained")


def bar_graph_cv_function(
    ohtm_file,
    option_selected: str = "all",
    show_fig: bool = False,
    return_fig: bool = True,
    topic_1_number: int = 0,
    topic_1_weight: float = 0,
    topic_2_number: int = 0,
    topic_2_weight: float = 0,
    correlation: list = ""
):
    if option_selected == "None":
        option_selected = "all"
    if topic_1_number == "None":
        print("Select a Topic Numer first")
    if topic_1_weight == "None":
        print("Select Topic Weight first")

    ohtm_file = convert_ohtm_file(ohtm_file)
    if ohtm_file["settings"]["topic_modeling"]["trained"] == "True":
        heat_cv_dic = {}
        if option_selected == "all":
            for archive in ohtm_file["weight"]:
                for interview in ohtm_file["weight"][archive]:
                    for chunks in ohtm_file["weight"][archive][interview]:
                        if "correlation_cv" in correlation:
                            if str(ohtm_file["weight"][archive][interview][chunks][str(topic_1_number)]) >= str(topic_1_weight):
                                    if "e" in str(ohtm_file["weight"][archive][interview][chunks][str(topic_1_number)]):
                                        next
                                    else:
                                      if str(ohtm_file["weight"][archive][interview][chunks][str(topic_2_number)]) >= str(topic_2_weight):
                                        if "e" in str(ohtm_file["weight"][archive][interview][chunks][str(topic_1_number)]):
                                            next
                                        else:
                                            if archive not in heat_cv_dic:
                                                heat_cv_dic[archive] = {}
                                                heat_cv_dic[archive] = dict(ohtm_file["weight"][archive][interview][chunks])
                                            else:
                                                for topics in ohtm_file["weight"][archive][interview][chunks]:
                                                    old_value = heat_cv_dic[archive][topics]
                                                    heat_cv_dic[archive][topics] = float(old_value) + float(ohtm_file["weight"][archive][interview][chunks][topics])
                        else:
                            if str(ohtm_file["weight"][archive][interview][chunks][str(topic_1_number)]) >= str(topic_1_weight):
                                if "e" in str(ohtm_file["weight"][archive][interview][chunks][str(topic_1_number)]):
                                    next
                                else:
                                    if archive not in heat_cv_dic:
                                        heat_cv_dic[archive] = {}
                                        heat_cv_dic[archive] = dict(ohtm_file["weight"][archive][interview][chunks])
                                    else:
                                        for topics in ohtm_file["weight"][archive][interview][chunks]:
                                            old_value = heat_cv_dic[archive][topics]
                                            heat_cv_dic[archive][topics] = float(old_value) + float(ohtm_file["weight"][archive][interview][chunks][topics])

        else:
            archive = option_selected
            for interview in ohtm_file["weight"][archive]:
                    for chunks in ohtm_file["weight"][archive][interview]:
                        if "correlation_cv" in correlation:
                            if str(ohtm_file["weight"][archive][interview][chunks][str(topic_1_number)]) >= str(topic_1_weight):
                                    if "e" in str(ohtm_file["weight"][archive][interview][chunks][str(topic_1_number)]):
                                        next
                                    else:
                                      if str(ohtm_file["weight"][archive][interview][chunks][str(topic_2_number)]) >= str(topic_2_weight):
                                        if "e" in str(ohtm_file["weight"][archive][interview][chunks][str(topic_1_number)]):
                                            next
                                        else:
                                            if archive not in heat_cv_dic:
                                                heat_cv_dic[archive] = {}
                                                heat_cv_dic[archive] = dict(ohtm_file["weight"][archive][interview][chunks])
                                            else:
                                                for topics in ohtm_file["weight"][archive][interview][chunks]:
                                                    old_value = heat_cv_dic[archive][topics]
                                                    heat_cv_dic[archive][topics] = float(old_value) + float(ohtm_file["weight"][archive][interview][chunks][topics])
                        else:
                            if str(ohtm_file["weight"][archive][interview][chunks][str(topic_1_number)]) >= str(topic_1_weight):
                                if "e" in str(ohtm_file["weight"][archive][interview][chunks][str(topic_1_number)]):
                                    next
                                else:
                                    if archive not in heat_cv_dic:
                                        heat_cv_dic[archive] = {}
                                        heat_cv_dic[archive] = dict(ohtm_file["weight"][archive][interview][chunks])
                                    else:
                                        for topics in ohtm_file["weight"][archive][interview][chunks]:
                                            old_value = heat_cv_dic[archive][topics]
                                            heat_cv_dic[archive][topics] = float(old_value) + float(ohtm_file["weight"][archive][interview][chunks][topics])

        for entry in heat_cv_dic:
            heat_cv_dic[entry][str(topic_1_number)] = 0
        if "correlation_cv" in correlation:
            for entry in heat_cv_dic:
                heat_cv_dic[entry][str(topic_2_number)] = 0 
        df_bar_cv = pd.DataFrame.from_dict(heat_cv_dic)
        min_val = df_bar_cv.min()
        max_val = df_bar_cv.max()
        normalized_data = (df_bar_cv - min_val) / (max_val - min_val)

        df_bar_cv.index = pd.to_numeric(df_bar_cv.index)
        fig = px.bar(df_bar_cv, color_discrete_sequence=px.colors.qualitative.G10)
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
        fig.update_layout(
            xaxis_title=None,  # Entfernt die X-Achsenbeschriftung
            yaxis_title=None,  # Entfernt die Y-Achsenbeschriftung
        )
        if show_fig:
            fig.show()
        if return_fig:
            return fig
        
    else:
        print("No Topic Model trained")




