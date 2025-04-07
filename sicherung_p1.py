def render_page_content(pathname):
    if pathname == "/":
        return [dbc.Container([
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(id="slct_archiv", options=[],
                                 value="all",
                                 multi=False,
                                 style={"height": "20%", 'width': '70%', 'min-width': '150px', "font-size": "0.8vw"},
                                 placeholder="Corpus"
                                 ),
                ], width=4, style={"display": "flex", "alignItems": "left"}),
                dbc.Col([
                    dbc.Checklist(
                        options=[
                            {"label": "Z Score", "value": "z_score"},
                        ],
                        value=[],
                        id="switch_z_score_global_heatmap",
                        switch=True,
                        style={"width": "100%", "min-width": "150px", "font-size": "0.8vw", "display": "flex"}
                    ),
                ], width=1, style={"display": "flex", "alignItems": "left"})
            ], style={"height": "5vh"}),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='heat_map', figure={}, style={"height": "100%", "width": "100%"},
                              config={"responsive": True})
                ], width=6, style={"display": "flex", "alignItems": "left"}),
                dbc.Col([
                    dcc.Graph(id="bar", figure={}, style={"height": "100%", "width": "100%"},
                              config={"responsive": True})
                ], width=6, style={"display": "flex", "alignItems": "left"}),
            ], style={"height": "45vh"}),
            dbc.Row([
                dbc.Col([
                    html.H5([dbc.Badge(id="interview_titel", color="dark",
                                       style={"width": "100%", "font-size": "0.5vw", "display": "flex"})],
                            className="text-center")
                ], width=6, style={"display": "flex"}),
                dbc.Col([], width=2, style={"display": "flex", "alignItems": "left"}),
                dbc.Col([
                    html.H5([
                        dbc.Button("<", id="-_button_frontpage", color="dark", size="sm",
                                   style={"width": "100%", "font-size": "0.5vw", "display": "flex"}),
                        dbc.Badge("chunk", id="sent_titel", color="dark",
                                  style={"width": "100%", "font-size": "0.5vw", "display": "flex"}),
                        dbc.Button(">", id="+_button_frontpage", color="dark", size="sm",
                                   style={"width": "100%", "font-size": "0.5vw", "display": "flex"})
                    ], style={"display": "flex", "alignItems": "left"}),
                ], width=2, style={"display": "flex", "alignItems": "left"}
                ),
                dbc.Col([], width=2, style={"display": "flex", "alignItems": "left"}),
                dbc.Row([
                    dbc.Col([
                        dbc.Checklist(
                            options=[
                                {"label": "Topic Filter", "value": "filter"},
                                {"label": "Z Score", "value": "z_score"},
                                {"label": "Marker", "value": "marker"}
                            ],
                            value=[],
                            id="switch_chronology_filter",
                            switch=True,
                            inline=True,
                            style={"width": "100%", "min-width": "150px", "font-size": "0.8vw", "display": "flex"}
                        ),
                    ], width=3, style={"display": "flex", "alignItems": "left"}),
                    dbc.Col([
                        html.Div(dbc.Input(id='interview_manual_id', placeholder="Interview", type='word')),
                    ], width=1, style={"display": "flex", "alignItems": "left"}),
                    dbc.Col([
                        html.Div(dbc.Input(id='threshold_top_filter_value',
                                           placeholder="Top Filter Threshold", type='number')),
                    ], width=1, style={"display": "flex", "alignItems": "left"}),
                    dbc.Col([
                        html.Div(dbc.Input(id='outlier_threshold_value', placeholder="Outlier Threshold",
                                           type='number')),
                    ], width=1, style={"display": "flex", "alignItems": "left"})
                ]),
            ], style={"height": "5vh"}),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='heat_map_interview', figure={}, style={"height": "100%", "width": "100%"},
                              config={"responsive": True})
                ], width=6, style={"display": "flex", "alignItems": "left"}),
                dbc.Col([
                    dbc.Row([
                        html.Div(id='textarea',
                                 style={
                                     'whiteSpace': 'pre-line',
                                     'display': 'inline-block',
                                     'height': '45vh',
                                     'display': 'block',
                                     'font-size': "1vm",
                                     'background-color': 'rgb(249,249,249)',
                                     "overflow": "auto",
                                 }),
                    ]),
                ], width=5, style={"display": "flex", "alignItems": "left"}),
            ], style={"height": "45vh"}),
        ], fluid=True)
        ]





# 1. Versuch

return [dbc.Container([
                    dbc.Row([
                        dbc.Col([
                            dbc.Row([

                                    dcc.Dropdown(id="slct_archiv", options=[],
                                                 value="all",
                                                 multi=False,
                                                 style={"height":"20%", 'width': '70%', 'min-width': '150px', "font-size": "0.8vw"},
                                                 placeholder="Corpus"
                                                 ),


                                    dbc.Checklist(
                                        options=[
                                            {"label": "Z Score", "value": "z_score"},
                                        ],
                                        value=[],
                                        id="switch_z_score_global_heatmap",
                                        switch=True,
                                        style={"font-size": "0.8vw", "display": "flex"}
                                                    ),
                            ], style={"display": "flex", "alignItems": "left"}),
                            dbc.Row([

                                    dcc.Graph(id='heat_map', figure={}, style={"height": "100%", "width": "100%"}, config={"responsive": True})
                                    ], style={"display": "flex", "alignItems": "left"}),
                                    ]),

                        dbc.Col([
                            dcc.Graph(id="bar", figure={}, style={"height": "100%", "width": "100%"},
                                      config={"responsive": True})
                        ], style={"display": "flex", "alignItems": "left"}),
                        ], style={"display": "flex", "alignItems": "left"}),
                    dbc.Row([
                        dbc.Col([
                            dbc.Row([
                                    html.H5([dbc.Badge(id="interview_titel", color="dark", style={"width": "100%", "font-size":"0.5vw", "display": "flex"})], className="text-center")
                                ], style={"display": "flex"}),
                            dbc.Row([
                                    dbc.Checklist(
                                        options=[
                                            {"label": "Topic Filter", "value": "filter"},
                                            {"label": "Z Score", "value": "z_score"},
                                            {"label": "Marker", "value": "marker"}
                                        ],
                                        value=[],
                                        id="switch_chronology_filter",
                                        switch=True,
                                        inline=True,
                                        style={"font-size": "0.5vw",
                                               "display": "flex"}),
                                    html.Div(dbc.Input(id='interview_manual_id', placeholder="Interview", type='word', style={"display": "flex"})),
                                    html.Div(dbc.Input(id='threshold_top_filter_value',
                                                       placeholder="Top Filter Threshold", type='number', style={"display": "flex"})),
                                    html.Div(dbc.Input(id='outlier_threshold_value', placeholder="Outlier Threshold",
                                                       type='number', style={"display": "flex"})),
                                ]),
                        dbc.Row([
                                dcc.Graph(id='heat_map_interview', figure={}, style={"height": "100%", "width": "100%"},
                                          config={"responsive": True})
                        ]),
                    ]),
                        # dbc.Col([
                        #     dbc.Row([
                        #         html.H5([
                        #             dbc.Button("<", id="-_button_frontpage", color="dark", size="sm",
                        #                        style={"font-size": "0.5vw", "display": "flex"}),
                        #             dbc.Badge("chunk", id="sent_titel", color="dark",
                        #                       style={"font-size": "0.5vw", "display": "flex"}),
                        #             dbc.Button(">", id="+_button_frontpage", color="dark", size="sm",
                        #                        style={"font-size": "0.5vw", "display": "flex"})
                        #         ], style={"display": "flex", "alignItems": "left"}),
                        #     ]),
                        #     dbc.Row([
                        #
                        #                 html.Div(id='textarea',
                        #                          style={
                        #                              'whiteSpace': 'pre-line',
                        #                              'display': 'inline-block',
                        #                              'height': '45vh',
                        #                              'display': 'block',
                        #                              'font-size': "1vm",
                        #                              'background-color': 'rgb(249,249,249)',
                        #                              "overflow": "auto",
                        #                                 }),
                        #             ]),
                        #         ], style={"display": "flex", "alignItems": "left"}),

                    ]),
            ], fluid=True)
            ]