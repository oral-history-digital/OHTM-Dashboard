from settings_OHDdash import *

global top_dic
global chronology_df
load_file_name = "OHD_final_100C_100T_A5"
#load_file_name = "OHD_auswahl_pre_150c_80t"

with open(file_workingfolder + load_file_name) as f:
    top_dic = json.load(f)


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "14%",
    "padding": "2rem 1rem",
    "background-color": "#2B88AF",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "14%",
    "margin-right": "0,5%",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        dcc.Store(id="top_dic", data={}, storage_type="session"),
        dcc.Store(id="heat_dic", data={}, storage_type="session"),
        dcc.Store(id="top_dic2", data={}, storage_type="session"),
        dcc.Store(id="data_path", storage_type="session"),
        dcc.Store(id = "heatmap_interview_topic_nr", data = "", storage_type="session"),
        dcc.Store(id="heatmap_interview_detail_topic_nr", data="", storage_type="session"),
        dcc.Store(id="bar_topic_nr", data="", storage_type="session"),
        dcc.Store(id="bar_detail_topic_nr", data="", storage_type="session"),
        dcc.Store(id="heatmap_corpus_topic_nr", data="", storage_type="session"),
        dcc.Store(id="chunk_number_frontpage", data="", storage_type = "sesssion"),
        dcc.Store(id="chunk_number_detail", data="", storage_type="sesssion"),

        html.Img(src=b64_image(image_filename), style={"max-width": "100%"}),
        dbc.Row(html.Hr()),
        html.Div(
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Dash-Board", href="/"),
                dbc.DropdownMenuItem("Text Search", href="/page-1"),
                dbc.DropdownMenuItem("Balkendiagram", href="/page-2"),
                dbc.DropdownMenuItem("Chronology Heamtap", href="/page-3"),
                dbc.DropdownMenuItem("Topic Übersicht", href="/page-4"),
                               ],
            label="Menu",
            color="dark",
           # menu_variant="dark",
            className ="m-1",
             ),
        ),
        dbc.Row(html.Hr()),
        dbc.Row([
            html.H5(dbc.Badge("Topic Wortliste", color="dark"))
        ]),
        dbc.Row([
            dbc.Input(id="input", placeholder="Topic Nummer eingeben", type="number",size="sm",
                      min=0, max=100 - 1, step=1
                      ),
        ]),
        dbc.Row(html.Hr()),
        dbc.Row([
            html.Div(id="topics",
                     style={
                         'height': '150px',
                         'width':'95%',
                        "padding": "1% 1%",
                         'display': 'block',
                         'font-size':"15px",
                         'background-color':'rgb(249,249,249)',
                         "overflow": "auto"}
                             )
        ]),
        dbc.Row(),
        dbc.Row(html.Hr()),

        dbc.Accordion(
            [
                dbc.AccordionItem(html.Div([
                    dbc.Row([
                        dcc.Textarea(
                            id='textarea-example',
                            value='Hier können sie Notizen machen',
                            style={'width': 220, 'height': 170, 'font-size': "15px", },
                        ),
                    ]),

                ]),

                    title="Notizen",
                ),
                dbc.AccordionItem(html.Div([
                    dbc.Row([
                        dbc.RadioItems(
                            options=[
                                {"label": "Horizontal", "value": 1},
                                {"label": "Vertikal", "value": 2},
                            ],
                            value=1,
                            id="correlation_switch",
                            inline=True,
                        ),
                    ]),
                    dbc.Row([
                        html.Div([
                            dbc.Pagination(id="gross_nr_correlations_per_chunk_pagination", max_value=4, min_value=2,
                                           size="sm")
                        ]),
                    ]),
                    dbc.Row([
                        html.Div(id="correlation_output",
                                 style={
                                     'height': '200px',
                                     'width': '95%',
                                     "padding": "1% 1%",
                                     'whiteSpace': 'pre-line',
                                     'display': 'inline-block',
                                     'font-size': "15px",
                                     'background-color': 'rgb(249,249,249)',
                                     "overflow": "auto"}
                                 ),
                    ]),
               ]),
                    title="Correlation",
                ),

            ],
            always_open=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(id="slct_archiv", options = [ ],
                                 value = "all",
                                multi=False,
                                style = {'width': "80%"},
                                 ),

                ], width=4),
                dbc.Col([
                    dbc.Checklist(
                        options=[
                            {"label": "Z Score", "value": "z_score"},
                        ],
                        value=[],
                        id="switch_z_score_global_heatmap",
                        switch=True,
                    ),


                ], width = 1)
            ]),

            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='heat_map', figure={})
                ], width=6),

                dbc.Col([
                    dcc.Graph(id="bar", figure={})
                ], width=6),
            ]),

            dbc.Row([
                dbc.Col([
                    html.H5([dbc.Badge(id="interview_titel", color="dark")], className="text-center")
                ], width=6),
                dbc.Col([], width=2),
                dbc.Col([
                    html.H5([

                    dbc.Button("<", id="-_button_frontpage", color="dark", size="sm"),

                    dbc.Badge("chunk", id="sent_titel", color="dark"),

                    dbc.Button(">", id="+_button_frontpage", color="dark", size = "sm")]),
                ],
                     width = 2),
                dbc.Col([], width=2),
                dbc.Row([
                    dbc.Col([
                        dbc.Checklist(
                            options=[
                                {"label": "Topic Filter", "value": "filter"},
                                {"label": "Z Score", "value": "z_score"},
                                {"label": "Mark", "value": "mark"}
                            ],
                            value=[],
                            id="switch_chronology_filter",
                            switch=True,
                            inline = True
                        ),

                    ], width =3),
                    dbc.Col([
                        html.Div(dbc.Input(id='interview_manual_id', placeholder="Interview",type='word')),

                    ], width=1),
                    dbc.Col([
                        html.Div(dbc.Input(id='threshold_top_filter_value', placeholder="Top Filter Threshold", type='number')),

                    ], width = 1),
                    dbc.Col([
                        html.Div(dbc.Input(id='outlier_threshold_value', placeholder="Outlier Threshold",
                                           type='number')),
                    ], width=1)
                ]),

            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='heat_map_interview', figure={})
                ], width=6),
                dbc.Col([
                    dbc.Row([
                        html.Div(id='textarea',
                                 style={
                                     'whiteSpace': 'pre-line',
                                     'display': 'inline-block',
                                     'height': '400px',
                                     'display': 'block',
                                     'font-size': "15px",
                                     'background-color': 'rgb(249,249,249)',
                                     "overflow": "auto",
                                        }),
                    ]),
                ], width=5),
            ]),

        ]

    elif pathname == "/page-1":
        return [
            dbc.Row([
            dbc.Col([
                html.Div([
                    dbc.InputGroup(
                        [dbc.InputGroupText("Topic"), dbc.Input(id='topic_print', placeholder="Topic", type='number'),
                    ], className="mb-3"),
                    dbc.InputGroup(
                        [dbc.InputGroupText("Weight"), dbc.Input(id='weight_print', placeholder="Weight", type='number'),
                    ], className="mb-3"),
                    dbc.InputGroup(
                        [dbc.InputGroupText("Interview ID"), dbc.Input(id='interview_id_search', placeholder="Interview ID", type='text'),
                    ], className="mb-3"),

            ]),
            ], width = 2),

            dbc.Col([
                html.Div([
                    dbc.InputGroup([dbc.InputGroupText("Topic_c 1"), dbc.Input(id='topic_c_1', placeholder="Topic", type='number'),
                         ], className="mb-3"),
                    dbc.InputGroup([dbc.InputGroupText("Topic_c 2"),dbc.Input(id='topic_c_2', placeholder="Topic", type='number'),
                         ], className="mb-3"),
                    dbc.InputGroup([dbc.Select(options=[
                        {"label": "Korpus Search", "value": 1},
                        {"label": "Interview Search", "value": 2},
                        {"label": "Correlation Search Vertical", "value": 3},
                        {"label": "Correlation Search Horizontal", "value": 4},

                    ], id = "text_search_options")])


                ]),
            ], width = 2),
            dbc.Col([
                html.Div([
                    dbc.InputGroup([dbc.InputGroupText("Topic_c 3"),
                                    dbc.Input(id='topic_c_3', placeholder="Topic", type='number'),
                                    ], className="mb-3"),
                    dbc.InputGroup([dbc.InputGroupText("Topic_c 4"),
                                    dbc.Input(id='topic_c_4', placeholder="Topic", type='number'),
                                    ], className="mb-3"),
                    dbc.InputGroup([ dbc.Button("Search", id='enter_print', color="dark")], className="mb-3"),

                ]),
            ], width=2),
                ]),
            dbc.Row([
                dbc.Col([html.Div(id = "table-container")], width=8),
            ]),

                ]

    elif pathname == "/page-2":
        return [
            dbc.Row([dcc.Graph(id="bar2", figure={})
                     ]),
            dbc.Row([
                dbc.Col([
                    dbc.Input(id="input1", placeholder="Topic Nummer eingeben", type="number",
                              min=0, max=100 - 1, step=1
                              )
                ]),
                dbc.Col([
                    dbc.Input(id="input2", placeholder="Topic Nummer eingeben", type="number",
                              min=0, max=100 - 1, step=1
                              )
                ]),
                dbc.Col([
                    dbc.Input(id="input3", placeholder="Topic Nummer eingeben", type="number",
                              min=0, max=100 - 1, step=1
                              )
                ]),
                dbc.Row([
                    dbc.Col([
                        html.Div(id="topics1")
                    ]),
                    dbc.Col([
                        html.Div(id="topics2")
                    ]),
                    dbc.Col([
                        html.Div(id="topics3")
                    ]),

                ]), ])
        ]

    elif pathname == "/page-3":
        return [
            dbc.Row([
                dbc.Col([
                    dbc.Checklist(
                        options=[
                            {"label": "Topic Filter", "value": "filter"},
                            {"label": "Z Score", "value": "z_score"},
                            {"label": "Mark", "value": "mark"},
                        ],
                        value=[],
                        id="switch_chronology_filter_detail",
                        switch=True,
                        inline=True
                    ),

                ], width=3),
                dbc.Col([
                    html.Div(dbc.Input(id='interview_manual_id_detail', placeholder="Interview", type='word')),

                ], width=1),
                dbc.Col([
                    html.Div(dbc.Input(id='threshold_top_filter_value_detail', placeholder="Top Filter Threshold",
                                       type='number')),

                ], width=1),
                dbc.Col([
                    html.Div(dbc.Input(id='outlier_threshold_value_detail', placeholder="Outlier Threshold",
                                       type='number')),
                ], width=1)
            ]),

            dbc.Row([
                html.H5([dbc.Badge(id="interview_title_detail", color="dark")], className="text-center")
            ]),
            dbc.Row([
                    dcc.Graph(id='heat_map_interview_detail', figure={}),
            ]),
            dbc.Row([
                dbc.Col([], width = 5),
                dbc.Col([
                    dbc.Button("<", id="-_button_detail", color="dark", size="sm"),
                    dbc.Badge("chunk", id="sent_title_detail", color="dark", className="text-center"),
                    dbc.Button(">", id="+_button_detail", color="dark", size="sm"),
                    ], width = 2),
                dbc.Col([], width = 5),
            ]),
            dbc.Row(html.Hr()),
            dbc.Row([
                html.Div(id='textarea_detail',
                         style={
                             'whiteSpace': 'pre-line',
                             'height': '400px',
                             'display': 'block',
                             'font-size': "15px",
                             'background-color': 'rgb(249,249,249)',
                             "overflow": "auto",
                         }),
             ]),

        ]

    elif pathname == "/page-4":
        return [
            dbc.Col([
            html.Div(dbc.Input(id='word_number', placeholder="Anzahl Wörter pro Topic", type='number')),
            dbc.Button("print", id='enter_print_topics', color="dark", size="sm"),
            ], width = 2),

            dbc.Col([
            html.Div(id = "topic_table")
                ], width = 8),
                ]


    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-dark"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# Heatmap für den gesamten Corpus mit Auswahlmöglichkeit für die einzelnen Archive
@app.callback(
    Output(component_id='heat_map', component_property='figure'),
    Input('slct_archiv', "value"),
    Input("switch_z_score_global_heatmap", "value"),
)
def update_graph(value, z_score_global):

    if "z_score" in z_score_global:
        z_score = True
    else: z_score = False

    fig = heatmap_corpus(top_dic, option_selected=str(value),z_score = z_score,show_fig=False, return_fig=True)
    return fig


# Chronologie Heatmap
@app.callback(
    Output(component_id='heat_map_interview', component_property='figure'),
    Output("interview_titel", "children"),
    Input("heat_map", "clickData"),
    Input("switch_chronology_filter", "value"),
    Input("threshold_top_filter_value", "value"),
    Input("outlier_threshold_value", "value"),
    Input("interview_manual_id", "value"),
    Input("heat_map_interview", "clickData"),
    Input("chunk_number_frontpage", "data"),

    prevent_initial_call = True

)
def interview_heat_map(clickData, heatmap_filter, top_filter_th, outlier_th, interview_manual_id,clickData_2, chunk_number_storage):
    global interview_id
    global chronology_df
    global tc_indicator


    if "filter" in heatmap_filter:
        topic_filtering = True
    else: topic_filtering = False

    if "z_score" in heatmap_filter:
        z_score = True
    else: z_score = False

    if top_filter_th == None:
        top_filter_th = 0.01
    if outlier_th == None:
        outlier_th = 0.02

    if interview_manual_id is not None:
        interview_id = interview_manual_id
        if interview_manual_id == '':
            interview_id = clickData["points"][0]["y"]
    else:
        interview_id = clickData["points"][0]["y"]

    chronology_data = chronology_matrix(top_dic, interview_id, return_fig=True, print_fig=False, z_score = z_score, topic_filter = topic_filtering, threshold_top_filter=top_filter_th, outlier_threshold=outlier_th)
    chronology_df = chronology_data[1]
    tc_indicator = chronology_data[2]
    fig = chronology_data[0]

    if ctx.triggered[0]["prop_id"] == "heat_map.clickData":
        titel = "Interview chronology " + interview_id
    elif ctx.triggered[0]["prop_id"] == "interview_manual_id.value":
        titel = "Interview chronology " + interview_id
    else:
        if "mark" in heatmap_filter:
            if tc_indicator:

                row_index_clicked = chronology_df.index.get_loc(chronology_df[chronology_df["minute"] == clickData_2["points"][0]["x"]].index[0])
                chunk_number_clicked = chronology_df.loc[row_index_clicked]["ind"]

                if chunk_number_clicked == 0:
                    row_index = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_clicked].index[0])
                    time_id = chronology_df.loc[row_index]["minute"]
                    row_index_after = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_clicked + 1].index[0])
                    time_id_after = chronology_df.loc[row_index_after]["minute"]

                    x_1 = (time_id + time_id_after) / 2
                    x_0 = x_1 - time_id


                elif chunk_number_clicked == chronology_df["ind"][chronology_df.index[-1]]:
                    row_index = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_clicked].index[0])
                    time_id = chronology_df.loc[row_index]["minute"]
                    row_index_before = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_clicked - 1].index[0])
                    time_id_before = chronology_df.loc[row_index_before]["minute"]

                    x_0 = (time_id + time_id_before) / 2
                    x_1 = time_id + (time_id - x_0)

                else:
                    row_index = chronology_df.index.get_loc(
                    chronology_df[chronology_df["ind"] == chunk_number_clicked].index[0])
                    time_id = chronology_df.loc[row_index]["minute"]
                    row_index_before = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_clicked - 1].index[0])
                    time_id_before = chronology_df.loc[row_index_before]["minute"]
                    row_index_after = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_clicked + 1].index[0])
                    time_id_after = chronology_df.loc[row_index_after]["minute"]

                    x_0 = (time_id + time_id_before) / 2
                    x_1 = (time_id + time_id_after) / 2

            else:
                x_0 = clickData_2["points"][0]["x"]-0.5
                x_1 = clickData_2["points"][0]["x"]+0.5

            if ctx.triggered[0]["prop_id"] == "chunk_number_frontpage.data":
                if tc_indicator:

                    if chunk_number_storage == 0:
                        row_index = chronology_df.index.get_loc(
                            chronology_df[chronology_df["ind"] == chunk_number_storage].index[0])
                        time_id = chronology_df.loc[row_index]["minute"]
                        row_index_after = chronology_df.index.get_loc(
                            chronology_df[chronology_df["ind"] == chunk_number_storage + 1].index[0])
                        time_id_after = chronology_df.loc[row_index_after]["minute"]

                        x_1 = (time_id + time_id_after) / 2
                        x_0 = x_1 - time_id


                    elif chunk_number_storage == chronology_df["ind"][chronology_df.index[-1]]:
                        row_index = chronology_df.index.get_loc(
                            chronology_df[chronology_df["ind"] == chunk_number_storage].index[0])
                        time_id = chronology_df.loc[row_index]["minute"]
                        row_index_before = chronology_df.index.get_loc(
                            chronology_df[chronology_df["ind"] == chunk_number_storage - 1].index[0])
                        time_id_before = chronology_df.loc[row_index_before]["minute"]

                        x_0 = (time_id + time_id_before) / 2
                        x_1 = time_id + (time_id - x_0)

                    else:

                        row_index = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_storage].index[0])
                        time_id = chronology_df.loc[row_index]["minute"]
                        row_index_before = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_storage-1].index[0])
                        time_id_before = chronology_df.loc[row_index_before]["minute"]
                        row_index_after = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_storage+1].index[0])
                        time_id_after = chronology_df.loc[row_index_after]["minute"]

                        x_0 = (time_id+time_id_before)/2
                        x_1 = (time_id+time_id_after)/2

                else:
                    x_0 = chunk_number_storage - 0.5
                    x_1 = chunk_number_storage + 0.5


            fig.add_vrect(
                x0=x_0, x1=x_1,
                fillcolor="LightSalmon", opacity=0.3,
                layer="above", line_width=1,)

        titel = "Interview chronology " + interview_id

    return fig, titel


# Ausgabe der Raw-Sätze des Chunks
@app.callback(
    Output(component_id='textarea', component_property='children'),
    Output("sent_titel", "children"),
    Output("chunk_number_frontpage", "data"),
    Input("heat_map_interview", "clickData"),
    Input("-_button_frontpage", "n_clicks"),
    Input("+_button_frontpage", "n_clicks"),
    State("chunk_number_frontpage", "data"),
    prevent_initial_call=True
)
def sent_drawing(clickData, input_before, input_next, chunk_number):

    if ctx.triggered[0]["prop_id"] == "+_button_frontpage.n_clicks":
        chunk_id = chunk_number +1
    elif ctx.triggered[0]["prop_id"] == "-_button_frontpage.n_clicks":
        chunk_id = chunk_number -1
    else:

        if tc_indicator:
            time_id = clickData["points"][0]["x"]
            row_index = chronology_df.index.get_loc(chronology_df[chronology_df["minute"] == time_id].index[0]) # die Information aus dem DF aus Chronology. Hier wird die Zeit und das zugehörige DF gespeichert. Wir müssen zunächst den Index der Zeitangabe finden
            chunk_id = chronology_df.loc[row_index]["ind"] # mit dem Index der Zeitangabe kann hier der Chunkwert ausgelesen werden und als chunk_id übergeben werden
        else:
            chunk_id = clickData["points"][0]["x"]

    sent_example = []
    speaker = "None"
    for a in top_dic["corpus"][interview_id[0:3]][interview_id]["sent"]:
        if top_dic["corpus"][interview_id[0:3]][interview_id]["sent"][a]["chunk"] == int(chunk_id):
            if speaker == top_dic["corpus"][interview_id[0:3]][interview_id]["sent"][a]["speaker"]:
                sent_example.append(top_dic["corpus"][interview_id[0:3]][interview_id]["sent"][a]["raw"] + ". ")
            else:
                sent_example.append("\n" + "*" + top_dic["corpus"][interview_id[0:3]][interview_id]["sent"][a]["speaker"] + "*: ")
                sent_example.append(top_dic["corpus"][interview_id[0:3]][interview_id]["sent"][a]["raw"] + ". ")
                speaker = top_dic["corpus"][interview_id[0:3]][interview_id]["sent"][a]["speaker"]

    sent_id = "Chunk: " + str(chunk_id)
    return sent_example, sent_id, chunk_id


# Balkendiagramm auf der ersten Seite
@app.callback(
    Output(component_id="bar", component_property="figure"),
    Input("top_dic", "data2"),
)
def bar_map(data2):
    fig = bar_graph_corpus(top_dic, show_fig = False, return_fig = True)
    return fig

# Balkendiagramm auf der dritten Seite
@app.callback(
    Output(component_id="bar2", component_property="figure"),
    Input("top_dic2", "data2"),

)
def bar_map2(data2):
    fig = bar_graph_corpus(top_dic, show_fig = False, return_fig = True)
    return fig

@app.callback(
    Output("heatmap_interview_topic_nr", "data"),
    Input("heat_map_interview", "clickData"),
    prevent_initial_call=True
)
def gloabl_topic_nr_update(clickData):

    topic = clickData["points"][0]["y"]
    return topic

@app.callback(
    Output("heatmap_interview_detail_topic_nr", "data"),
    Input("heat_map_interview_detail", "clickData"),
    prevent_initial_call=True
)
def gloabl_topic_nr_update(clickData):

    topic = clickData["points"][0]["y"]
    return topic

@app.callback(
    Output("bar_topic_nr", "data"),
    Input("bar", "clickData"),
    prevent_initial_call=True
)
def gloabl_topic_nr_update(clickData):

    topic = clickData["points"][0]["x"]
    return topic

@app.callback(
    Output("bar_detail_topic_nr", "data"),
    Input("bar2", "clickData"),
)
def gloabl_topic_nr_update(clickData):

    topic = clickData["points"][0]["x"]
    return topic

@app.callback(
    Output("heatmap_corpus_topic_nr", "data"),
    Input("heat_map", "clickData"),

)
def gloabl_topic_nr_update(clickData):

    topic = clickData["points"][0]["x"]
    return topic


# Ausgabe der ersten 50 Worte des ausgewählten Topics von jedem Graphen bei Click oder manueller Eingabe
@app.callback(
    Output("topics", "children"),
    Input("input", "value"),
    Input("heatmap_interview_topic_nr", "data"),
    Input("heatmap_interview_detail_topic_nr", "data"),
    Input("bar_topic_nr", "data"),
    Input("bar_detail_topic_nr", "data"),
    Input("heatmap_corpus_topic_nr", "data"),
    prevent_initial_call=True

)
def df_input(value1, value2, value3, value4, value5, value6):

    topic_value = ctx.triggered[0]["value"]
    entry = top_words(topic_value, top_dic)

    return entry

@app.callback(
    Output("topics1", "children"),
    Input("input1", "value"),
    prevent_initial_call=True
)
def df_input(value):
    entry = top_words(value, top_dic)
    return entry

@app.callback(
    Output("topics2", "children"),
    Input("input2", "value"),
    prevent_initial_call=True
)
def df_input(value):
    entry = top_words(value, top_dic)
    return entry

@app.callback(
    Output("topics3", "children"),
    Input("input3", "value"),
    prevent_initial_call=True
)
def df_input(value):
    entry = top_words(value, top_dic)
    return entry

# Durchsuchung alles Chunks nach den größten weights für ein bestimmtes Topic
@app.callback(
    Output("table-container", "children"),
    Input("topic_print", "value"),
    Input("weight_print", "value"),
    Input("enter_print", "n_clicks"),
    Input("interview_id_search", "value"),
    Input("text_search_options", "value"),
    Input('topic_c_1', "value"),
    Input('topic_c_2', "value"),
    Input('topic_c_3', "value"),
    Input('topic_c_4', "value"),

)

def weight_print(topic_print, weight_print, n_clicks, interview_id,text_search_options, t_1, t_2, t_3, t_4):

    if ctx.triggered[0]["prop_id"] == "enter_print.n_clicks":
        if text_search_options == "2":
            sent_final = []
            topic = topic_print
            chunk = weight_print
            a = interview_id[:3]
            i = interview_id
            for chunks in top_dic["weight"][a][i]:
                if str(top_dic["weight"][a][i][chunks][str(topic)]) >= str(chunk):
                    chunk_id = chunks
                    sent_current = []
                    for sents in top_dic["corpus"][a][i]["sent"]:
                        int_sent = copy.deepcopy(top_dic["corpus"][a][i]["sent"][sents]["chunk"])
                        if int(int_sent) == int(chunks):
                            sent_current.append(str(top_dic["corpus"][a][i]["sent"][sents]["raw"]) + " ")
                    sent_current = " ".join(sent_current)
                    sent_current_2 = (str(top_dic["weight"][a][i][chunks][str(topic)]), i, chunk_id, sent_current)
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


        if text_search_options == "1":
            sent_final = []
            topic = topic_print
            chunk = weight_print
            for a in top_dic["weight"]:
                for i in top_dic["weight"][a]:
                    for chunks in top_dic["weight"][a][i]:
                        if str(top_dic["weight"][a][i][chunks][str(topic)]) >= str(chunk):
                            sent_id = i
                            chunk_id = chunks
                            sent_current = []

                            for sents in top_dic["corpus"][a][i]["sent"]:
                                int_sent = copy.deepcopy(top_dic["corpus"][a][i]["sent"][sents]["chunk"])
                                if int(int_sent) == int(chunks):
                                    sent_current.append(str(top_dic["corpus"][a][i]["sent"][sents]["raw"]) + " ")
                            sent_current = " ".join(sent_current)
                            sent_current_2 = (str(top_dic["weight"][a][i][chunks][str(topic)]),sent_id,chunk_id, sent_current)
                            sent_final.append(sent_current_2)
            sent_final.sort(reverse=True)
            df = pd.DataFrame(sent_final)

            df = df.round(3)
            df.columns=["weight", "Interview", "Chunk Nr", "Chunk"]
            # data = df_rounded.to_dict('records')
            # columns = [{"name": i, "id": i} for i in df_rounded.columns]
            table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, color="dark", responsive = True, )

            return table

        if text_search_options == "3":

            a = global_vertical_correlation_search_json(top_dic, t1=t_1, t2=t_2, t3 =t_3, t4 = t_4, return_search=True)
            df = pd.DataFrame(a)
            df.columns = ["Interview", "Chunk Nr"]
            table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, color="dark",
                                             responsive=True, )
            return table

        if text_search_options == "4":

            a = global_horizontal_correlation_search_json(top_dic, t1=t_1, t2=t_2, return_search=True)
            df = pd.DataFrame(a)
            df.columns = ["Interview", "Chunk Nr"]
            table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, color="dark",
                                             responsive=True, )
            return table




# Heatmap Chronology Heatmap Detail


# Chronologie Heatmap


@app.callback(
    Output(component_id='heat_map_interview_detail', component_property='figure'),
    Output("interview_title_detail", "children"),
    Input("interview_manual_id_detail", "value"),
    Input("switch_chronology_filter_detail", "value"),
    Input("threshold_top_filter_value_detail", "value"),
    Input("outlier_threshold_value_detail", "value"),
    Input("heat_map_interview_detail", "clickData"),
    Input("chunk_number_detail", "data"),

)
def interview_heat_map(interview_manual_id, heatmap_filter, top_filter_th, outlier_th,clickData_2, chunk_number_storage):
    global chronology_df_detail
    global tc_indicator_detail
    global interview_id_detail


    if "filter" in heatmap_filter:
        topic_filtering = True
    else: topic_filtering = False

    if "z_score" in heatmap_filter:
        z_score = True
    else: z_score = False

    if top_filter_th == None:
        top_filter_th = 0.01
    if outlier_th == None:
        outlier_th = 0.02

    interview_id_detail = interview_manual_id

    chronology_data = chronology_matrix(top_dic, interview_id_detail, return_fig=True, print_fig=False, z_score = z_score, topic_filter = topic_filtering, threshold_top_filter=top_filter_th, outlier_threshold=outlier_th)
    chronology_df_detail = chronology_data[1]
    tc_indicator_detail = chronology_data[2]
    fig = chronology_data[0]

    if ctx.triggered[0]["prop_id"] == "interview_manual_id_detail.value":
        titel = "Interview chronology " + interview_id_detail
    else:
        if "mark" in heatmap_filter:
            if tc_indicator_detail:

                row_index_clicked = chronology_df_detail.index.get_loc(chronology_df_detail[chronology_df_detail["minute"] == clickData_2["points"][0]["x"]].index[0])
                chunk_number_clicked = chronology_df_detail.loc[row_index_clicked]["ind"]

                if chunk_number_clicked == 0:
                    row_index = chronology_df_detail.index.get_loc(chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked].index[0])
                    time_id = chronology_df_detail.loc[row_index]["minute"]
                    row_index_after = chronology_df_detail.index.get_loc(chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked + 1].index[0])
                    time_id_after = chronology_df_detail.loc[row_index_after]["minute"]

                    x_1 = (time_id + time_id_after) / 2
                    x_0 = x_1 - time_id


                elif chunk_number_clicked == chronology_df_detail["ind"][chronology_df_detail.index[-1]]:
                    row_index = chronology_df_detail.index.get_loc(chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked].index[0])
                    time_id = chronology_df_detail.loc[row_index]["minute"]
                    row_index_before = chronology_df_detail.index.get_loc(chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked - 1].index[0])
                    time_id_before = chronology_df_detail.loc[row_index_before]["minute"]

                    x_0 = (time_id + time_id_before) / 2
                    x_1 = time_id + (time_id - x_0)

                else:
                    row_index = chronology_df_detail.index.get_loc(
                    chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked].index[0])
                    time_id = chronology_df_detail.loc[row_index]["minute"]
                    row_index_before = chronology_df_detail.index.get_loc(chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked - 1].index[0])
                    time_id_before = chronology_df_detail.loc[row_index_before]["minute"]
                    row_index_after = chronology_df_detail.index.get_loc(chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked + 1].index[0])
                    time_id_after = chronology_df_detail.loc[row_index_after]["minute"]

                    x_0 = (time_id + time_id_before) / 2
                    x_1 = (time_id + time_id_after) / 2

            else:
                x_0 = clickData_2["points"][0]["x"]-0.5
                x_1 = clickData_2["points"][0]["x"]+0.5

            if ctx.triggered[0]["prop_id"] == "chunk_number_detail.data":
                if tc_indicator_detail:

                    if chunk_number_storage == 0:
                        row_index = chronology_df_detail.index.get_loc(
                            chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage].index[0])
                        time_id = chronology_df_detail.loc[row_index]["minute"]
                        row_index_after = chronology_df_detail.index.get_loc(
                            chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage + 1].index[0])
                        time_id_after = chronology_df_detail.loc[row_index_after]["minute"]

                        x_1 = (time_id + time_id_after) / 2
                        x_0 = x_1 - time_id


                    elif chunk_number_storage == chronology_df_detail["ind"][chronology_df_detail.index[-1]]:
                        print("last")
                        row_index = chronology_df_detail.index.get_loc(
                            chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage].index[0])
                        time_id = chronology_df_detail.loc[row_index]["minute"]
                        row_index_before = chronology_df_detail.index.get_loc(
                            chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage - 1].index[0])
                        time_id_before = chronology_df_detail.loc[row_index_before]["minute"]

                        x_0 = (time_id + time_id_before) / 2
                        x_1 = time_id + (time_id - x_0)

                    else:

                        row_index = chronology_df_detail.index.get_loc(chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage].index[0])
                        time_id = chronology_df_detail.loc[row_index]["minute"]
                        row_index_before = chronology_df_detail.index.get_loc(chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage-1].index[0])
                        time_id_before = chronology_df_detail.loc[row_index_before]["minute"]
                        row_index_after = chronology_df_detail.index.get_loc(chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage+1].index[0])
                        time_id_after = chronology_df_detail.loc[row_index_after]["minute"]

                        x_0 = (time_id+time_id_before)/2
                        x_1 = (time_id+time_id_after)/2

                else:
                    x_0 = chunk_number_storage - 0.5
                    x_1 = chunk_number_storage + 0.5


            fig.add_vrect(
                x0=x_0, x1=x_1,
                fillcolor="LightSalmon", opacity=0.3,
                layer="above", line_width=1,)

        titel = "Interview chronology " + interview_id_detail

    return fig, titel



# Print der einzelnen Sätze des ausgewählten Chunks
@app.callback(
    Output("textarea_detail", "children"),
    Output("sent_title_detail", "children"),
    Output("chunk_number_detail", "data"),
    Input("heat_map_interview_detail", "clickData"),
    Input("-_button_detail", "n_clicks"),
    Input("+_button_detail", "n_clicks"),
    State("chunk_number_detail", "data"),

)
def sent_drawing_detail(clickData, input_before, input_next, chunk_number):
    if ctx.triggered[0]["prop_id"] == "+_button_detail.n_clicks":
        chunk_id = chunk_number +1
    elif ctx.triggered[0]["prop_id"] == "-_button_detail.n_clicks":
        chunk_id = chunk_number -1
    else:
        if tc_indicator_detail:
            time_id = clickData["points"][0]["x"]
            row_index = chronology_df_detail.index.get_loc(chronology_df_detail[chronology_df_detail["minute"] == time_id].index[0]) # die Information aus dem DF aus Chronology. Hier wird die Zeit und das zugehörige DF gespeichert. Wir müssen zunächst den Index der Zeitangabe finden
            chunk_id = chronology_df_detail.loc[row_index]["ind"] # mit dem Index der Zeitangabe kann hier der Chunkwert ausgelesen werden und als chunk_id übergeben werden
        else:
            chunk_id = clickData["points"][0]["x"]

    sent_example = []
    speaker = "None"
    for a in top_dic["corpus"][interview_id_detail[0:3]][interview_id_detail]["sent"]:
        if top_dic["corpus"][interview_id_detail[0:3]][interview_id_detail]["sent"][a]["chunk"] == int(chunk_id):
            if speaker == top_dic["corpus"][interview_id_detail[0:3]][interview_id_detail]["sent"][a]["speaker"]:
                sent_example.append(top_dic["corpus"][interview_id_detail[0:3]][interview_id_detail]["sent"][a]["raw"] + ". ")
            else:
                sent_example.append("\n" + "*" + top_dic["corpus"][interview_id_detail[0:3]][interview_id_detail]["sent"][a]["speaker"] + "*: ")
                sent_example.append(top_dic["corpus"][interview_id_detail[0:3]][interview_id_detail]["sent"][a]["raw"] + ". ")
                speaker = top_dic["corpus"][interview_id_detail[0:3]][interview_id_detail]["sent"][a]["speaker"]

    sent_id = "Chunk: " + str(int(chunk_id))

    return sent_example, sent_id, chunk_id

@app.callback(
    Output("topic_table", "children"),
    Input("word_number", "value"),
    Input("enter_print_topics", "n_clicks"),
)
def print_all_topics(words, nClicks):
    if ctx.triggered[0]["prop_id"] == "enter_print_topics.n_clicks":
        number_of_words = words
        data=[]
        for topic in top_dic["words"]:
            data_topic = []
            out_line = []
            for i in range(number_of_words):
                out_line.append((top_dic["words"][topic])[i][1] + ", ")
            data_topic =(topic, out_line)
            data.append(data_topic)

        df = pd.DataFrame(data)
        df.columns = ["Topic", "Words"]
        table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, color="dark", responsive=True, )

        return table

@app.callback(
    Output("correlation_output", "children"),
    Input("correlation_switch", "value"),
    Input("gross_nr_correlations_per_chunk_pagination", "active_page")
)
def print_top_correlation(switch, gross_nr_correlations_per_chunk):
    if switch == 1:
        data = top_global_correlations_json(top_dic, 30, horizontal=True, gross_nr_correlations_per_chunk = gross_nr_correlations_per_chunk)
        return_data = []
        for line in data:
            return_data.append(str(line) + "\n")
        return return_data
    if switch == 2:
        data = top_global_correlations_json(top_dic, 30, vertical=True, gross_nr_correlations_per_chunk= gross_nr_correlations_per_chunk)
        return_data = []
        for line in data:
            return_data.append(str(line) + "\n")
        return return_data

@app.callback(
    Output("slct_archiv", "options"),
    Input("top_dic", "data2")
)
def creat_global_dropdown(data2):
    print("worked")
    drop_down_menu = []
    for archives in top_dic["corpus"]:
        a = {"label": archives, "value": archives}
        drop_down_menu.append(a)

    drop_down_menu.append({"label": "Gesamtkorpus", "value": "all"})
    return drop_down_menu



if __name__ == '__main__':
    app.run_server(debug=False, port=3002)