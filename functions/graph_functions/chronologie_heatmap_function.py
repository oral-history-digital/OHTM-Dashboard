"""
Function will be added later, with Dennis Möbus

"""
# Chronologie Heatmap
#     @app.callback(
#         Output(component_id='heat_map_interview', component_property='figure'),
#         Output("interview_titel", "children"),
#         Input("heat_map", "clickData"),
#         Input("switch_chronology_filter", "value"),
#         Input("threshold_top_filter_value", "value"),
#         Input("outlier_threshold_value", "value"),
#         Input("interview_manual_id", "value"),
#         Input("heat_map_interview", "clickData"),
#         Input("chunk_number_frontpage", "data"),
#         prevent_initial_call=True
#     )
#     def interview_heat_map(clickData, heatmap_filter, top_filter_th, outlier_th,
#                            interview_manual_id,clickData_2, chunk_number_storage):
#         global interview_id
#         global chronology_df
#         global tc_indicator
#
#
#         if "filter" in heatmap_filter:
#             topic_filtering = True
#         else: topic_filtering = False
#
#         if "z_score" in heatmap_filter:
#             z_score = True
#         else: z_score = False
#
#         if top_filter_th == None:
#             top_filter_th = 0.01
#         if outlier_th == None:
#             outlier_th = 0.02
#
#         if interview_manual_id is not None:
#             interview_id = interview_manual_id
#             if interview_manual_id == '':
#                 interview_id = clickData["points"][0]["y"]
#         else:
#             interview_id = clickData["points"][0]["y"]
#
#         # chronology_data = chronology_matrix(ohtm_file, interview_id, return_fig=True, print_fig=False,
#         z_score = z_score, topic_filter = topic_filtering,
#         threshold_top_filter=top_filter_th, outlier_threshold=outlier_th)
#
#         chronology_df = chronology_data[1]
#         tc_indicator = chronology_data[2]
#         fig = chronology_data[0]
#
#         if ctx.triggered[0]["prop_id"] == "heat_map.clickData":
#             titel = "Interview chronology " + interview_id
#         elif ctx.triggered[0]["prop_id"] == "interview_manual_id.value":
#             titel = "Interview chronology " + interview_id
#         else:
#             if "mark" in heatmap_filter:
#                 if tc_indicator:
#
#                     row_index_clicked = chronology_df.index.get_loc(chronology_df[chronology_df["minute"] == clickData_2["points"][0]["x"]].index[0])
#                     chunk_number_clicked = chronology_df.loc[row_index_clicked]["ind"]
#
#                     if chunk_number_clicked == 0:
#                         row_index = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_clicked].index[0])
#                         time_id = chronology_df.loc[row_index]["minute"]
#                         row_index_after = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_clicked + 1].index[0])
#                         time_id_after = chronology_df.loc[row_index_after]["minute"]
#
#                         x_1 = (time_id + time_id_after) / 2
#                         x_0 = x_1 - time_id
#
#
#                     elif chunk_number_clicked == chronology_df["ind"][chronology_df.index[-1]]:
#                         row_index = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_clicked].index[0])
#                         time_id = chronology_df.loc[row_index]["minute"]
#                         row_index_before = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_clicked - 1].index[0])
#                         time_id_before = chronology_df.loc[row_index_before]["minute"]
#
#                         x_0 = (time_id + time_id_before) / 2
#                         x_1 = time_id + (time_id - x_0)
#
#                     else:
#                         row_index = chronology_df.index.get_loc(
#                         chronology_df[chronology_df["ind"] == chunk_number_clicked].index[0])
#                         time_id = chronology_df.loc[row_index]["minute"]
#                         row_index_before = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_clicked - 1].index[0])
#                         time_id_before = chronology_df.loc[row_index_before]["minute"]
#                         row_index_after = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_clicked + 1].index[0])
#                         time_id_after = chronology_df.loc[row_index_after]["minute"]
#
#                         x_0 = (time_id + time_id_before) / 2
#                         x_1 = (time_id + time_id_after) / 2
#
#                 else:
#                     x_0 = clickData_2["points"][0]["x"]-0.5
#                     x_1 = clickData_2["points"][0]["x"]+0.5
#
#                 if ctx.triggered[0]["prop_id"] == "chunk_number_frontpage.data":
#                     if tc_indicator:
#
#                         if chunk_number_storage == 0:
#                             row_index = chronology_df.index.get_loc(
#                                 chronology_df[chronology_df["ind"] == chunk_number_storage].index[0])
#                             time_id = chronology_df.loc[row_index]["minute"]
#                             row_index_after = chronology_df.index.get_loc(
#                                 chronology_df[chronology_df["ind"] == chunk_number_storage + 1].index[0])
#                             time_id_after = chronology_df.loc[row_index_after]["minute"]
#
#                             x_1 = (time_id + time_id_after) / 2
#                             x_0 = x_1 - time_id
#
#
#                         elif chunk_number_storage == chronology_df["ind"][chronology_df.index[-1]]:
#                             row_index = chronology_df.index.get_loc(
#                                 chronology_df[chronology_df["ind"] == chunk_number_storage].index[0])
#                             time_id = chronology_df.loc[row_index]["minute"]
#                             row_index_before = chronology_df.index.get_loc(
#                                 chronology_df[chronology_df["ind"] == chunk_number_storage - 1].index[0])
#                             time_id_before = chronology_df.loc[row_index_before]["minute"]
#
#                             x_0 = (time_id + time_id_before) / 2
#                             x_1 = time_id + (time_id - x_0)
#
#                         else:
#
#                             row_index = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_storage].index[0])
#                             time_id = chronology_df.loc[row_index]["minute"]
#                             row_index_before = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_storage-1].index[0])
#                             time_id_before = chronology_df.loc[row_index_before]["minute"]
#                             row_index_after = chronology_df.index.get_loc(chronology_df[chronology_df["ind"] == chunk_number_storage+1].index[0])
#                             time_id_after = chronology_df.loc[row_index_after]["minute"]
#
#                             x_0 = (time_id+time_id_before)/2
#                             x_1 = (time_id+time_id_after)/2
#
#                     else:
#                         x_0 = chunk_number_storage - 0.5
#                         x_1 = chunk_number_storage + 0.5
#
#
#                 fig.add_vrect(
#                     x0=x_0, x1=x_1,
#                     fillcolor="LightSalmon", opacity=0.3,
#                     layer="above", line_width=1,)
#
#             titel = "Interview chronology " + interview_id
#
#         return fig, titel


# # Heatmap Chronology Heatmap Detail     # Chronologie Heatmap
#     @app.callback(
#         Output(component_id='heat_map_interview_detail', component_property='figure'),
#         Output("interview_title_detail", "children"),
#         Input("interview_manual_id_detail", "value"),
#         Input("switch_chronology_filter_detail", "value"),
#         Input("threshold_top_filter_value_detail", "value"),
#         Input("outlier_threshold_value_detail", "value"),
#         Input("heat_map_interview_detail", "clickData"),
#         Input("chunk_number_detail", "data"),
#
#     )
# def interview_heat_map(interview_manual_id, heatmap_filter, top_filter_th, outlier_th, clickData_2,
#                        chunk_number_storage):
#     global chronology_df_detail
#     global tc_indicator_detail
#     global interview_id_detail
#
#     if "filter" in heatmap_filter:
#         topic_filtering = True
#     else:
#         topic_filtering = False
#
#     if "z_score" in heatmap_filter:
#         z_score = True
#     else:
#         z_score = False
#
#     if top_filter_th == None:
#         top_filter_th = 0.01
#     if outlier_th == None:
#         outlier_th = 0.02
#
#     interview_id_detail = interview_manual_id
#
#     chronology_data = chronology_matrix(ohtm_file, interview_id_detail, return_fig=True, print_fig=False,
#                                         z_score=z_score, topic_filter=topic_filtering,
#                                         threshold_top_filter=top_filter_th, outlier_threshold=outlier_th)
#     chronology_df_detail = chronology_data[1]
#     tc_indicator_detail = chronology_data[2]
#     fig = chronology_data[0]
#
#     if ctx.triggered[0]["prop_id"] == "interview_manual_id_detail.value":
#         titel = "Interview chronology " + interview_id_detail
#     else:
#         if "mark" in heatmap_filter:
#             if tc_indicator_detail:
#
#                 row_index_clicked = chronology_df_detail.index.get_loc(
#                     chronology_df_detail[chronology_df_detail["minute"] == clickData_2["points"][0]["x"]].index[0])
#                 chunk_number_clicked = chronology_df_detail.loc[row_index_clicked]["ind"]
#
#                 if chunk_number_clicked == 0:
#                     row_index = chronology_df_detail.index.get_loc(
#                         chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked].index[0])
#                     time_id = chronology_df_detail.loc[row_index]["minute"]
#                     row_index_after = chronology_df_detail.index.get_loc(
#                         chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked + 1].index[0])
#                     time_id_after = chronology_df_detail.loc[row_index_after]["minute"]
#
#                     x_1 = (time_id + time_id_after) / 2
#                     x_0 = x_1 - time_id
#
#
#                 elif chunk_number_clicked == chronology_df_detail["ind"][chronology_df_detail.index[-1]]:
#                     row_index = chronology_df_detail.index.get_loc(
#                         chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked].index[0])
#                     time_id = chronology_df_detail.loc[row_index]["minute"]
#                     row_index_before = chronology_df_detail.index.get_loc(
#                         chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked - 1].index[0])
#                     time_id_before = chronology_df_detail.loc[row_index_before]["minute"]
#
#                     x_0 = (time_id + time_id_before) / 2
#                     x_1 = time_id + (time_id - x_0)
#
#                 else:
#                     row_index = chronology_df_detail.index.get_loc(
#                         chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked].index[0])
#                     time_id = chronology_df_detail.loc[row_index]["minute"]
#                     row_index_before = chronology_df_detail.index.get_loc(
#                         chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked - 1].index[0])
#                     time_id_before = chronology_df_detail.loc[row_index_before]["minute"]
#                     row_index_after = chronology_df_detail.index.get_loc(
#                         chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked + 1].index[0])
#                     time_id_after = chronology_df_detail.loc[row_index_after]["minute"]
#
#                     x_0 = (time_id + time_id_before) / 2
#                     x_1 = (time_id + time_id_after) / 2
#
#             else:
#                 x_0 = clickData_2["points"][0]["x"] - 0.5
#                 x_1 = clickData_2["points"][0]["x"] + 0.5
#
#             if ctx.triggered[0]["prop_id"] == "chunk_number_detail.data":
#                 if tc_indicator_detail:
#
#                     if chunk_number_storage == 0:
#                         row_index = chronology_df_detail.index.get_loc(
#                             chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage].index[0])
#                         time_id = chronology_df_detail.loc[row_index]["minute"]
#                         row_index_after = chronology_df_detail.index.get_loc(
#                             chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage + 1].index[0])
#                         time_id_after = chronology_df_detail.loc[row_index_after]["minute"]
#
#                         x_1 = (time_id + time_id_after) / 2
#                         x_0 = x_1 - time_id
#
#
#                     elif chunk_number_storage == chronology_df_detail["ind"][chronology_df_detail.index[-1]]:
#                         print("last")
#                         row_index = chronology_df_detail.index.get_loc(
#                             chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage].index[0])
#                         time_id = chronology_df_detail.loc[row_index]["minute"]
#                         row_index_before = chronology_df_detail.index.get_loc(
#                             chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage - 1].index[0])
#                         time_id_before = chronology_df_detail.loc[row_index_before]["minute"]
#
#                         x_0 = (time_id + time_id_before) / 2
#                         x_1 = time_id + (time_id - x_0)
#
#                     else:
#
#                         row_index = chronology_df_detail.index.get_loc(
#                             chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage].index[0])
#                         time_id = chronology_df_detail.loc[row_index]["minute"]
#                         row_index_before = chronology_df_detail.index.get_loc(
#                             chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage - 1].index[0])
#                         time_id_before = chronology_df_detail.loc[row_index_before]["minute"]
#                         row_index_after = chronology_df_detail.index.get_loc(
#                             chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage + 1].index[0])
#                         time_id_after = chronology_df_detail.loc[row_index_after]["minute"]
#
#                         x_0 = (time_id + time_id_before) / 2
#                         x_1 = (time_id + time_id_after) / 2
#
#                 else:
#                     x_0 = chunk_number_storage - 0.5
#                     x_1 = chunk_number_storage + 0.5
#
#             fig.add_vrect(
#                 x0=x_0, x1=x_1,
#                 fillcolor="LightSalmon", opacity=0.3,
#                 layer="above", line_width=1, )
#
#         titel = "Interview chronology " + interview_id_detail
#
#     return fig, titel