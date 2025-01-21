"""
chunk_number_detail
"""
from dash import ctx


def heatmap_marker_creation_normal(clickData_2, chunk_number_storage):
    x_0 = int(clickData_2["points"][0]["x"]) - 0.5
    x_1 = int(clickData_2["points"][0]["x"]) + 0.5

    if ctx.triggered[0]["prop_id"] == "chunk_number_frontpage.data":
        x_0 = int(chunk_number_storage) - 0.5
        x_1 = int(chunk_number_storage) + 0.5
    elif ctx.triggered[0]["prop_id"] == "chunk_number_detail.data":
        x_0 = int(chunk_number_storage) - 0.5
        x_1 = int(chunk_number_storage) + 0.5

    return x_0, x_1


def heatmap_marker_creation_chronic(chronology_df_detail, heatmap_filter, tc_indicator_detail, clickData_2, chunk_number_storage):
    if "mark" in heatmap_filter:
        if tc_indicator_detail:

            row_index_clicked = chronology_df_detail.index.get_loc(
                chronology_df_detail[chronology_df_detail["minute"] == clickData_2["points"][0]["x"]].index[0])
            chunk_number_clicked = chronology_df_detail.loc[row_index_clicked]["ind"]

            if chunk_number_clicked == 0:
                row_index = chronology_df_detail.index.get_loc(
                    chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked].index[0])
                time_id = chronology_df_detail.loc[row_index]["minute"]
                row_index_after = chronology_df_detail.index.get_loc(
                    chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked + 1].index[0])
                time_id_after = chronology_df_detail.loc[row_index_after]["minute"]

                x_1 = (time_id + time_id_after) / 2
                x_0 = x_1 - time_id

            elif chunk_number_clicked == chronology_df_detail["ind"][chronology_df_detail.index[-1]]:
                row_index = chronology_df_detail.index.get_loc(
                    chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked].index[0])
                time_id = chronology_df_detail.loc[row_index]["minute"]
                row_index_before = chronology_df_detail.index.get_loc(
                    chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked - 1].index[0])
                time_id_before = chronology_df_detail.loc[row_index_before]["minute"]

                x_0 = (time_id + time_id_before) / 2
                x_1 = time_id + (time_id - x_0)

            else:
                row_index = chronology_df_detail.index.get_loc(
                    chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked].index[0])
                time_id = chronology_df_detail.loc[row_index]["minute"]
                row_index_before = chronology_df_detail.index.get_loc(
                    chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked - 1].index[0])
                time_id_before = chronology_df_detail.loc[row_index_before]["minute"]
                row_index_after = chronology_df_detail.index.get_loc(
                    chronology_df_detail[chronology_df_detail["ind"] == chunk_number_clicked + 1].index[0])
                time_id_after = chronology_df_detail.loc[row_index_after]["minute"]

                x_0 = (time_id + time_id_before) / 2
                x_1 = (time_id + time_id_after) / 2

        else:
            x_0 = clickData_2["points"][0]["x"] - 0.5
            x_1 = clickData_2["points"][0]["x"] + 0.5

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

                    row_index = chronology_df_detail.index.get_loc(
                        chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage].index[0])
                    time_id = chronology_df_detail.loc[row_index]["minute"]
                    row_index_before = chronology_df_detail.index.get_loc(
                        chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage - 1].index[0])
                    time_id_before = chronology_df_detail.loc[row_index_before]["minute"]
                    row_index_after = chronology_df_detail.index.get_loc(
                        chronology_df_detail[chronology_df_detail["ind"] == chunk_number_storage + 1].index[0])
                    time_id_after = chronology_df_detail.loc[row_index_after]["minute"]

                    x_0 = (time_id + time_id_before) / 2
                    x_1 = (time_id + time_id_after) / 2

            else:
                x_0 = chunk_number_storage - 0.5
                x_1 = chunk_number_storage + 0.5
