from settings_OHDdash import *

global top_dic
global chronology_df
load_file_name = "ohd_complete_lemmetized_pos_off_75c_80t"
#load_file_name = "OHD_auswahl_pre_150c_80t"

with open(workingfolder + load_file_name) as f:
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
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
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


        html.P(id='placeholder'),
        html.Img(src=b64_image(image_filename), style={"max-width": "100%"}),
        html.Hr(id="dummy", children=[]),
        dbc.Nav(
            [
                dbc.NavLink("Dash-Board", href="/", active="exact"),
                dbc.NavLink("Text Search", href="/page-1", active="exact"),
                dbc.NavLink("Balkendiagram", href="/page-2", active="exact"),
                dbc.NavLink("Chronology Heamtap", href="/page-3", active="exact"),
                dbc.NavLink("Topic Übersicht", href="/page-4", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
        dbc.Row(html.Hr()),
        dbc.Row([
            html.H5(dbc.Badge("Topic Wortliste", color="danger"))
        ]),
        dbc.Row([
            dbc.Input(id="input", placeholder="Topic Nummer eingeben", type="number",
                      min=0, max=100 - 1, step=1
                      )
        ]),
        dbc.Row([
            html.Div(id="topics")
        ]),
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
                    dcc.Dropdown(id="slct_archiv",
                                 options=[
                                     {"label": "Archiv Zwangsarbeit", "value": "ZWA"},
                                     {"label": "Archiv Deutsches Gedächtnis", "value": "ADG"},
                                     {"label": "Werkstatt der Erinnerung", "value": "WdE"},
                                     {"label": "Museum Friedland", "value": "MFL"},
                                     {"label": "Flucht Vertreibung Versöhnung", "value": "FVV"},
                                     {"label": "Hannah-Arendt-Institut", "value": "HAI"},
                                     {"label": "Gesamtkorpus", "value": "all"},
                                 ],
                                 multi=False,
                                 value="all",
                                 style={'width': "80%"}
                                 )], width=4),
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
                    html.H5([dbc.Badge(id="interview_titel", color="danger")], className="text-center")
                ], width=6),
                dbc.Col([

                    dbc.Button("<", id="-_button_frontpage", color="danger", size="sm"),

                    dbc.Badge("chunk", id="sent_titel", color="danger"),

                    dbc.Button(">", id="+_button_frontpage", color="danger", size = "sm")
                ], className ="d-grid gap-2 d-md-block",
                     width = 6),
                dbc.Row([
                    dbc.Col([
                        dbc.Checklist(
                            options=[
                                {"label": "Topic Filter", "value": "filter"},
                                {"label": "Z Score", "value": "z_score"}
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
                        html.Div(id='textarea', style={'whiteSpace': 'pre-line'}),
                    ]),
                ], width=5),
            ]),

        ]

    elif pathname == "/page-1":
        return [

                html.Div(id="text", children='Enter Topic Number and weight Value'),
                html.Div(dcc.Input(id='topic_print', placeholder="topic", type='number')),
                html.Div(dcc.Input(id='weight_print', placeholder="weight", type='number')),
                html.Button("print", id='enter_print'),
                dash_table.DataTable(
                    id="output_df",
                    style_as_list_view=True,
                        style_cell={'textAlign': 'left'},
                    css=[{
                        'selector': '.dash-spreadsheet td div',
                        'rule': '''
                                    line-height: 15px;
                                    max-height: 30px; min-height: 30px; height: 30px;
                                    display: block;
                                    overflow-y: hidden;
                                '''
                    }],
                ),
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
                    html.H5([dbc.Badge(id="interview_titel_detail", color="danger")], className="text-center")
                ], width=6),
                dbc.Col([
                    html.H5([dbc.Badge(id="sent_titel_detail", color="danger")], className="text-center")
                ], width=5),
                dbc.Row([
                    dbc.Col([
                        dbc.Checklist(
                            options=[
                                {"label": "Topic Filter", "value": "filter"},
                                {"label": "Z Score", "value": "z_score"}
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

            ]),
            dbc.Row([
                html.H5([dbc.Badge(id="interview_title_detail", color="danger")], className="text-center")
            ]),
            dbc.Row([
                    dcc.Graph(id='heat_map_interview_detail', figure={}),
            dbc.Row([
                dbc.Col([
                    dbc.Button("<", id="-_button_detail", color="danger", size="sm"),
                    dbc.Badge("chunk", id="sent_title_detail", color="danger", className="text-center"),
                    dbc.Button(">", id="-_button_detail", color="danger", size="sm"),
                 ]),
            ]),
            dbc.Row([
                    html.Div(id='textarea_detail', style={'whiteSpace': 'pre-line'}),
                ]),

            ]),
                ]

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# Heatmap für den gesamten Corpus mit Auswahlmöglichkeit für die einzelnen Archive
@app.callback(
    Output(component_id='heat_map', component_property='figure'),
    Input(component_id='slct_archiv', component_property='value'),
    Input("switch_z_score_global_heatmap", "value")
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
    prevent_initial_call = True

)
def interview_heat_map(clickData, heatmap_filter, top_filter_th, outlier_th, interview_manual_id):
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
    for a in top_dic["korpus"][interview_id[0:3]][interview_id]["sent"]:
        if top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["chunk"] == int(chunk_id):
            if speaker == top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["speaker"]:
                sent_example.append(top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["raw"] + ". ")
            else:
                sent_example.append("\n" + "*" + top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["speaker"] + "*: ")
                sent_example.append(top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["raw"] + ". ")
                speaker = top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["speaker"]

    sent_id = "Chunk: " + str(chunk_id)
    return sent_example, sent_id, chunk_id


# Balkendiagramm auf der ersten Seite
@app.callback(
    Output(component_id="bar", component_property="figure"),
    Input("top_dic", "data2"),
)
def bar_map(data2):
    fig = bar_dic(top_dic, show_fig = False, return_fig = True)
    return fig

# Balkendiagramm auf der dritten Seite
@app.callback(
    Output(component_id="bar2", component_property="figure"),
    Input("top_dic2", "data2"),
    prevent_initial_call=True
)
def bar_map(data2):
    fig = bar_dic(top_dic, show_fig = False, return_fig = True)
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
    prevent_initial_call=True
)
def gloabl_topic_nr_update(clickData):

    topic = clickData["points"][0]["x"]
    return topic

@app.callback(
    Output("heatmap_corpus_topic_nr", "data"),
    Input("heat_map", "clickData"),
    prevent_initial_call=True
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
    print(ctx.triggered)
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
    Output(component_id="output_df", component_property="data"),
    Output(component_id="output_df", component_property='columns'),
    Input("topic_print", "value"),
    Input("weight_print", "value"),
    Input("enter_print", "n_clicks"),
    prevent_initial_call=True
)

def weight_print(topic_print, weight_print, n_clicks):

    if n_clicks is not None:
        sent_final = []
        if n_clicks > 0:
            topic = topic_print
            chunk = weight_print
            for a in top_dic["weight"]:
                for i in top_dic["weight"][a]:
                    for chunks in top_dic["weight"][a][i]:
                        if str(top_dic["weight"][a][i][chunks][str(topic)]) >= str(chunk):
                            sent_current = []
                            sent_current.append(i)
                            for sents in top_dic["korpus"][a][i]["sent"]:
                                int_sent = copy.deepcopy(top_dic["korpus"][a][i]["sent"][sents]["chunk"])
                                if int(int_sent) == int(chunks):
                                    sent_current.append(str(top_dic["korpus"][a][i]["sent"][sents]["raw"]) + " ")
                            sent_current = " ".join(sent_current)
                            sent_current_2 = (str(top_dic["weight"][a][i][chunks][str(topic)]), sent_current)
                            sent_final.append(sent_current_2)
            sent_final.sort(reverse=True)
            df = pd.DataFrame(sent_final)

        df_rounded = df.round(3)
        data = df_rounded.to_dict('records')
        columns = [{"name": i, "id": i} for i in df_rounded.columns]

        return data, columns

# Heatmap Chronology Heatmap Detail
@app.callback(
    Output(component_id='heat_map_interview_detail', component_property='figure'),
    Output("interview_title_detail", "children"),
    Input("switch_chronology_filter_detail", "value"),
    Input("threshold_top_filter_value_detail", "value"),
    Input("outlier_threshold_value_detail", "value"),
    Input("interview_manual_id_detail", "value"),
    prevent_initial_call=True
)
def interview_heat_map(heatmap_filter, top_filter_th, outlier_th, interview_manual_id):

    global chronology_df_detail
    global tc_indicator_detail
    global interview_id_detail

    if "filter" in heatmap_filter:
        topic_filtering = True
    else:
        topic_filtering = False

    if "z_score" in heatmap_filter:
        z_score = True
    else:
        z_score = False

    if top_filter_th == None:
        top_filter_th = 0.01
    if outlier_th == None:
        outlier_th = 0.02


    interview_id_detail = interview_manual_id

    chronology_data = chronology_matrix(top_dic, interview_id_detail, return_fig=True, print_fig=False, z_score=z_score,
                                        topic_filter=topic_filtering, threshold_top_filter=top_filter_th,
                                        outlier_threshold=outlier_th)
    chronology_df_detail = chronology_data[1]
    tc_indicator_detail = chronology_data[2]
    fig = chronology_data[0]
    title = "Interview chronology " + interview_id_detail

    return fig, title

# Print der einzelnen Sätze des ausgewählten Chunks
@app.callback(
    Output(component_id='textarea_detail', component_property='children'),
    Output("sent_title_detail", "children"),
    Output("chunk_number_detail", "data"),
    Input("heat_map_interview_detail", "clickData"),
    Input("-_button_detail", "n_clicks"),
    Input("+_button_detail", "n_clicks"),
    State("chunk_number_detail", "data"),

    prevent_initial_call=True
)
def sent_drawing_detail(clickData, input_before, input_next, chunk_number):
    interview_id = interview_id_detail

    if ctx.triggered[0]["prop_id"] == "+_button_detail.n_clicks":
        chunk_id = chunk_number +1
    elif ctx.triggered[0]["prop_id"] == "-_button_detail.n_clicks":
        chunk_id = chunk_number -1
    else:
        if tc_indicator_detail:
            time_id = clickData["points"][0]["x"]
            row_index = chronology_df_detail.index.get_loc(chronology_df[chronology_df_detail["minute"] == time_id].index[0]) # die Information aus dem DF aus Chronology. Hier wird die Zeit und das zugehörige DF gespeichert. Wir müssen zunächst den Index der Zeitangabe finden
            chunk_id = chronology_df_detail.loc[row_index]["ind"] # mit dem Index der Zeitangabe kann hier der Chunkwert ausgelesen werden und als chunk_id übergeben werden
        else:
            chunk_id = clickData["points"][0]["x"]

    sent_example = []
    speaker = "None"
    for a in top_dic["korpus"][interview_id[0:3]][interview_id]["sent"]:
        if top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["chunk"] == int(chunk_id):
            if speaker == top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["speaker"]:
                sent_example.append(top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["raw"] + ". ")
            else:
                sent_example.append("\n" + "*" + top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["speaker"] + "*: ")
                sent_example.append(top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["raw"] + ". ")
                speaker = top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["speaker"]

    sent_id = "Chunk: " + str(chunk_id)
    return sent_example, sent_id, chunk_id

if __name__ == '__main__':
    app.run_server(debug=False, port=3002)