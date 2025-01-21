from builtins import print
import pandas as pd
import plotly_express as px
from ohtm_dash.functions.basic_functions.convert_ohtm_file import convert_ohtm_file


def heatmap_corpus(ohtm_file, option_selected: str = "all",
                   show_fig: bool = True, return_fig: bool = False, z_score_global: str = "True"):

    ohtm_file = convert_ohtm_file(ohtm_file)

    if "z_score" in z_score_global:
        z_score = True
    else:
        z_score = False

    if ohtm_file["settings"]["topic_modeling"]["trained"] == "True":
        if option_selected == "all":
            heat_dic = {}
            for archive in ohtm_file["weight"]:
                for interview in ohtm_file["weight"][archive]:
                    heat_dic[interview] = {}
                    count = 0
                    for c in ohtm_file["weight"][archive][interview]:
                        count += 1
                        for t in ohtm_file["weight"][archive][interview][c]:
                            if t not in heat_dic[interview]:
                                heat_dic[interview].update({t: ohtm_file["weight"][archive][interview][c][t]})
                            else:
                                heat_dic[interview].update(
                                    {t: heat_dic[interview][t] + ohtm_file["weight"][archive][interview][c][t]})
                    for entry in heat_dic[interview]:
                        heat_dic[interview].update({entry: heat_dic[interview][entry] / count})
            df = pd.DataFrame.from_dict(heat_dic)
        else:
            archive = option_selected
            heat_dic = {}
            for interview in ohtm_file["weight"][archive]:
                heat_dic[interview] = {}
                count = 0
                for c in ohtm_file["weight"][archive][interview]:
                    count += 1
                    for t in ohtm_file["weight"][archive][interview][c]:
                        if t not in heat_dic[interview]:
                            heat_dic[interview].update({t: ohtm_file["weight"][archive][interview][c][t]})
                        else:
                            heat_dic[interview].update(
                                {t: heat_dic[interview][t] + ohtm_file["weight"][archive][interview][c][t]})
                for entry in heat_dic[interview]:
                    heat_dic[interview].update({entry: heat_dic[interview][entry] / count})

            df = pd.DataFrame.from_dict(heat_dic)

        if z_score:
            mean = df.mean()
            std_dev = df.std()
            z_scores = ((df - mean) / std_dev)
            df = z_scores

        df = df.swapaxes("index", "columns")
        fig = px.imshow(df, color_continuous_scale='dense', aspect='auto')
        fig.update_traces(hovertemplate="Interview: %{y}" "<br>Topic: %{x}" "<br>Weight: %{z}<extra></extra>")
        fig.update_layout(clickmode='event+select')
        fig.update_layout(clickmode='event+select')
        fig.update(layout_coloraxis_showscale=False)
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
        if show_fig:
            fig.show()
        if return_fig:
            return fig

    else:
        print("No Topic Model trained")


"""
This function has to be tested in the dash. Because now it is really slow. With the chagen to possilbe different 
archive namens than the first 3 letters of the interview id, i had to find another way. Maye this function has to be
improved. (17.1.2025)


"""


def heatmap_interview(ohtm_file, interview_id: str = "", show_fig: bool = True,
                      return_fig: bool = False, heatmap_filter: list = ""):
    ohtm_file = convert_ohtm_file(ohtm_file)
    tc_indictator = False
    if "z_score" in heatmap_filter:
        z_score = True
    else:
        z_score = False
    if ohtm_file["settings"]["topic_modeling"]["trained"] == "True":
        dff = {}
        for archive in ohtm_file["weight"]:
            if interview_id in ohtm_file["weight"][archive]:
                for chunks in ohtm_file["weight"][archive][interview_id]:
                    dff[chunks] = ohtm_file["weight"][archive][interview_id][chunks]

        df = pd.DataFrame.from_dict(dff)
        df.index = pd.to_numeric(df.index)

        # Berechnung der z-Standardisierung
        if z_score:
            mean = df.mean()
            std_dev = df.std()
            z_scores = ((df - mean)/std_dev)
            df = z_scores
            df.index = pd.to_numeric(df.index)

        fig = px.imshow(df, color_continuous_scale='dense')
        fig.update_traces(hovertemplate="Chunk: %{x}" "<br>Topic: %{y}" "<br>Weight: %{z}<extra></extra>")
        fig.update_traces(showlegend=False)
        fig.update_traces(showscale=False)
        fig.update(layout_coloraxis_showscale=False)
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
        if show_fig:
            fig.show()
        if return_fig:
            return fig, df, tc_indictator

    else:
        print("No Topic Model trained")
