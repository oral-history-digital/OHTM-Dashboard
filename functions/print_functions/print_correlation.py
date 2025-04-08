"""
Will be added later with Dennis Möbus
"""

#
# @app.callback(
#     Output("correlation_output", "children"),
#     Input("correlation_switch", "value"),
#     Input("gross_nr_correlations_per_chunk_pagination", "active_page")
# )
# def print_top_correlation_dash(switch, gross_nr_correlations_per_chunk):
#     if switch == 1:
#         data = top_global_correlations_json(ohtm_file, 30, horizontal=True, gross_nr_correlations_per_chunk = gross_nr_correlations_per_chunk)
#         return_data = []
#         for line in data:
#             return_data.append(str(line) + "\n")
#         return return_data
#     if switch == 2:
#         data = top_global_correlations_json(ohtm_file, 30, vertical=True, gross_nr_correlations_per_chunk= gross_nr_correlations_per_chunk)
#         return_data = []
#         for line in data:
#             return_data.append(str(line) + "\n")
#         return return_data
