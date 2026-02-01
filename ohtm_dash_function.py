""" """

import base64

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, ctx, dcc, html, no_update
import copy
# import dash_mantine_components

from functions.dash_board_functions.dropdown_list import create_dropdown_list
from functions.graph_functions.bar_graph import bar_graph_corpus, bar_graph_cv_function
from functions.graph_functions.heat_maps import (
    heatmap_corpus,
    heatmap_interview_simple,
    chunk_heatmap,
)
from functions.print_functions.print_chunk_sents import (
    chunk_sent_drawing,
    chunk_sent_drawing_cv,
)
from dash.exceptions import PreventUpdate
from functions.print_functions.print_topic_search import print_topic_search_weight
from functions.print_functions.print_topics import print_all_topics, top_words
from functions.print_functions.print_sideboard_info import sideboard_info_function
from functions.print_functions.print_details_cv import print_details_cv_function
from functions.dash_board_functions.tooltip_function import (
    tooltip_creation,
    menu_label_function,
    menu_tooltip,
)
from functions.textfiles_functions.impressum_text_file import impressum_titel_text, impressum_text
from functions.textfiles_functions.glossar_text_file import glossar_titel_text, glossar_text
from functions.dash_board_functions.option_switch_sidebar import (
    option_switch_sidebar_function,
)

global top_dic
global tooltip_bool
global axis_titel_option
logo_image_filename = "dash_ohd_image.png"


def create_ohd_dash(
    ohtm_file, chronologie_analyse: bool = False, pop_up_window: bool = False,
    axis_titel_option: bool = False,
):
    def b64_image(logo_image_filename):
        with open(logo_image_filename, "rb") as f:
            image = f.read()
        return "data:image/png;base64," + base64.b64encode(image).decode("utf-8")

    if chronologie_analyse:
        from functions.graph_functions.chronologie_heatmap_function import (
            chronology_matrix,
        )
    sideboard_options = option_switch_sidebar_function(chronologie_analyse)

    app = dash.Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        suppress_callback_exceptions=True,
        prevent_initial_callbacks=True,
    )

    # styling the sidebar
    sidebar_style = {
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "14%",
        "hight": "100%",
        "padding": "2rem 1rem",
        "background-color": "#2B88AF",
    }

    # padding for the page content
    content_style = {
        "margin-left": "14%",
        "margin-right": "0,5%",
        "padding": "2rem 1rem",
        "margine": "auto",
    }

    sidebar = html.Div(
        [
            dbc.Container(
                [
                    # Tooltips
                    html.Div(id="tooltip_store"),
                    html.Div(id="tooltip_store_sidebar"),
                    # Stores for different Variables and States
                    dcc.Store(id="top_dic", data="", storage_type="session"),
                    dcc.Store(id="heat_dic", data={}, storage_type="session"),
                    dcc.Store(id="top_dic2", data={}, storage_type="session"),
                    dcc.Store(id="data_path", storage_type="session"),
                    dcc.Store(
                        id="heatmap_interview_topic_nr", data="", storage_type="session"
                    ),
                    dcc.Store(
                        id="heatmap_interview_detail_topic_nr",
                        data="",
                        storage_type="session",
                    ),
                    dcc.Store(id="bar_topic_nr", data="", storage_type="session"),
                    dcc.Store(
                        id="bar_detail_topic_nr", data="", storage_type="session"
                    ),
                    dcc.Store(
                        id="heatmap_corpus_topic_nr", data="", storage_type="session"
                    ),
                    dcc.Store(
                        id="heatmap_corpus_detail_topic_nr",
                        data="",
                        storage_type="session",
                    ),
                    dcc.Store(
                        id="chunk_number_frontpage", data="", storage_type="session"
                    ),
                    dcc.Store(
                        id="chunk_number_heatmap_interview",
                        data="",
                        storage_type="session",
                    ),
                    dcc.Store(
                        id="chunk_number_chunk_sent_draw",
                        data="",
                        storage_type="session",
                    ),
                    dcc.Store(
                        id="chunk_number_detail", data="", storage_type="session"
                    ),
                    dcc.Store(
                        id="interview_id_storage", data="", storage_type="session"
                    ),
                    dcc.Store(
                        id="interview_id_storage_detail",
                        data="",
                        storage_type="session",
                    ),
                    dcc.Store(
                        id="tc_indicator_detail", data="", storage_type="session"
                    ),
                    dcc.Store(id="tc_indicator", data="", storage_type="session"),
                    dcc.Store(
                        id="interview_heatmap_df", data="", storage_type="session"
                    ),
                    dcc.Store(
                        id="interview_heatmap_df_detail",
                        data="",
                        storage_type="session",
                    ),
                    dcc.Store(
                        id="heat_map_cv_topic_nr",
                        data="",
                        storage_type="session",
                    ),
                    dcc.Store(
                        id="bar_graph_cv_topic_nr",
                        data="",
                        storage_type="session",
                    ),
                    dcc.Store(
                        id="chunk_number_cv",
                        storage_type="session",
                    ),
                    html.Img(
                        src=b64_image(logo_image_filename), style={"max-width": "100%"}
                    ),
                    dbc.Row(
                        [],
                        style={
                            "height": "0.5vh",
                            "display": "flex",
                            "gap": "clamp(0.5em, 2vw, 2em)",
                        },
                    ),
                    dbc.Row(
                        html.Hr(),
                        style={"display": "flex", "gap": "clamp(0.5em, 2vw, 2em)"},
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.DropdownMenu(
                                        children=[
                                            dbc.DropdownMenuItem(
                                                "Overview",
                                                id="overview",
                                                href="/",
                                                style={"font-size": "0.8vw"},
                                            ),
                                            dbc.DropdownMenuItem(
                                                "Chunk Analyzation",
                                                id="chunk_analyzation",
                                                href="/page-6",
                                                style={"font-size": "0.8vw"},
                                            ),
                                            dbc.DropdownMenuItem(
                                                "Balkendiagram",
                                                id="bar_graph",
                                                href="/page-2",
                                                style={"font-size": "0.8vw"},
                                            ),
                                            dbc.DropdownMenuItem(
                                                "Heatmap",
                                                id="heatmap",
                                                href="/page-5",
                                                style={"font-size": "0.8vw"},
                                            ),
                                            dbc.DropdownMenuItem(
                                                "Interview Heatmap",
                                                id="interview_heatmap",
                                                href="/page-3",
                                                style={"font-size": "0.8vw"},
                                            ),
                                            dbc.DropdownMenuItem(
                                                "Text Search",
                                                id="text_search",
                                                href="/page-1",
                                                style={"font-size": "0.8vw"},
                                            ),
                                            dbc.DropdownMenuItem(
                                                "Topic Wörter",
                                                id="topic_words",
                                                href="/page-4",
                                                style={"font-size": "0.8vw"},
                                            ),
                                        ],
                                        label="Menu",
                                        color="dark",
                                        className="m-1",
                                        toggle_style={
                                            "font-size": "0.8vw"
                                        },  # PRÄSENTATION 1
                                        id="menu_selection",
                                        # menu_variant="dark",
                                    ),
                                ]
                            ),
                            dbc.Col(
                                [
                                    html.H5(
                                        [
                                            dbc.Badge(
                                                id="menu_selection_info",
                                                children="Overview",
                                                className="m-1",
                                                color="secondary",
                                                style={"font-size": "0.7vw"},
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                        ],
                        style={"display": "flex", "flexDirection": "column"},
                    ),
                    dbc.Row(
                        [],
                        style={
                            "height": "1vh",
                            "display": "flex",
                            "gap": "clamp(0.5em, 2vw, 2em)",
                        },
                    ),
                    dbc.Row(
                        html.Hr(),
                        style={"display": "flex", "gap": "clamp(0.5em, 2vw, 2em)"},
                    ),
                    dbc.Row(
                        [
                            html.H5(
                                dbc.Badge(
                                    id="topic_number_sidebar_1",
                                    children="Topic: ",
                                    color="dark",
                                    style={
                                        "width": "50%",
                                        "font-size": "0.7vw",  # PRÄSENTATION 1
                                    },
                                )
                            )
                        ],
                        style={"display": "flex"},
                    ),
                    dbc.Row(
                        [
                            html.H5(
                                dbc.Badge(
                                    id="topic_label_side_bar",
                                    children="",
                                    color="secondary",
                                    style={
                                        "font-size": "0.7vw",  # PRÄSENTATION 1
                                    },
                                )
                            )
                        ],
                        style={"display": "flex"},
                    ),
                    dbc.Row(
                        [
                            dbc.Input(
                                id="input",
                                placeholder="Topic Nummer eingeben",
                                type="number",
                                size="sm",
                                min=0,
                                max=100 - 1,
                                step=1,
                            ),
                        ]
                    ),
                    dbc.Row(html.Hr()),
                    dbc.Row(
                        [
                            html.Div(
                                [
                                    html.Br(),
                                    html.Br(),
                                    html.Br(),
                                    html.Br(),
                                    html.Br(),
                                    html.Br(),
                                    html.Br(),
                                    html.Br(),
                                    html.Br(),
                                ],
                                id="topics",
                                style={
                                    "height": "20%",
                                    "width": "95%",
                                    "padding": "1% 1%",
                                    "display": "block",
                                    "font-size": "0.8vw",  # PRÄSENTATION 1
                                    "background-color": "rgb(249,249,249)",
                                    "overflow": "auto",
                                },
                            )
                        ],
                        style={"display": "flex", "alignItems": "center"},
                    ),
                    html.Div(
                        [
                            html.Hr(),
                            dbc.Checklist(
                                options=sideboard_options,
                                value=[],
                                id="side_bar_menu_switch",
                                switch=True,
                                style={
                                    "width": "100%",
                                    "min-width": "150px",
                                    "font-size": "0.8vw",
                                    "display": "flex",
                                    "flex-direction": "column",
                                },
                            ),
                        ]
                    ),
                    # Informs the user, if Labels or clusters are missing
                    html.Div(
                        [
                            dbc.Toast(
                                header="Fehler",
                                id="warning",
                                is_open=False,
                                dismissable=True,
                                icon="danger",
                                style={
                                    "position": "fixed",
                                    "bottom": 40,  # Abstand von unten
                                    "left": 20,  # Abstand von links
                                    "width": 200,
                                    "zIndex": 9999,  # ganz nach vorne
                                },
                            )
                        ]
                    ),
                    html.Div(
                        [
                            html.Hr(),
                            html.P(
                                "Topic Model Info",
                                className="text-muted",
                                style={"font-size": "0.6vw", "display": "flex"},
                            ),
                            html.Div(
                                id="sidebar-info",
                                children="[]",
                                style={
                                    "whiteSpace": "pre-line",
                                    "font-size": "0.6vw",
                                    "display": "flex",
                                },
                            ),
                            html.Hr(),
                        ]
                    ),
                    html.Div(
                        [
                            dbc.Button(
                                "Impressum",
                                id="impressum_button",
                                color="light",
                                size="sm",
                                style={"font-size": "0.5vw"},
                            )
                        ],
                    ),
                    html.Div(
                        dbc.Offcanvas(
                            html.P(
                                impressum_text,
                                style={
                                    "whiteSpace": "pre-line",
                                    "font-size": "0.8vw",},
                            ),
                            id="offcanvas",
                            title=impressum_titel_text,
                            is_open=pop_up_window,
                            style={"width": "40vw"},
                        ),
                        id="impressum",
                    ),
                    html.Div(
                        [
                            dbc.Button(
                                "Glossar",
                                id="glossar_button",
                                color="light",
                                size="sm",
                                style={"font-size": "0.5vw"},
                            )
                        ],
                    ),
                    html.Div(
                        dbc.Offcanvas(
                            html.P(
                                glossar_text,
                                style={
                                    "whiteSpace": "pre-line",
                                    "font-size": "0.8vw",},
                            ),
                            id="offcanvas_glossar",
                            title=glossar_titel_text,
                            is_open=False,
                            style={"width": "40vw"},
                        ),
                        id="glossar",
                    ),
                ],
                fluid=True,
            )
        ],
        style=sidebar_style,
    )
    content = html.Div(id="page-content", children=[], style=content_style)

    app.layout = html.Div(
        [dcc.Location(id="url"), sidebar, content],
        style={
            "height": "100vh",
            "width": "100vw",
            "display": "flex",
            "flexDirection": "column",
        },
    )

    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname == "/":
            return [
                dbc.Container(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H2(
                                            [
                                                dbc.Badge(
                                                    id="Corpus_heatmap_page_1_header",
                                                    children=["Corpus Heatmap"],
                                                    color="dark",
                                                    style={
                                                        "font-size": "0.8vw",
                                                        "display": "flex",
                                                    },
                                                )
                                            ],
                                            style={
                                                "display": "flex",
                                                "alignItems": "center",
                                                "justifyContent": "center",
                                            },
                                        ),
                                    ],
                                    width=2,
                                ),
                                dbc.Col(
                                    [
                                        dcc.Dropdown(
                                            id="slct_archiv",
                                            options=[],
                                            value="all",
                                            multi=False,
                                            style={
                                                "height": "95%",
                                                "width": "100%",
                                                "min-width": "200px",
                                                "font-size": "0.8vw",
                                                "display": "flex",
                                            },
                                            placeholder="Corpus",
                                        )
                                    ],
                                    width=2,
                                    style={
                                        "display": "flex",
                                        "alignItems": "center",
                                        "justifyContent": "center",
                                    },
                                ),
                                dbc.Col(
                                    [
                                        dbc.Checklist(
                                            options=[
                                                {"label": "Z Score", "value": "z_score"}
                                            ],
                                            value=[],
                                            id="switch_z_score_global_heatmap",
                                            switch=True,
                                            style={
                                                "width": "100%",
                                                "min-width": "150px",
                                                "font-size": "0.8vw",
                                                "display": "flex",
                                            },
                                        )
                                    ],
                                    width=1,
                                ),
                                dbc.Col([], width=3),
                                dbc.Col(
                                    [
                                        html.H2(
                                            [
                                                dbc.Badge(
                                                    id="bargraph_page_1_header",
                                                    children=["Corpus Bargraph"],
                                                    color="dark",
                                                    style={
                                                        "font-size": "0.8vw",
                                                        "display": "flex",
                                                    },
                                                )
                                            ],
                                            style={"display": "flex"},
                                            className="text-center",
                                        ),
                                    ],
                                    width=2,
                                ),
                                dbc.Col([], width=2),
                            ],
                            style={"height": "5vh"},
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dcc.Graph(
                                            id="heat_map",
                                            figure={},
                                            config={"responsive": True},
                                            style={
                                                "height": "100%",
                                                "width": "100%",
                                                "display": "flex",
                                            },
                                        )
                                    ],
                                    width=7,
                                    style={"display": "flex"},
                                ),
                                dbc.Col(
                                    [
                                        dcc.Graph(
                                            id="bar",
                                            figure={},
                                            config={"responsive": True},
                                            style={
                                                "height": "100%",
                                                "width": "100%",
                                                "display": "flex",
                                            },
                                        )
                                    ],
                                    width=5,
                                    style={"display": "flex"},
                                ),
                            ],
                            style={"height": "40vh"},
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H2(
                                            [
                                                dbc.Badge(
                                                    id="interview_titel",
                                                    children=["Interview"],
                                                    color="dark",
                                                    style={
                                                        "font-size": "0.8vw",
                                                        "display": "flex",
                                                    },
                                                )
                                            ],
                                            className="text-center",
                                        ),
                                    ],
                                    width=2,
                                    style={
                                        "display": "flex",
                                        "alignItems": "center",
                                        "justifyContent": "center",
                                    },
                                ),
                                # dbc.Col(
                                #     [
                                #     dcc.Input(
                                #     id = "range",
                                #     type = "range",
                                #     min = 0,
                                #     max = 1,
                                # )], width = 1),
                                dbc.Col(
                                    [
                                        dbc.Checklist(
                                            options=[
                                                {"label": "Marker", "value": "marker"},
                                            ],
                                            value=[],
                                            id="switch_chronology_filter",
                                            switch=True,
                                            inline=True,
                                            style={
                                                "font-size": "0.7vw",
                                                "display": "flex",
                                            },
                                        ),
                                    ],
                                    width=2,
                                    style={"display": "flex"},
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            dbc.Input(
                                                id="interview_manual_id",
                                                placeholder="Interview",
                                                type="text",
                                                style={
                                                    "width": "100%",
                                                    "font-size": "0.8vw",
                                                    "display": "flex",
                                                },
                                            )
                                        ),
                                    ],
                                    width=1,
                                    style={"display": "flex"},
                                ),
                                dbc.Col([], width=2),
                                dbc.Col(
                                    [
                                        html.H2(
                                            [
                                                dbc.Button(
                                                    "<",
                                                    id="-_button_frontpage",
                                                    color="dark",
                                                    size="sm",
                                                    style={
                                                        "font-size": "0.6vw",
                                                        "alignItems": "center",
                                                        "justifyContent": "center",
                                                    },
                                                ),
                                                dbc.Badge(
                                                    "Chunk",
                                                    id="sent_titel",
                                                    color="dark",
                                                    style={
                                                        "font-size": "0.6vw",
                                                        "alignItems": "center",
                                                        "justifyContent": "center",
                                                        "margin": "0 auto",
                                                    },
                                                ),
                                                dbc.Button(
                                                    ">",
                                                    id="+_button_frontpage",
                                                    color="dark",
                                                    size="sm",
                                                    style={
                                                        "font-size": "0.6vw",
                                                        "justifyContent": "center",
                                                    },
                                                ),
                                            ],
                                            style={"display": "flex"},
                                            className="text-center",
                                        ),
                                    ],
                                    width=2,
                                    style={"display": "flex"},
                                ),
                                dbc.Col([], width=2),
                            ],
                            style={"height": "5vh"},
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dcc.Graph(
                                            id="heat_map_interview",
                                            figure={},
                                            style={"height": "100%", "width": "100%"},
                                            config={"responsive": True},
                                        )
                                    ],
                                    width=6,
                                    style={"display": "flex"},
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            id="textarea",
                                            style={
                                                "whiteSpace": "pre-line",
                                                "display": "inline-block",
                                                "height": "45vh",
                                                "display": "block",
                                                "font-size": "1vm",
                                                "background-color": "rgb(249,249,249)",
                                                "overflow": "auto",
                                            },
                                        ),
                                    ],
                                    width=6,
                                    style={"display": "flex"},
                                ),
                            ],
                            style={"height": "35vh"},
                        ),
                    ],
                    fluid=True,
                ),
            ]
        elif pathname == "/page-1":
            return [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        dbc.InputGroup(
                                            [
                                                dbc.InputGroupText("Topic"),
                                                dbc.Input(
                                                    id="topic_print",
                                                    placeholder="Topic",
                                                    type="number",
                                                ),
                                            ],
                                            className="mb-3",
                                        ),
                                        dbc.InputGroup(
                                            [
                                                dbc.InputGroupText("Weight"),
                                                dbc.Input(
                                                    id="weight_print",
                                                    placeholder="Weight",
                                                    type="number",
                                                ),
                                            ],
                                            className="mb-3",
                                        ),
                                    ]
                                ),
                            ],
                            width=2,
                        ),
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        dbc.InputGroup(
                                            [
                                                dbc.InputGroupText("Interview ID"),
                                                dbc.Input(
                                                    id="interview_id_search",
                                                    placeholder="Interview ID",
                                                    type="text",
                                                ),
                                            ],
                                            className="mb-3",
                                        ),
                                        dbc.InputGroup(
                                            [
                                                dbc.Select(
                                                    options=[
                                                        {
                                                            "label": "Korpus Search",
                                                            "value": "1",
                                                        },
                                                        {
                                                            "label": "Interview Search",
                                                            "value": "2",
                                                        },
                                                        # {"label": "Correlation Search Vertical", "value": 3},
                                                        # {"label": "Correlation Search Horizontal", "value": 4},
                                                    ],
                                                    id="text_search_options",
                                                    value="1",
                                                )
                                            ]
                                        ),
                                    ]
                                ),
                            ],
                            width=2,
                        ),
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        dbc.InputGroup(
                                            [
                                                dbc.Button(
                                                    "Search",
                                                    id="enter_print",
                                                    color="dark",
                                                )
                                            ],
                                            className="mb-3",
                                        ),
                                    ]
                                ),
                            ],
                            width=2,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col([html.Div(id="table-container")], width=8),
                    ]
                ),
            ]

        elif pathname == "/page-2":
            return [
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Graph(
                                id="bar2",
                                figure={},
                                style={"height": "100%", "width": "100%"},
                                config={"responsive": True},
                            )
                        )
                    ],
                    style={"height": "60vh"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Input(
                                    id="input1",
                                    placeholder="Topic Nummer eingeben",
                                    type="number",
                                    min=0,
                                    max=100 - 1,
                                    step=1,
                                    style={
                                        "width": "70%",
                                        "min-width": "100px",
                                        "font-size": "0.8vw",
                                        "display": "flex",
                                    },
                                )
                            ]
                        ),
                        dbc.Col(
                            [
                                dbc.Input(
                                    id="input2",
                                    placeholder="Topic Nummer eingeben",
                                    type="number",
                                    min=0,
                                    max=100 - 1,
                                    step=1,
                                    style={
                                        "width": "70%",
                                        "min-width": "100px",
                                        "font-size": "0.8vw",
                                        "display": "flex",
                                    },
                                )
                            ]
                        ),
                        dbc.Col(
                            [
                                dbc.Input(
                                    id="input3",
                                    placeholder="Topic Nummer eingeben",
                                    type="number",
                                    min=0,
                                    max=100 - 1,
                                    step=1,
                                    style={
                                        "width": "70%",
                                        "min-width": "100px",
                                        "font-size": "0.8vw",
                                        "display": "flex",
                                    },
                                )
                            ]
                        ),
                        dbc.Row([], style={"height": "1vh"}),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            id="topics1",
                                            style={
                                                "height": "100%",
                                                "width": "95%",
                                                "padding": "5% 5%",
                                                "display": "block",
                                                "font-size": "0.8vw",  # PRÄSENTATION 1
                                                "background-color": "rgb(249,249,249)",
                                                "overflow": "off",
                                            },
                                        )
                                    ],
                                    style={"display": "flex", "alignItems": "center"},
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            id="topics2",
                                            style={
                                                "height": "100%",
                                                "width": "95%",
                                                "padding": "5% 5%",
                                                "display": "block",
                                                "font-size": "0.8vw",  # PRÄSENTATION 1
                                                "background-color": "rgb(249,249,249)",
                                                "overflow": "off",
                                            },
                                        )
                                    ],
                                    style={"display": "flex", "alignItems": "center"},
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            id="topics3",
                                            style={
                                                "height": "100%",
                                                "width": "95%",
                                                "padding": "5% 5%",
                                                "display": "block",
                                                "font-size": "0.8vw",  # PRÄSENTATION 1
                                                "background-color": "rgb(249,249,249)",
                                                "overflow": "off",
                                            },
                                        )
                                    ],
                                    style={"display": "flex", "alignItems": "center"},
                                ),
                            ]
                        ),
                    ]
                ),
            ]

        elif pathname == "/page-3":
            return [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    dbc.Input(
                                        id="interview_manual_id_detail",
                                        placeholder="Interview",
                                        type="wod",
                                    )
                                ),
                            ],
                            width=1,
                        ),
                        dbc.Col(
                            [
                                dbc.Checklist(
                                    options=[
                                        {"label": "Z Score", "value": "z_score"},
                                        {"label": "Marker", "value": "marker"},
                                    ],
                                    value=[],
                                    id="switch_chronology_filter_detail",
                                    switch=True,
                                    inline=True,
                                ),
                            ],
                            width=4,
                        ),
                        dbc.Col(
                            [
                                dbc.Checklist(
                                    options=[
                                        {
                                            "label": "Topic Filter",
                                            "value": "topic_filter",
                                        },
                                    ],
                                    value=[],
                                    id="topic_filter_switch_detail",
                                    switch=True,
                                    inline=True,
                                    style={"display": "none"},
                                ),
                            ],
                            width=2,
                        ),
                        dbc.Col(
                            [
                                html.Div(
                                    dbc.Input(
                                        placeholder="outlier_threshold",
                                        type="floag",
                                        id="ihc_outlier_threshold_value",
                                    ),
                                    id="ihc_outlier_threshold",
                                    style={"display": "none"},
                                ),
                            ],
                            width=1,
                        ),
                        dbc.Col(
                            [
                                html.Div(
                                    dbc.Input(
                                        id="ihc_threshold_top_filter_value",
                                        placeholder="threshold_top_filter",
                                        type="float",
                                    ),
                                    id="ihc_threshold_top_filter",
                                    style={"display": "none"},
                                ),
                            ],
                            width=1,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        html.H5(
                            [dbc.Badge(id="interview_title_detail", color="dark")],
                            className="text-center",
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dcc.Graph(id="heat_map_interview_detail", figure={}),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col([], width=5),
                        dbc.Col(
                            [
                                dbc.Button(
                                    "<", id="-_button_detail", color="dark", size="sm"
                                ),
                                dbc.Badge(
                                    "chunk",
                                    id="sent_title_detail",
                                    color="dark",
                                    className="text-center",
                                ),
                                dbc.Button(
                                    ">", id="+_button_detail", color="dark", size="sm"
                                ),
                            ],
                            width=2,
                        ),
                        dbc.Col([], width=5),
                    ]
                ),
                dbc.Row(html.Hr()),
                dbc.Row(
                    [
                        html.Div(
                            id="textarea_detail",
                            style={
                                "whiteSpace": "pre-line",
                                "height": "400px",
                                "display": "block",
                                "font-size": "15px",
                                "background-color": "rgb(249,249,249)",
                                "overflow": "auto",
                            },
                        ),
                    ]
                ),
            ]
        elif pathname == "/page-4":
            return [
                dbc.Col(
                    [
                        html.Div(
                            dbc.Input(
                                id="word_number",
                                placeholder="Anzahl Wörter pro Topic",
                                type="number",
                            )
                        ),
                        dbc.Button(
                            "print", id="enter_print_topics", color="dark", size="sm"
                        ),
                    ],
                    width=2,
                ),
                dbc.Col([html.Div(id="topic_table")], width=8),
            ]
        elif pathname == "/page-5":
            return [
                dbc.Container(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dcc.Dropdown(
                                            id="slct_archiv_heat_map_corpus_detail",
                                            options=[],
                                            value="all",
                                            multi=False,
                                            style={
                                                "width": "80%",
                                                "min-width": "150px",
                                                "font-size": "0.8vw",
                                            },
                                            placeholder="Corpus",
                                        ),
                                    ],
                                    width=3,
                                    style={"display": "flex", "alignItems": "center"},
                                ),
                                dbc.Col(
                                    [
                                        dbc.Checklist(
                                            options=[
                                                {
                                                    "label": "Z Score",
                                                    "value": "z_score",
                                                },
                                                {
                                                    "label": "Filter",
                                                    "value": "topic_filter",
                                                },
                                            ],
                                            value=[],
                                            id="z_score_corpus_heatmap_detail",
                                            switch=True,
                                            style={
                                                "width": "100%",
                                                "min-width": "150px",
                                                "font-size": "0.8vw",
                                                "display": "flex",
                                            },
                                        ),
                                    ],
                                    width=3,
                                    style={"display": "flex", "alignItems": "center"},
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            dbc.Input(
                                                id="corpus_heatmap_detail_topic",
                                                placeholder="Topic",
                                                type="int",
                                                style={
                                                    "width": "70%",
                                                    "min-width": "100px",
                                                    "font-size": "0.8vw",
                                                    "display": "flex",
                                                },
                                            )
                                        ),
                                    ],
                                    width=2,
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            dbc.Input(
                                                id="corpus_heatmap_detail_threshold",
                                                placeholder="Threshold",
                                                type="int",
                                                style={
                                                    "width": "70%",
                                                    "min-width": "100px",
                                                    "font-size": "0.8vw",
                                                    "display": "flex",
                                                },
                                            )
                                        ),
                                    ],
                                    width=2,
                                ),
                            ],
                            style={"display": "flex", "alignItems": "left"},
                        ),
                        dbc.Row(
                            [
                                dcc.Graph(
                                    id="heat_map_corpus_detail",
                                    figure={},
                                    style={"height": "100%", "width": "100%"},
                                    config={"responsive": True},
                                )
                            ],
                            style={"height": "80vh"},
                        ),
                        dbc.Row(),
                    ],
                    fluid=True,
                )
            ]
        elif pathname == "/page-6":
            return [
                dbc.Container(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                dbc.InputGroup(
                                                    [
                                                        dbc.InputGroupText("Topic"),
                                                        dbc.Input(
                                                            id="topic_cv",
                                                            placeholder="Topic",
                                                            type="number",
                                                        ),
                                                    ],
                                                    className="mb-3",
                                                    size="sm",
                                                ),
                                                dbc.InputGroup(
                                                    [
                                                        dbc.InputGroupText("Weight"),
                                                        dbc.Input(
                                                            id="topic_weight_cv",
                                                            placeholder="Weight",
                                                            type="number",
                                                        ),
                                                    ],
                                                    className="mb-3",
                                                    size="sm",
                                                ),
                                                dbc.InputGroup(
                                                    [
                                                        dbc.Button(
                                                            "Search",
                                                            id="start_search_cv",
                                                            color="dark",
                                                        )
                                                    ],
                                                    className="mb-3",
                                                    size="sm",
                                                ),
                                            ]
                                        ),
                                    ],
                                    width=2,
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                dbc.InputGroup(
                                                    [
                                                        dbc.InputGroupText("Topic 2"),
                                                        dbc.Input(
                                                            id="topic_2_cv",
                                                            placeholder="Topic",
                                                            type="number",
                                                        ),
                                                    ],
                                                    className="mb-3",
                                                    size="sm",
                                                ),
                                                dbc.InputGroup(
                                                    [
                                                        dbc.InputGroupText("Weight 2"),
                                                        dbc.Input(
                                                            id="topic_2_weight_cv2",
                                                            placeholder="Weight",
                                                            type="number",
                                                        ),
                                                    ],
                                                    className="mb-3",
                                                    size="sm",
                                                ),
                                                html.H5(
                                                    [
                                                        dbc.Badge(
                                                            id="cv_results",
                                                            children=["0 Chunks"],
                                                            color="dark",
                                                            style={
                                                                "font-size": "0.7vw",
                                                                "display": "flex",
                                                            },
                                                        )
                                                    ],
                                                    className="text-center",
                                                ),
                                            ]
                                        ),
                                    ],
                                    width=2,
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                dbc.DropdownMenu(
                                                    id="dropdown_sort",
                                                    label="Sort Filter",
                                                    color="secondary",
                                                    class_name="mb-3",
                                                    size="sm",
                                                    children=[
                                                        dbc.DropdownMenuItem(
                                                            "Interview",
                                                            id="sort_interview_cv",
                                                        ),
                                                        dbc.DropdownMenuItem(
                                                            "Topic 1",
                                                            id="sort_topic_1_cv",
                                                        ),
                                                        dbc.DropdownMenuItem(
                                                            "Topic 2",
                                                            id="sort_topic_2_cv",
                                                        ),
                                                    ],
                                                ),
                                                dcc.Dropdown(
                                                    id="slct_archiv",
                                                    options=[],
                                                    value="all",
                                                    multi=False,
                                                    style={},
                                                    placeholder="Corpus",
                                                ),
                                            ]
                                        ),
                                    ],
                                    width=2,
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                dbc.Checklist(
                                                    options=[
                                                        {
                                                            "label": "Correlation",
                                                            "value": "correlation_cv",
                                                        }
                                                    ],
                                                    value=[],
                                                    id="correlation_cv",
                                                    switch=True,
                                                    style={
                                                        "width": "100%",
                                                        "min-width": "150px",
                                                        "font-size": "0.8vw",
                                                        "display": "flex",
                                                    },
                                                ),
                                            ]
                                        ),
                                    ],
                                    width=1,
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            dbc.Badge(
                                                id="interview_results_header",
                                                children=["Interview Results"],
                                            )
                                        ),
                                        html.Div(
                                            id="topic_info_cv",
                                            style={
                                                # "whiteSpace": "pre-line",
                                                "display": "inline-block",
                                                "height": "15vh",
                                                "display": "block",
                                                "font-size": "0.5vm",
                                                "background-color": "rgb(249,249,249)",
                                                "overflow": "auto",
                                                "display": "flex",
                                            },
                                        ),
                                    ],
                                    width=4,
                                    style={
                                        "display": "flex",
                                        "flexDirection": "column",
                                    },
                                ),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dcc.Graph(
                                            id="heat_map_cv",
                                            figure={},
                                            config={"responsive": True},
                                            style={
                                                "height": "100%",
                                                "width": "100%",
                                                "display": "flex",
                                            },
                                        )
                                    ],
                                    width=7,
                                    style={"display": "flex"},
                                ),
                                dbc.Col(
                                    [
                                        dcc.Graph(
                                            id="bar_cv",
                                            figure={},
                                            config={"responsive": True},
                                            style={
                                                "height": "100%",
                                                "width": "100%",
                                                "display": "flex",
                                            },
                                        )
                                    ],
                                    width=5,
                                    style={"display": "flex"},
                                ),
                            ],
                            style={"height": "40vh"},
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [],
                                    width=2,
                                    style={"display": "flex"},
                                ),
                                dbc.Col(
                                    [
                                        dbc.InputGroup(
                                            [
                                                dbc.Button(
                                                    "<",
                                                    id="-_button_cv",
                                                    color="dark",
                                                    style={
                                                        "font-size": "0.7vw",
                                                        "display": "flex",
                                                    },
                                                ),
                                            ],
                                            className="mb-3",
                                            size="sm",
                                        ),
                                        html.H5(
                                            [
                                                dbc.Badge(
                                                    id="interview_titel_cv",
                                                    children=["Interview ID - Chunk:"],
                                                    color="dark",
                                                    style={
                                                        "font-size": "0.8vw",
                                                        "display": "flex",
                                                    },
                                                )
                                            ],
                                            className="text-center",
                                        ),
                                        dbc.InputGroup(
                                            [
                                                dbc.Button(
                                                    ">",
                                                    id="+_button_cv",
                                                    color="dark",
                                                    style={
                                                        "font-size": "0.7vw",
                                                        "display": "flex",
                                                    },
                                                ),
                                            ],
                                            className="mb-3",
                                            size="sm",
                                        ),
                                    ],
                                    width=2,
                                    style={"display": "flex"},
                                ),
                                dbc.Col(
                                    [],
                                    width=2,
                                    style={"display": "flex"},
                                ),
                                dbc.Col(
                                    [
                                        dbc.Badge(
                                            id="chunk_topic_info",
                                            children=["Chunk Topic Verteilung"],
                                            style={
                                                "font-size": "0.7vw",
                                                "display": "flex",
                                            },
                                        ),
                                    ],
                                    width=2,
                                ),
                                dbc.Col([], width=1),
                                dbc.Col(
                                    [
                                        dbc.Badge(
                                            id="chunk_topic_info_all",
                                            children=["Top 5 Topics"],
                                            style={
                                                "font-size": "0.7vw",
                                                "display": "flex",
                                            },
                                        ),
                                    ],
                                    width=2,
                                ),
                            ],
                            style={"height": "5vh"},
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            id="textarea_cv",
                                            style={
                                                "whiteSpace": "pre-line",
                                                "display": "inline-block",
                                                "height": "45vh",
                                                "display": "block",
                                                "font-size": "1vm",
                                                "background-color": "rgb(249,249,249)",
                                                "overflow": "auto",
                                            },
                                        ),
                                    ],
                                    width=6,
                                    style={"display": "flex"},
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            id="detail_info_cv_chunk",
                                            style={
                                                "whiteSpace": "pre-line",
                                                "display": "inline-block",
                                                "height": "45vh",
                                                "width": "100%",
                                                "display": "block",
                                                "font-size": "0.6vm",
                                                "background-color": "rgb(249,249,249)",
                                                "overflow": "auto",
                                            },
                                        ),
                                    ],
                                    width=3,
                                    style={"display": "flex"},
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            id="detail_info_cv",
                                            style={
                                                "whiteSpace": "pre-line",
                                                "display": "inline-block",
                                                "height": "45vh",
                                                "width": "100%",
                                                "display": "block",
                                                "font-size": "0.6vm",
                                                "background-color": "rgb(249,249,249)",
                                                "overflow": "auto",
                                            },
                                        ),
                                    ],
                                    width=3,
                                    style={"display": "flex"},
                                ),
                            ],
                            style={"height": "40vh"},
                        ),
                    ],
                    fluid=True,
                )
            ]

        # If the user tries to reach a different page, return a 404 message
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-dark"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )

    # Tooltip for the Menue Selection
    @app.callback(
        Output("tooltip_store_sidebar", "children"),
        Input("side_bar_menu_switch", "value"),
        Input("overview", "n_clicks"),
        Input("chunk_analyzation", "n_clicks"),
        Input("bar_graph", "n_clicks"),
        Input("heatmap", "n_clicks"),
        Input("interview_heatmap", "n_clicks"),
        Input("text_search", "n_clicks"),
        Input("topic_words", "n_clicks"),
        prevent_inital_call=True,
    )
    def set_tooltip_for_menu(switch, m1, m2, m3, m4, m5, m6, m7):
        if "tooltip_on" in switch:
            tooltip = menu_tooltip(ctx.triggered)
            return tooltip
        else:
            return []

    # Menu Label for the Menue Selection
    @app.callback(
        Output("menu_selection_info", "children"),
        Input("url", "pathname"),
        prevent_inital_call=False,
    )
    def set_menu_label(pathname):
        menu_label = menu_label_function(pathname)
        return menu_label

    @app.callback(
        Output("warning", "is_open"),
        Output("warning", "children"),
        Input("side_bar_menu_switch", "value"),
    )
    def label_test(options):
        if "topic_labels_on" in options:
            try:
                if ohtm_file["settings"]["labeling_options"]["labeling"] == False:
                    return (
                        True,
                        "This file has no labels. To add labels, see the documentation",
                    )
            except KeyError:
                return (
                    True,
                    "This file has no labels. To add labels, see the documentation",
                )
        elif "topic_cluster_on" in options:
            try:
                if ohtm_file["settings"]["labeling_options"]["clustering"] == False:
                    return (
                        True,
                        "This file has no clusters. To add clusters, see the documentation",
                    )
            except KeyError:
                return (
                    True,
                    "This file has no clusters. To add clusters, see the documentation",
                )
        else:
            return False, "no warning"

    # Page 1

    # Dropboxmenue for corpus heatmap page 1
    @app.callback(
        Output("slct_archiv", "options"),
        Output("slct_archiv", "value"),
        Input("top_dic", "n"),
        prevent_initial_call=False,
    )
    def create_dropdown_list_dash(data):
        drop_down_menu = create_dropdown_list(ohtm_file)
        return drop_down_menu, "all"

    # Bargraph on page 1
    @app.callback(
        Output(component_id="bar", component_property="figure"),
        Input("top_dic", "data"),
        Input("side_bar_menu_switch", "value"),
        prevent_initial_call=False,
    )
    def bar_map(data, options_list):
        fig = bar_graph_corpus(
            ohtm_file, show_fig=False, return_fig=True, options=options_list,
            axis_titel_option=axis_titel_option,
        )
        return fig

    # Corpusheatmap page 1
    @app.callback(
        Output(component_id="heat_map", component_property="figure"),
        Input("slct_archiv", "value"),
        Input("switch_z_score_global_heatmap", "value"),
        Input("side_bar_menu_switch", "value"),
    )
    def update_graph(value, z_score_global, options):
        fig = heatmap_corpus(
            ohtm_file,
            option_selected=str(value),
            z_score_global=z_score_global,
            show_fig=False,
            return_fig=True,
            options=options,
            axis_titel_option=axis_titel_option,
        )
        return fig

    # Interviewheatmap page 1
    @app.callback(
        Output(component_id="heat_map_interview", component_property="figure"),
        Output("interview_titel", "children"),
        Output("interview_id_storage", "data"),
        Output("chunk_number_heatmap_interview", "data"),
        Output("tc_indicator", "data"),
        Output("interview_heatmap_df", "data"),
        Input("heat_map", "clickData"),
        Input("switch_chronology_filter", "value"),
        Input("interview_manual_id", "value"),
        Input("heat_map_interview", "clickData"),
        Input("chunk_number_frontpage", "data"),
        Input("side_bar_menu_switch", "value"),
    )
    def interview_heat_map_dash(
        click_data,
        heatmap_filter,
        interview_manual_id,
        click_data_2,
        chunk_number_storage,
        option_list,
    ):
        if chronologie_analyse and "ihc" in option_list:
            chronologie_heatmap = chronology_matrix(
                data=ohtm_file,
                click_data=click_data,
                click_data_2=click_data_2,
                ctx_triggered=ctx.triggered,
                interview_manual_id=interview_manual_id,
                heatmap_filter=heatmap_filter,
                chunk_number_storage=chunk_number_storage,
                options=option_list,
                axis_titel_option=axis_titel_option,
            )

            if chronologie_heatmap is not None:
                fig = chronologie_heatmap[0]
                title = chronologie_heatmap[1]
                interview_id = chronologie_heatmap[2]
                chunk_number = chronologie_heatmap[3]
                tc_indicator = chronologie_heatmap[4]
                df_heatmap_interview = chronologie_heatmap[5]

                return (
                    fig,
                    title,
                    interview_id,
                    chunk_number,
                    tc_indicator,
                    df_heatmap_interview,
                )
            else:
                return no_update, no_update, no_update, no_update, no_update, no_update

        else:
            interview_heatmap = heatmap_interview_simple(
                ohtm_file=ohtm_file,
                click_data=click_data,
                click_data_2=click_data_2,
                ctx_triggered=ctx.triggered,
                chunk_number_storage=chunk_number_storage,
                heatmap_filter=heatmap_filter,
                interview_manual_id=interview_manual_id,
                options=option_list,
                axis_titel_option=axis_titel_option,
            )
            fig = interview_heatmap[0]
            title = interview_heatmap[1]
            interview_id = interview_heatmap[2]
            chunk_number = interview_heatmap[3]
            tc_indicator = interview_heatmap[4]
            df_heatmap_interview = interview_heatmap[5]
            return (
                fig,
                title,
                interview_id,
                chunk_number,
                tc_indicator,
                df_heatmap_interview,
            )

    # prints the raw sentences of the selected chunk into the field page 1
    @app.callback(
        Output(component_id="textarea", component_property="children"),
        Output("sent_titel", "children"),
        Output("chunk_number_chunk_sent_draw", "data"),
        Input("heat_map_interview", "clickData"),
        Input("-_button_frontpage", "n_clicks"),
        Input("+_button_frontpage", "n_clicks"),
        State("chunk_number_frontpage", "data"),
        State("interview_id_storage", "data"),
        State("tc_indicator", "data"),
        State("interview_heatmap_df", "data"),
        prevent_initial_call=True,
    )
    def sent_drawing_dash(
        click_data,
        input_before,
        input_next,
        chunk_number,
        interview_id,
        tc_indicator,
        interview_heatmap_df,
    ):
        if ctx.triggered[0]["value"] is None:
            if ctx.triggered[1]["value"] is None:
                if ctx.triggered[2]["value"] is None:
                    return no_update, no_update, no_update
        else:
            sent = chunk_sent_drawing(
                ohtm_file=ohtm_file,
                click_data_input=click_data,
                chunk_number=chunk_number,
                interview_id=interview_id,
                chronology_df=interview_heatmap_df,
                tc_indicator=tc_indicator,
            )

            chunk_sent = sent[0]
            sent_id = sent[1]
            chunk_id = sent[2]
            return chunk_sent, sent_id, chunk_id

    # Update Chunk_number_frontpate storage out of heatmap_interview and print_chunk_sentences:
    @app.callback(
        Output("chunk_number_frontpage", "data"),
        Input("chunk_number_chunk_sent_draw", "data"),
        Input("chunk_number_heatmap_interview", "data"),
    )
    def bar_map2(chunk_nr_print, chunk_number_heat):
        if ctx.triggered_id == "chunk_number_chunk_sent_draw":
            chunk_number = chunk_nr_print
            return chunk_number
        if ctx.triggered_id == "chunk_number_heatmap_interview":
            chunk_number = chunk_number_heat
            return chunk_number

    # Page 2
    # text search inside the chunks
    @app.callback(
        Output("table-container", "children"),
        Input("weight_print", "value"),
        Input("enter_print", "n_clicks"),
        Input("interview_id_search", "value"),
        Input("text_search_options", "value"),
        Input("topic_print", "value"),
        Input("side_bar_menu_switch", "value"),
    )
    def text_search_detail(
        weight_print,
        n_clicks,
        interview_id,
        text_search_options,
        topic_print,
        option_list,
    ):
        search_results = print_topic_search_weight(
            ohtm_file=ohtm_file,
            topic_print=topic_print,
            weight_print=weight_print,
            interview_id=interview_id,
            text_search_options=text_search_options,
            options=option_list,
        )
        return search_results

    # Page 3
    # bargraph on page 3
    @app.callback(
        Output(component_id="bar2", component_property="figure"),
        Input("top_dic2", "data"),
        Input("side_bar_menu_switch", "value"),
        prevent_initial_call=False,
    )
    def bar_map2(data, option_list):
        fig = bar_graph_corpus(
            ohtm_file, show_fig=False, return_fig=True, options=option_list, 
            axis_titel_option=axis_titel_option,
        )
        return fig

    # Print the topics on the single_bar_side page 3
    @app.callback(
        Output("topics1", "children"),
        Input("input1", "value"),
        prevent_initial_call=True,
    )
    def df_input(value):
        entry = top_words(value, ohtm_file)
        return entry

    @app.callback(
        Output("topics2", "children"),
        Input("input2", "value"),
        prevent_initial_call=True,
    )
    def df_input(value):
        entry = top_words(value, ohtm_file)
        return entry

    @app.callback(
        Output("topics3", "children"),
        Input("input3", "value"),
        prevent_initial_call=True,
    )
    def df_input(value):
        entry = top_words(value, ohtm_file)
        return entry

    # Page 4
    # Deatil Interview Heatmap page 4
    @app.callback(
        Output("ihc_outlier_threshold", "style"),
        Output("ihc_threshold_top_filter", "style"),
        Output("topic_filter_switch_detail", "style"),
        Input("side_bar_menu_switch", "value"),
    )
    def topic_filter_input_regulator(value):
        if chronologie_analyse == True:
            if "ihc" in value:
                return {"display": "block"}, {"display": "block"}, {"display": "block"}
            else:
                return {"display": "none"}, {"display": "none"}, {"display": "none"}
        if chronologie_analyse == False:
            return {"display": "none"}, {"display": "none"}, {"display": "none"}

    @app.callback(
        Output(component_id="heat_map_interview_detail", component_property="figure"),
        Output("interview_title_detail", "children"),
        Output("interview_id_storage_detail", "data"),
        Output("tc_indicator_detail", "data"),
        Output("interview_heatmap_df_detail", "data"),
        Input("interview_manual_id_detail", "value"),
        Input("switch_chronology_filter_detail", "value"),
        Input("heat_map_interview_detail", "clickData"),
        Input("chunk_number_detail", "data"),
        Input("side_bar_menu_switch", "value"),
        Input("ihc_outlier_threshold_value", "value"),
        Input("ihc_threshold_top_filter_value", "value"),
        prevent_initial_call=True,
    )
    def interview_heat_map_dash(
        interview_manual_id,
        heatmap_filter,
        click_data_2,
        chunk_number_storage,
        option_list,
        threshold_top_filter,
        outlier_threshold,
    ):
        if chronologie_analyse and "ihc" in option_list:
            chronologie_heatmap = chronology_matrix(
                data=ohtm_file,
                click_data="",
                click_data_2=click_data_2,
                ctx_triggered=ctx.triggered,
                interview_manual_id=interview_manual_id,
                heatmap_filter=heatmap_filter,
                outlier_threshold=outlier_threshold,
                threshold_top_filter=threshold_top_filter,
                topic_filtering=option_list,
                chunk_number_storage=chunk_number_storage,
                axis_titel_option=axis_titel_option,
            )
            if chronologie_heatmap is not None:
                fig = chronologie_heatmap[0]
                title = chronologie_heatmap[1]
                interview_id = chronologie_heatmap[2]
                chunk_number = chronologie_heatmap[3]
                tc_indicator = chronologie_heatmap[4]
                df_heatmap_interview = chronologie_heatmap[5]

                return fig, title, interview_id, tc_indicator, df_heatmap_interview
            else:
                return no_update, no_update, no_update, no_update, no_update
        else:
            interview_heatmap = heatmap_interview_simple(
                ohtm_file=ohtm_file,
                click_data="off",
                click_data_2=click_data_2,
                ctx_triggered=ctx.triggered,
                chunk_number_storage=chunk_number_storage,
                heatmap_filter=heatmap_filter,
                interview_manual_id=interview_manual_id,
                options=option_list,
                axis_titel_option=axis_titel_option,
            )
            fig = interview_heatmap[0]
            title = interview_heatmap[1]
            interview_id = interview_heatmap[2]
            chunk_number = interview_heatmap[3]
            tc_indicator = interview_heatmap[4]
            df_heatmap_interview = interview_heatmap[5]
            return fig, title, interview_id, tc_indicator, df_heatmap_interview

    # Interview Detail print the raw sents of the selected chunk
    @app.callback(
        Output("textarea_detail", "children"),
        Output("sent_title_detail", "children"),
        Output("chunk_number_detail", "data"),
        Input("heat_map_interview_detail", "clickData"),
        Input("-_button_detail", "n_clicks"),
        Input("+_button_detail", "n_clicks"),
        State("chunk_number_detail", "data"),
        State("interview_manual_id_detail", "value"),
        State("tc_indicator_detail", "data"),
        State("interview_heatmap_df_detail", "data"),
        prevent_initial_call=True,
    )
    def sent_drawing_detail_dash(
        click_data,
        input_before,
        input_next,
        chunk_number,
        interview_manual_id_detail,
        tc_indicator_detail,
        interview_heatmap_df_detail,
    ):
        if ctx.triggered[0]["value"] is None:
            if ctx.triggered[1]["value"] is None:
                if ctx.triggered[2]["value"] is None:
                    return no_update, no_update, no_update
        else:
            sent_chunk_drawing_heatmap_detail = chunk_sent_drawing(
                ohtm_file=ohtm_file,
                click_data_input=click_data,
                chunk_number=chunk_number,
                interview_id=interview_manual_id_detail,
                chronology_df=interview_heatmap_df_detail,
                tc_indicator=tc_indicator_detail,
            )
            chunk_sent = sent_chunk_drawing_heatmap_detail[0]
            sent_id = sent_chunk_drawing_heatmap_detail[1]
            chunk_id = sent_chunk_drawing_heatmap_detail[2]

            return chunk_sent, sent_id, chunk_id

    # Print the words from the topic-list page 5
    @app.callback(
        Output("topic_table", "children"),
        Input("word_number", "value"),
        Input("enter_print_topics", "n_clicks"),
        Input("side_bar_menu_switch", "value"),
    )
    def print_all_topics_dash(words, n_clicks, options_list):
        table = print_all_topics(words, n_clicks, ohtm_file, options=options_list)
        return table

    # Function to identifie which topic is clicked in any graph. The information is than returned and the first words
    # of this topic are printed in the topic field.
    @app.callback(
        Output("heatmap_interview_topic_nr", "data"),
        Input("heat_map_interview", "clickData"),
        Input("side_bar_menu_switch", "value"),
        prevent_initial_call=True,
    )
    def gloabl_topic_nr_update(click_data, sidebar_options):
        if click_data != None:
            if chronologie_analyse and "ihc" in sidebar_options:
                topic = click_data["points"][0]["y"]
                topic = topic.split(" - ")[0]
            else:
                topic = click_data["points"][0]["y"] 
            return topic 

    @app.callback(
        Output("heatmap_interview_detail_topic_nr", "data"),
        Input("heat_map_interview_detail", "clickData"),
        Input("side_bar_menu_switch", "value"),
        prevent_initial_call=True,
    )
    def gloabl_topic_nr_update(click_data, sidebar_options):
        if click_data != None:
            if chronologie_analyse and "ihc" in sidebar_options:
                topic = click_data["points"][0]["y"]
                topic = topic.split(" - ")[0]
            else:
                topic = click_data["points"][0]["y"]         
            return topic   

    @app.callback(
        Output("bar_topic_nr", "data"),
        Input("bar", "clickData"),
        prevent_initial_call=True,
    )
    def gloabl_topic_nr_update(click_data):
        if click_data != None:
            topic = click_data["points"][0]["x"]
            return topic

    @app.callback(
        Output("bar_detail_topic_nr", "data"),
        Input("bar2", "clickData"),
        prevent_initial_call=True,
    )
    def gloabl_topic_nr_update(click_data):
        if click_data != None:
            topic = click_data["points"][0]["x"]
            return topic

    @app.callback(
        Output("heatmap_corpus_topic_nr", "data"),
        Input("heat_map", "clickData"),
        prevent_initial_call=True,
    )
    def gloabl_topic_nr_update(click_data):
        if click_data != None:
            topic = click_data["points"][0]["x"]
            return topic

    @app.callback(
        Output("heatmap_corpus_detail_topic_nr", "data"),
        Input("heat_map_corpus_detail", "clickData"),
        prevent_initial_call=True,
    )
    def gloabl_topic_nr_update(click_data):
        if click_data != None:
            topic = click_data["points"][0]["x"]
            return topic

    # print the first 50 words of each topic that is selected on any graph on any page [menu]
    @app.callback(
        Output("topics", "children"),
        Output("topic_number_sidebar_1", "children"),
        Output("topic_label_side_bar", "children"),
        Input("input", "value"),
        Input("heatmap_interview_topic_nr", "data"),
        Input("heatmap_interview_detail_topic_nr", "data"),
        Input("bar_topic_nr", "data"),
        Input("bar_detail_topic_nr", "data"),
        Input("heatmap_corpus_topic_nr", "data"),
        Input("heatmap_corpus_detail_topic_nr", "data"),
        Input("heat_map_cv_topic_nr", "data"),
        Input("bar_graph_cv_topic_nr", "data"),
        Input("side_bar_menu_switch", "value"),
        prevent_initial_call=True,
    )
    def df_input(
        value1,
        value2,
        value3,
        value4,
        value5,
        value6,
        value7,
        value8,
        value9,
        option_list,
    ):
        if ctx.triggered[0]["value"] != None:
            if ctx.triggered[0]["prop_id"] == "side_bar_menu_switch.value":
                raise PreventUpdate
            topic_value = ctx.triggered[0]["value"]
            entry = top_words(topic_value, ohtm_file)
            topic_entry = "Topic: " + str(topic_value)
            if "topic_labels_on" in option_list:
                topic_label = ohtm_file["topic_labels"]["labels"][str(topic_value)]
                return entry, topic_entry, topic_label
            else:
                return entry, topic_entry, ""
        else:
            return no_update, no_update, no_update

    # Corpusheatmap page 5
    @app.callback(
        Output(component_id="heat_map_corpus_detail", component_property="figure"),
        Input("slct_archiv_heat_map_corpus_detail", "value"),
        Input("z_score_corpus_heatmap_detail", "value"),
        Input("corpus_heatmap_detail_topic", "value"),
        Input("corpus_heatmap_detail_threshold", "value"),
        Input("side_bar_menu_switch", "value"),
    )
    def update_graph(value, z_score_global, topic, threshold, options_list):
        fig = heatmap_corpus(
            ohtm_file,
            option_selected=str(value),
            z_score_global=z_score_global,
            show_fig=False,
            return_fig=True,
            topic_filter_number=topic,
            topic_filter_threshold=threshold,
            options=options_list,
        )
        return fig

    # Dropboxmenue for corpus heatmap page 1 and page 6
    @app.callback(
        Output("slct_archiv_heat_map_corpus_detail", "options"),
        Output("slct_archiv_heat_map_corpus_detail", "value"),
        Input("top_dic", "data"),
        prevent_initial_call=False,
    )
    def create_dropdown_list_dash(data):
        drop_down_menu = create_dropdown_list(ohtm_file)
        return drop_down_menu, "all"

    # Funktions Page 6 Chunk-View

    # Chunk-Number building and storage
    @app.callback(
        Output("chunk_number_cv", "data"),
        Input("heat_map_cv", "clickData"),
        Input("-_button_cv", "n_clicks"),
        Input("+_button_cv", "n_clicks"),
        State("chunk_number_cv", "data"),
        prevent_initial_call=True,
    )
    def create_chunk_number(click_data_input, mins, plus, store):
        if ctx.triggered[0]["prop_id"] == "+_button_cv.n_clicks":
            number = int(store)
            number += 1
            return number
        if ctx.triggered[0]["prop_id"] == "-_button_cv.n_clicks":
            number = int(store)
            number -= 1
            return number
        else:
            number = click_data_input["points"][0]["y"].split("**")[1]
            return number

    # Chunk_Heatmap

    @app.callback(
        Output("heat_map_cv", "figure"),
        Output("bar_cv", "figure"),
        Output("cv_results", "children"),
        Output("detail_info_cv", "children"),
        Output("topic_info_cv", "children"),
        Input("topic_cv", "value"),
        Input("topic_weight_cv", "value"),
        Input("start_search_cv", "n_clicks"),
        Input("slct_archiv", "value"),
        Input("correlation_cv", "value"),
        Input("topic_2_cv", "value"),
        Input("topic_2_weight_cv2", "value"),
        Input("sort_interview_cv", "n_clicks"),
        Input("sort_topic_1_cv", "n_clicks"),
        Input("sort_topic_2_cv", "n_clicks"),
        Input("side_bar_menu_switch", "value"),
        prevent_initial_call=True,
    )
    def output_info_cv(
        topic_1,
        weight_1,
        n_clicks,
        option_select,
        correlation,
        topic_2,
        weight_2,
        c1,
        c2,
        c3,
        option_list,
    ):
        import plotly.graph_objects as go

        if n_clicks:
            results = []
            fig_heat = chunk_heatmap(
                ohtm_file,
                option_selected=option_select,
                show_fig=False,
                return_fig=True,
                topic_1_number=topic_1,
                topic_1_weight=weight_1,
                topic_2_number=topic_2,
                topic_2_weight=weight_2,
                correlation=correlation,
                sort_filter=ctx.triggered[0]["prop_id"].split(".")[0],
                options=option_list,
                axis_titel_option=axis_titel_option,
            )
            results = fig_heat[1]
            results_header = str(len(results)) + " Chunks"
            detail_results_cv = print_details_cv_function(
                results, options=option_list, labels=ohtm_file["topic_labels"]["labels"]
            )
            fig = fig_heat[0]

            fig_bar = bar_graph_cv_function(
                ohtm_file,
                option_selected=option_select,
                show_fig=False,
                return_fig=True,
                topic_1_number=topic_1,
                topic_1_weight=weight_1,
                topic_2_number=topic_2,
                topic_2_weight=weight_2,
                correlation=correlation,
                options=option_list,
                axis_titel_option=axis_titel_option,
            )

            return (
                fig,
                fig_bar,
                results_header,
                detail_results_cv[0],
                detail_results_cv[1],
            )
        else:
            return go.Figure(), go.Figure(), "0 Chunks", [], []

    @app.callback(
        Output("textarea_cv", "children"),
        Output("interview_titel_cv", "children"),
        Output("detail_info_cv_chunk", "children"),
        Input("heat_map_cv", "clickData"),
        Input("chunk_number_cv", "data"),
        Input("side_bar_menu_switch", "value"),
        prevent_initial_call=True,
    )
    def chunk_view_text_print(click_data, chunk_nr, option):
        chunk_text = chunk_sent_drawing_cv(
            ohtm_file=ohtm_file,
            click_data_input=click_data,
            chunk_number=chunk_nr,
            options=option,
        )
        interview = (
            click_data["points"][0]["y"].split("**")[0]
            + "- Chunk: "
            + str(chunk_text[2])
        )
        return chunk_text[0], interview, chunk_text[1]

    @app.callback(
        Output("heat_map_cv_topic_nr", "data"),
        Input("heat_map_cv", "clickData"),
        prevent_initial_call=True,
    )
    def gloabl_topic_nr_update(click_data):
        if click_data != None:
            topic = click_data["points"][0]["x"]
            return topic

    @app.callback(
        Output("bar_graph_cv_topic_nr", "data"),
        Input("bar_cv", "clickData"),
        prevent_initial_call=True,
    )
    def gloabl_topic_nr_update(click_data):
        if click_data != None:
            topic = click_data["points"][0]["x"]
            return topic

    @app.callback(
        Output("dropdown_sort", "label"),
        Input("sort_interview_cv", "n_clicks"),
        Input("sort_topic_1_cv", "n_clicks"),
        Input("sort_topic_2_cv", "n_clicks"),
    )
    def dropdown_sort_label_retunr(c1, c2, c3):
        if not ctx.triggered:
            return "Sort Filter"
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if button_id == "sort_interview_cv":
            return "Interview"
        elif button_id == "sort_topic_1_cv":
            return "Topic 1"
        elif button_id == "sort_topic_2_cv":
            return "Topic 2"
        return "Sort Filter"

    @app.callback(
        Output("sidebar-info", "children"),
        Input("top_dic", "data"),
        prevent_initial_call=False,
    )
    def sidebar_info_output(data):
        output = sideboard_info_function(ohtm_file)

        return output

    # Function to switch Tooltips on or off. The Tooltips are created in tooltip_function seperatly

    @app.callback(
        Output("tooltip_store", "children"),
        Input("side_bar_menu_switch", "value"),
    )
    def tooltip_showing(data):
        if "tooltip_on" in data:
            tooltip = tooltip_creation()
            return tooltip
        else:
            return []

    # Impressum Function
    @app.callback(
        Output("impressum", "children"),
        Input("impressum_button", "n_clicks"),
    )
    def impressum_output(n_clicks):
        return (
            dbc.Offcanvas(
                html.P(
                    impressum_text,
                    style={
                        "whiteSpace": "pre-line",
                        "font-size": "0.8vw",},
                ),
                id="offcanvas",
                title=impressum_titel_text,
                is_open=True,
                style={"width": "40vw"},
            ),
        )
    # Glossar Function
    @app.callback(
        Output("glossar", "children"),
        Input("glossar_button", "n_clicks"),
    )
    def glossar_output(n_clicks):
        return (
            dbc.Offcanvas(
                html.P(
                    glossar_text,
                    style={
                        "whiteSpace": "pre-line",
                        "font-size": "0.8vw",},
                ),
                id="offcanvas_glossar",
                title=glossar_titel_text,
                is_open=True,
                style={"width": "40vw"},
            ),
        )

    return app
