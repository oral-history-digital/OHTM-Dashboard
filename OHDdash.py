from settings_OHDdash import *

global top_dic
global chronology_df
load_file_name = "OHD_complete_pre_150c_80t.json"
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
        dcc.Store(id="top_dic", data = {}, storage_type ="session"),
        dcc.Store(id="heat_dic", data ={}, storage_type = "session"),
        dcc.Store(id="top_dic2", data = {}, storage_type ="session"),
        dcc.Store(id="data_path", storage_type = "session"),
        html.P(id='placeholder'),
        html.Img(src=b64_image(image_filename), style={"max-width": "100%"}),
        html.Hr(id="dummy", children=[]),
        dbc.Nav(
            [
                dbc.NavLink("Dash-Board", href="/", active="exact"),
                dbc.NavLink("Text Search", href="/page-1", active="exact"),
                dbc.NavLink("Topic-Übersicht", href="/page-2", active="exact"),
                dbc.NavLink("Interview", href="/page-3", active="exact"),
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
                                 )], width=6),
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
                    html.H5([dbc.Badge(id="sent_titel", color="danger")], className="text-center")
                ], width=6),
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='heat_map_interview', figure={})
                ], width=6),
                dbc.Col([
                    dbc.Row([
                        (html.Div(id="sents", children=[], className="box1",
                                  style={
                                      'backgroundColor': '#dee2e6',
                                      'max-height': '400px',
                                      "outline": "2px solid #ff4444",
                                      "border": "4px solid #dee2e6",
                                      'display': 'inline-block',
                                      "overflow": "auto"}
                                  )),
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

                html.Div(id="text", children='Enter a json and press enter'),
                html.Div(dcc.Input(id='json_name', placeholder="enter", type='text')),
                html.Button("enter", id='load_enter'),
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
)
def update_graph(value):
    fig = heatmap_corpus(top_dic, option_selected=str(value), show_fig=False, return_fig=True)
    return fig


# Heatmap: Topic-Verteilung über die einzelnen Chunks eines Interviews
# @app.callback(
#     Output(component_id='heat_map_interview', component_property='figure'),
#     Output("interview_titel", "children"),
#     Input("heat_map", "clickData"),
#
# )
# def interview_heat_map(clickData):
#     global interview_id
#
#     interview_id = clickData["points"][0]["y"]
#     dff = {}
#     for chunks in top_dic["weight"][interview_id[0:3]][interview_id]:
#         dff[chunks] = top_dic["weight"][interview_id[0:3]][interview_id][chunks]
#
#     df = pd.DataFrame.from_dict(dff)
#     df.index = pd.to_numeric(df.index)
#     titel = "Heatmap Interview: " + interview_id
#     fig = px.imshow(df, color_continuous_scale='deep')
#     fig.update_traces(hovertemplate="Chunk: %{x}" "<br>Topic: %{y}" "<br>Weight: %{z}<extra></extra>")
#
#     return fig, titel

@app.callback(
    Output(component_id='heat_map_interview', component_property='figure'),
    Output("interview_titel", "children"),
    Input("heat_map", "clickData"),
)
def interview_heat_map(clickData):
    global interview_id
    global chronology_df

    interview_id = clickData["points"][0]["y"]
    chronology_data = chronology_matrix(top_dic, interview_id)
    chronology_df = chronology_data[1]
    fig = chronology_data[0]
    titel = "Heatmap Interview: " + interview_id
    # fig[0].update_traces(hovertemplate="Chunk: %{x}" "<br>Topic: %{y}" "<br>Weight: %{z}<extra></extra>")

    return fig, titel





# Print der einzelnen Sätze des ausgewählten Chunks
@app.callback(
    Output(component_id='sents', component_property='children'),
    Output("sent_titel", "children"),
    Input("heat_map_interview", "clickData"),
)
def sent_drawing(clickData):

    #chunk_id = clickData["points"][0]["x"]
    time_id = clickData["points"][0]["x"]
    row_index = chronology_df.index.get_loc(chronology_df[chronology_df["minute"] == time_id].index[0]) # die Information aus dem DF aus Chronology. Hier wird die Zeit und das zugehörige DF gespeichert. Wir müssen zunächst den Index der Zeitangabe finden
    chunk_id = chronology_df.loc[row_index]["ind"] # mit dem Index der Zeitangabe kann hier der Chunkwert ausgelesen werden und als chunk_id übergeben werden

    sent_example = []
    speaker = "None"
    for a in top_dic["korpus"][interview_id[0:3]][interview_id]["sent"]:
        if top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["chunk"] == int(chunk_id):
            if speaker == top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["speaker"]:
                sent_example.append(top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["raw"] + ". ")
            else:
                sent_example.append("*" + top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["speaker"] + "*: ")
                sent_example.append(top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["raw"] + ". ")
                speaker = top_dic["korpus"][interview_id[0:3]][interview_id]["sent"][a]["speaker"]

    sent_id = "Chunk: " + str(chunk_id)
    return sent_example, sent_id


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
)
def bar_map(data2):
    fig = bar_dic(top_dic, show_fig = False, return_fig = True)
    return fig

# Ausgabe der ersten 50 Worte des ausgewählten Topics
@app.callback(
    Output("topics", "children"),
    Input("input", "value"),
)
def df_input(value):
    entry = top_words(value, top_dic)
    return entry

@app.callback(
    Output("topics1", "children"),
    Input("input1", "value"),
)
def df_input(value):
    entry = top_words(value, top_dic)
    return entry

@app.callback(
    Output("topics2", "children"),
    Input("input2", "value"),
)
def df_input(value):
    entry = top_words(value, top_dic)
    return entry

@app.callback(
    Output("topics3", "children"),
    Input("input3", "value"),
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


if __name__ == '__main__':
    app.run_server(debug=False, port=3002)