from dash import Input, Output, State, ctx, dcc, html, no_update
import dash_bootstrap_components as dbc
def tooltip_creation():
    tooltip = html.Div([
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
                ]
                    )
    return tooltip

