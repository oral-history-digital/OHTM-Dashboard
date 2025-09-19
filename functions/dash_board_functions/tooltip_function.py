from dash import Input, Output, State, ctx, dcc, html, no_update
import dash_bootstrap_components as dbc
def tooltip_creation():
    tooltip = html.Div([
                # Page 1
                dbc.Tooltip(
                        "Die Corpus Heatmap zeigt die Topic Verteilung pro Interview. Dabei wird ein Durchschnittswert aus allen Chunks gebildet. Durch klicken auf ein Interview kann die Detailansicht ausgewählt werden",
                        target="Corpus_heatmap_page_1_header",
                        ),
                dbc.Tooltip(
                        "Das Balkendiagramm zeigt die Verteilung der Topics innerhalb des gesamten Corpus. Die einzelnen Farben repräsentieren die einzelnen Archive",
                        target="bargraph_page_1_header",
                        ),
                dbc.Tooltip(
                        "Hier können die einzelnen Archive für die Corpus Heatmap ausgewählt werden",
                        target="slct_archiv",
                        ),
                dbc.Tooltip(
                        "Der Z-Score berechnet eine Standartverteilung der Heatmap, um eine bessere Darstellung zu bekommen.",
                        target="switch_z_score_global_heatmap",
                        ),

                # Page 2
                dbc.Tooltip(
                    "In wievieln einzelnen Interviews sind Suchergebnisse gefgunden worden.",
                    target = "interview_results_header",
                ),
                dbc.Tooltip(
                    "Sortiert die Heatmap entweder nach dem Interviewnamen, oder den Werten von Topic 1 oder Topic 2",
                    target = "dropdown_sort",
                ), 
                dbc.Tooltip(
                    "Wählen sie ein Topic aus, indem sie die Nummer eintragen.",
                    target = "topic_cv",
                ),
                dbc.Tooltip(
                    "Wählen sie ein Gewicht aus, über dem das gesucht Topic 1 liegen soll. Der Wert muss unter 1 liegen.",
                    target = "topic_weight_cv",
                ),
                dbc.Tooltip(
                    "Wenn sie mindestens ein Topic und ein Gewicht ausgewählt haben, drücken sie auf diesen Button, um die Suche zu starten.",
                    target = "start_search_cv",
                ),
                dbc.Tooltip(
                    "Wählen sie ein zweites Topic aus, um nach einer Korrelation zwischen Topic 1 und 2 zu suchen. Vorher müssen sie die Korrelation über den Correlation Button auswählen.",
                    target = "topic_2_cv",
                ),
                dbc.Tooltip(
                    "Wählen sie ein Gewicht aus, über dem das gesucht Topic 2 liegen soll. Der Wert muss unter 1 liegen.",
                    target = "topic_2_weight_cv2",
                ),
                dbc.Tooltip(
                    "Wenn sie mindestens ein Topic und ein Gewicht ausgewählt haben, drücken sie auf diesen Button, um die Suche zu starten.",
                    target = "correlation_cv",
                ),


                ]
                    )
    return tooltip


def menu_tooltip(trigger):
    if trigger[0]["prop_id"] == "overview.n_clicks":
        tooltip= html.Div([
            dbc.Tooltip(
                """Die Übersicht bietet einen detaillierten Blick in die verschiedenen Ebenen der
                 Topic Modeling Ergebnisse. Durch die Auswahl von Interviews in der Heatmap können 
                  die Interviews für die Detailansicht ausgewählt werden.""",
                target = "menu_selection_info",
            ),         
        ])
        return tooltip
    if trigger[0]["prop_id"] == "chunk_analyzation.n_clicks":
        tooltip= html.Div([
            dbc.Tooltip(
                """Die Chunk Analyse bietet eine umfangreiche Möglichkeit, die Topic Verteilung 
                innerhalb der einzelnen Chunks zu analysieren. Darüber hinaus können auch Korrelationen
                mit anderen Topics untersucht werden.
                """,
                target = "menu_selection_info",
            ),         
        ])
        return tooltip
    if trigger[0]["prop_id"] == "bar_graph.n_clicks":
        tooltip= html.Div([
            dbc.Tooltip(
                "Das Balkendiagramm bietet eine grafische Darstellung der Topic Verteilung innerhalb des gesamten Korpus.",
                target = "menu_selection_info",
            ),         
        ])
        return tooltip
    if trigger[0]["prop_id"] == "heatmap.n_clicks":
        tooltip= html.Div([
            dbc.Tooltip(
                "Die Heatmap repräsentiert die Topic Verteilung über die einzelnen Interviews.",
                target = "menu_selection_info",
            ),         
        ])
        return tooltip
    if trigger[0]["prop_id"] == "interview_heatmap.n_clicks":
        tooltip= html.Div([
            dbc.Tooltip(
                "Die Interview Heatmap zeigt die Topic Verteilung innerhalb eines einzelnen Interviews.",
                target = "menu_selection_info",
            ),         
        ])
        return tooltip
    if trigger[0]["prop_id"] == "text_search.n_clicks":
        tooltip= html.Div([
            dbc.Tooltip(
                "Die Textsuche bietet die Möglichkeit, nach Chunks mit gewisser Topic Gewichtung zu suchen. Die Ergebnisse werden direkt in Textform präsentiert",
                target = "menu_selection_info",
            ),         
        ])
        return tooltip
    if trigger[0]["prop_id"] == "topic_words.n_clicks":
        tooltip= html.Div([
            dbc.Tooltip(
                "Mit der Topic Wörter Funktion können Sie die einzelnen Worte jedes Topics anschauen.",
                target = "menu_selection_info",
            ),         
        ])
        return tooltip


def menu_label_function(trigger):
    if trigger[0]["prop_id"] == "overview.n_clicks":
        menu_label = "Overview"
        return menu_label
    if trigger[0]["prop_id"] == "chunk_analyzation.n_clicks":
        menu_label = "Chunk Analyzation"
        return menu_label
    if trigger[0]["prop_id"] == "bar_graph.n_clicks":
        menu_label = "Bar Graph"
        return menu_label
    if trigger[0]["prop_id"] == "heatmap.n_clicks":
        menu_label = "Heatmap"
        return menu_label
    if trigger[0]["prop_id"] == "interview_heatmap.n_clicks":
        menu_label = "Interview Heatmap"
        return menu_label
    if trigger[0]["prop_id"] == "text_search.n_clicks":
        menu_label = "Chunk Suche"
        return menu_label
    if trigger[0]["prop_id"] == "topic_words.n_clicks":
        menu_label = "Topic Wörter"
        return menu_label 
