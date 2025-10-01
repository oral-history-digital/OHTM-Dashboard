import json
import pandas as pd
import plotly.express as px
import warnings
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go

warnings.simplefilter(action='ignore', category=FutureWarning)

force_chunk_nr_as_x_axis = False

# Load labels
# for the creation of custom labels use write_labels.py
# WARNING! Existing labels in the ohtm-file will be permanently overwritten!
# @Philipp: mit read_labels.py können die vorläufigen label-jsons geprüft werden
# @Philipp: Händisches Clustering -> Liste in Funktion übergeben und eigenen Schalter einfügen -
# jetzt läuft es über den Topic Filter, der unten auskommentiert ist

#label_folder = "C:\\Users\\moebusd\\sciebo\\OHD\\Data TM OHD\\"
#import_labels = 'ohd_final_100c_100t_A5'

#with open(label_folder+import_labels+'_labels.json') as f:
#    labels = json.load(f)



# functions for time code manipulation

def timecode_to_frames(tc, framerate):
    if len(tc) > 8:
        minutes = int(tc[:2]) * 60
        seconds = (minutes + int(tc[3:5])) * 60
        frames = (seconds + int(tc[6:8])) * framerate + int(tc[9:])
        return frames
    if len(tc) == 8:
        minutes = int(tc[:2]) * 60
        seconds = (minutes + int(tc[3:5])) * 60
        frames = (seconds + int(tc[6:8])) * framerate
        return frames

def frames_to_timecode(frames, framerate):
    tc_fr = int(frames % framerate)
    if tc_fr < 10:
        tc_fr = '0' + str(tc_fr)
    tc_s = int((frames / framerate) % 60)
    if tc_s < 10:
        tc_s = '0' + str(tc_s)
    tc_m = int(frames / framerate / 60 % 60)
    if tc_m < 10:
        tc_m = '0' + str(tc_m)
    tc_h = int(frames / framerate / 60 / 60)
    if tc_h < 10:
        tc_h = '0' + str(tc_h)

    return str(tc_h) + ':' + str(tc_m) + ':' + str(tc_s) + '.' + str(tc_fr)

# creation of the main chronology visualization

def chronology_matrix(data,
                      click_data,
                      click_data_2,
                      ctx_triggered,
                      chunk_number_storage,
                      heatmap_filter: list = "",
                      interview_manual_id: str= "",
                      return_data: bool = False,
                      threshold_top_filter: float=0,
                      outlier_threshold: float=0,
                      options:list = "",
                      ):

    interview_id = None
    if click_data == "off":
        interview_id = interview_manual_id
    else:
        if interview_manual_id is not None:
            interview_id = interview_manual_id
            if interview_manual_id == '':
                interview_id = click_data["points"][0]["y"]
        else:
            if click_data is not None:
                interview_id = click_data["points"][0]["y"]
            else:
                interview_id = None
    if interview_id is not None:

        if threshold_top_filter is None:
            threshold_top_filter = 0
        if outlier_threshold is None:
            outlier_threshold = 0

        ohtm_file = data

        topic_labels = ohtm_file['topic_labels']['labels']
        clusters = ohtm_file['topic_labels']['clusters']

        if type(ohtm_file) is not dict:
            ohtm_file = json.loads(ohtm_file)
        else:
            ohtm_file = ohtm_file

        if "z_score" in heatmap_filter:
            z_score = True
        else:
            z_score = False

        if "filter" in heatmap_filter:
            topic_filter = True
        else:
            topic_filter = False

        interview_id = str(interview_id)
        # print(interview_id)
        archive_id = str(interview_id)[:3]
        dff = []
        chunk_counter = 0
        chunk_set = 0
        transfer = []
        threshold_top_filter = threshold_top_filter # @Philipp ggf. als Regler
        outlier_threshold = outlier_threshold # @Philipp ggf. als Regler
        top_filter = []

        for archive in ohtm_file["corpus"]:
            if interview_id in ohtm_file["corpus"][archive]:
                archive_id = archive

        for sents in ohtm_file["corpus"][archive_id][interview_id]["sent"]:

            if ohtm_file["corpus"][archive_id][interview_id]["sent"][sents]["chunk"] == chunk_set:
                transfer.append([ohtm_file["corpus"][archive_id][interview_id]["sent"][sents]["tape"],
                                 ohtm_file["corpus"][archive_id][interview_id]["sent"][sents]["time"],
                                 ohtm_file["corpus"][archive_id][interview_id]["sent"][sents]["speaker"],
                                 ohtm_file["corpus"][archive_id][interview_id]["sent"][sents]["raw"],
                                 ohtm_file["corpus"][archive_id][interview_id]["sent"][sents]["chunk"]])
            if ohtm_file["corpus"][archive_id][interview_id]["sent"][sents]["chunk"] != chunk_set:
                dff.append(transfer)
                chunk_set += 1
                transfer = []
                transfer.append([ohtm_file["corpus"][archive_id][interview_id]["sent"][sents]["tape"],
                                 ohtm_file["corpus"][archive_id][interview_id]["sent"][sents]["time"],
                                 ohtm_file["corpus"][archive_id][interview_id]["sent"][sents]["speaker"],
                                 ohtm_file["corpus"][archive_id][interview_id]["sent"][sents]["raw"],
                                 ohtm_file["corpus"][archive_id][interview_id]["sent"][sents]["chunk"]])
        dff.append(transfer)

        # add timecodes of subsequent tapes for complete interview chronology
        try:
            if type(dff[0][0][1]) is not str or force_chunk_nr_as_x_axis:
                # print('No Timecode for X-Axis available, using index-nr of chunks')
                dff_2 = dff
                tc_indicator = False

            else:
                tape_counter = 1
                dff_2 = []
                time_set = 0
                tc_indicator = True
                for chunk in dff:
                    # print(chunk)
                    transfer_segments = []
                    for segment in chunk:
                        # print(segment)
                        if tape_counter == int(segment[0]):
                            x = frames_to_timecode(timecode_to_frames(segment[1], 24) + time_set, 24)
                            transfer_segments.append([segment[0], x, segment[2], segment[3], segment[4]])
                        if tape_counter != int(segment[0]):
                            tape_counter += 1
                            time_set = timecode_to_frames(x, 24)
                            x = frames_to_timecode(timecode_to_frames(segment[1], 24) + time_set, 24)
                            transfer_segments.append([segment[0], x, segment[2], segment[3], segment[4]])
                    dff_2.append(transfer_segments)
        except IndexError:  # some transcripts may be empty
            return 'Transkript leer'

        # print(dff_2)

        #calculating word density and locating speaker changes

        results_worddensity = []
        results_speaker_diffusion = []

        # find all speakers

        speakers = []

        for chunk in dff_2:
            for segment in chunk:
                if type(segment[2]) is not str:
                    continue
                # print(segment)
                if segment[2] not in speakers:  # and segment[2] != '#'
                    speakers.append(segment[2])
                else:
                    continue
        # print(speakers)

        # calculate speakers amount
        for chunk in dff_2:
            speakerdiffusion = []
            for speaker in speakers:
                count = 0
                for segment in chunk:
                    # print(segment)
                    if segment[2] == speaker:
                        count += len(str(segment[3]).split(' '))
                speakerdiffusion.append(count)
            results_speaker_diffusion.append(speakerdiffusion)
        # print(results_speaker_diffusion)

        final_results_speaker_diffusion = []
        wordcount = []
        for chunk in results_speaker_diffusion:
            counter = 0
            for count in chunk:
                counter += count
            wordcount.append(counter)

        for i, count in enumerate(results_speaker_diffusion):
            # print(wordcount[i])
            if tc_indicator:
                for j, speaker in enumerate(count):
                    try:
                        final_results_speaker_diffusion.append(
                            [speakers[j], timecode_to_frames(dff_2[i][-1][1], 24) / 24 / 60, speaker / wordcount[i], i])
                    except ZeroDivisionError:
                        final_results_speaker_diffusion.append(
                            [speakers[j], timecode_to_frames(dff_2[i][-1][1], 24) / 24 / 60, 1, i])
            else:
                for j, speaker in enumerate(count):
                    try:
                        final_results_speaker_diffusion.append([speakers[j], i, speaker / wordcount[i]])
                    except ZeroDivisionError:
                        final_results_speaker_diffusion.append([speakers[j], i, 1])

        # calculate word frequency
        if tc_indicator:
            for i, chunk in enumerate(dff_2):
                time = (timecode_to_frames(chunk[-1][1], 24) - timecode_to_frames(chunk[0][1], 24)) / 24
                try:
                    wordfreq = wordcount[i] / time
                    results_worddensity.append(['worddensity', timecode_to_frames(chunk[-1][1], 24) / 24 / 60, wordfreq, i])
                except ZeroDivisionError:
                    results_worddensity.append(['worddensity', timecode_to_frames(chunk[-1][1], 24) / 24 / 60, 1, i])

        # parse and calculate topic weights from ohtm-file

        topicweights = []

        if "topic_cluster_on" in options and ohtm_file["settings"]["labeling_options"]["clustering"] == True:
            if tc_indicator:
                for nr, chunk in enumerate(dff_2):
                    for nr_c, cluster in enumerate(clusters):
                        transfer = 0
                        for top in cluster[0][1]:
                            transfer += ohtm_file["weight"][archive_id][interview_id][str(chunk[0][4])][str(top)]
                        topicweights.append([cluster[0], timecode_to_frames(chunk[-1][1], 24)/24/60, transfer, nr])  #transfer/len(cluster)
            else:
                for nr, chunk in enumerate(dff_2):
                    for nr_c, cluster in enumerate(clusters):
                        transfer = 0
                        for top in cluster[1]:
                            transfer += ohtm_file["weight"][archive_id][interview_id][str(chunk[0][4])][str(top)]
                        topicweights.append([cluster[0],nr , transfer])#

        # filter for a reduced and more consistent heatmap - topics below a certain threshold will be filtered out

        else:
            find_max = {}
            heat_dic = {}
            count = 0
            for c in ohtm_file["weight"][archive_id][interview_id]:
                count += 1
                for t in ohtm_file["weight"][archive_id][interview_id][c]:
                    if t not in heat_dic:
                        heat_dic.update({t: ohtm_file["weight"][archive_id][interview_id][c][
                        t]})  # das int(t) muss genutzt werden, da das speichern in Store die Datei umwandelt
                        find_max.update({t: ohtm_file["weight"][archive_id][interview_id][c][t]})

                    else:
                        heat_dic.update({t: heat_dic[t] + ohtm_file["weight"][archive_id][interview_id][c][t]})
                        if ohtm_file["weight"][archive_id][interview_id][c][
                        t] > find_max[t]:
                            find_max.update({t: ohtm_file["weight"][archive_id][interview_id][c][t]})
                        else:
                            continue

            for key, val in heat_dic.items():
                heat_dic.update({key: heat_dic[key] / count})
                if heat_dic[key] < threshold_top_filter:
                    top_filter.append(key)
            #print(top_filter)

            for key, val in find_max.items():
                if find_max[key] < outlier_threshold and key not in top_filter:
                    top_filter.append(key)
            #print(top_filter)

            topicweights = []

            if tc_indicator:
              for nr, chunk in enumerate(dff_2):
                for top in ohtm_file["weight"][archive_id][interview_id][str(chunk[0][4])]:
                    if top not in top_filter:
                        # topicweights.append([str(top) + ' ' + str([word[1] for word in top_dic["words"][top][:10]]), timecode_to_frames(chunk[-1][1], 24)/24/60, top_dic["weight"][interview_id[0:3]][interview_id][str(chunk[0][4])][top], nr])
                        topicweights.append([topic_labels[top], timecode_to_frames(chunk[-1][1], 24)/24/60, ohtm_file["weight"][archive_id][interview_id][str(chunk[0][4])][top], nr])

                    else:
                        continue

              #print(topicweights[1])
            else:
              for nr, chunk in enumerate(dff_2):
                for top in ohtm_file["weight"][archive_id][interview_id][str(chunk[0][4])]:
                  #print(chunk[0][4])
                  if top not in top_filter:
                    # topicweights.append([str(top) + ' ' + str([word[1] for word in top_dic["words"][top][:10]]),nr , top_dic["weight"][interview_id[0:3]][interview_id][str(chunk[0][4])][top]])
                    topicweights.append([topic_labels[top] ,nr , ohtm_file["weight"][archive_id][interview_id][str(chunk[0][4])][top]])
                  else:
                    continue
              #print(topicweights[1])

        if tc_indicator:
            chronology_df = pd.DataFrame(topicweights, columns=['top', 'minute', 'weight',
                                                             'ind'])
        if tc_indicator == False:
            chronology_df = pd.DataFrame(topicweights, columns=['top', 'chunk', 'weight'])

        if return_data:
            chronology_list = chronology_df.values.tolist()
            #print(chronology_list[0])
            return chronology_list

        fig_final = make_subplots(rows=3, cols=1)

        # chronology heatmap
        if tc_indicator:
            df_heatmap = pd.DataFrame(topicweights, columns=['top', 'minute', 'weight',
                                                             'ind'])  # kann man bei Timecode auf X-Achse Chunk-Nr. ins Hover schreiben? - ist in der Tabelle schon als "ind"
            doc_tops_heatmap = df_heatmap.pivot(index = "top", columns = "minute", values = "weight")

            if z_score == True:
                # Berechnung der z-Standardisierung
                mean = doc_tops_heatmap.mean()
                std_dev = doc_tops_heatmap.std()
                z_scores = ((doc_tops_heatmap - mean) / std_dev)

                doc_tops_heatmap = z_scores

        else:
            df_heatmap = pd.DataFrame(topicweights, columns=['top', 'chunk', 'weight'])
            doc_tops_heatmap = df_heatmap.pivot(index = "top", columns = "chunk", values = "weight")

            if z_score == True:
                # Berechnung der z-Standardisierung
                mean = doc_tops_heatmap.mean()
                std_dev = doc_tops_heatmap.std()
                z_scores = ((doc_tops_heatmap - mean) / std_dev)

                doc_tops_heatmap = z_scores

        fig_final.add_trace(go.Heatmap(z=doc_tops_heatmap, x=doc_tops_heatmap.columns, y=doc_tops_heatmap.index), row=1, col=1)
        fig_final.update_xaxes(visible=False, showticklabels=False, row=1, col=1)
        fig_final.update_yaxes(visible=True, showticklabels=True, type = "category", row=1, col=1) # type = "category": equal y-axis ticks bei uneven number steps

        # speaker chronology
        if tc_indicator:
            df_heatmap = pd.DataFrame(final_results_speaker_diffusion, columns=['top', 'minute', 'weight', 'ind'])
            doc_tops_heatmap = df_heatmap.pivot(index = "top", columns = "minute", values = "weight")
        else:
            df_heatmap = pd.DataFrame(final_results_speaker_diffusion, columns=['top', 'chunk', 'weight'])
            doc_tops_heatmap = df_heatmap.pivot(index = "top", columns= "chunk", values = "weight")
        fig_final.add_trace(go.Heatmap(z=doc_tops_heatmap, x=doc_tops_heatmap.columns, y=doc_tops_heatmap.index), row=2,col=1)
        fig_final.update_xaxes(visible=True, showticklabels=True, row=2,col=1)
        if tc_indicator:
            fig_final.update_xaxes(visible=False, showticklabels=False, row=2, col=1)
        fig_final.update_yaxes(visible=True, showticklabels=True, row=2,col=1)
        # fig_final.update(layout_coloraxis_showscale=False, row=2,col=1)

        #worddensity
        if tc_indicator:
            df_heatmap = pd.DataFrame(results_worddensity, columns=['top', 'minute', 'weight', 'ind'])
            doc_tops_heatmap = df_heatmap.pivot(index = "top", columns = "minute", values = "weight")
            fig = px.imshow(doc_tops_heatmap, color_continuous_scale='dense',
                            aspect='auto')
            fig.update_xaxes(visible=False, showticklabels=False)
            fig.update_yaxes(visible=False, showticklabels=False)
            fig.update(layout_coloraxis_showscale=False)
            fig_final.add_trace(go.Heatmap(z=doc_tops_heatmap, x=doc_tops_heatmap.columns, y=doc_tops_heatmap.index), row=3,col=1)
            fig_final.update_xaxes(visible=True, showticklabels=True, row=3,col=1)
            fig_final.update_yaxes(visible=False, showticklabels=False, row=3,col=1)


        fig_final.update_traces(hovertemplate="Chunk: %{x}" "<br>Topic: %{y}" "<br>Weight: %{z}<extra></extra>", row=1,
                                col=1)
        if tc_indicator:
            fig_final.update_traces(hovertemplate="Time: %{x}" "<br>Topic: %{y}" "<br>Weight: %{z}<extra></extra>", row=1,
                                    col=1)
        fig_final.update_traces(hovertemplate="Chunk: %{x}" "<br>Speaker: %{y} <extra></extra>" "<br>Weight: %{z}<extra>", row=2, col=1)
        if tc_indicator:
            fig_final.update_traces(hovertemplate="Time: %{x}" "<br>Speaker: %{y} <extra></extra>" "<br>Weight: %{z}<extra>", row=2, col=1)
        fig_final.update_traces(hovertemplate="Worddensity: %{x} <extra>", row=3, col=1)
        fig_final.update_traces(colorscale="dense")
        fig = fig_final
        fig['layout']['yaxis1'].update(domain=[0.16, 1.0])
        fig['layout']['yaxis2'].update(domain=[0.05, 0.15])
        fig['layout']['yaxis3'].update(domain=[0.0, 0.04])
        fig.update_traces(showlegend=False)
        fig.update_traces(showscale = False)
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
        if ctx_triggered[0]["prop_id"] == "heat_map.clickData":
            title = "Interview " + interview_id
        elif ctx_triggered[0]["prop_id"] == "interview_manual_id.value":
            title = "Interview " + interview_id
        elif ctx_triggered[0]["prop_id"] == "interview_manual_id_detail.value":
            title = "Interview " + interview_manual_id
        else:
            if "marker" in heatmap_filter:
                if tc_indicator:

                    row_index_clicked = chronology_df.index.get_loc(
                        chronology_df[chronology_df["minute"] == click_data_2["points"][0]["x"]].index[0])
                    chunk_number_clicked = chronology_df.loc[row_index_clicked]["ind"]

                    if chunk_number_clicked == 0:
                        row_index = chronology_df.index.get_loc(
                            chronology_df[chronology_df["ind"] == chunk_number_clicked].index[0])
                        time_id = chronology_df.loc[row_index]["minute"]
                        row_index_after = chronology_df.index.get_loc(
                            chronology_df[chronology_df["ind"] == chunk_number_clicked + 1].index[0])
                        time_id_after = chronology_df.loc[row_index_after]["minute"]

                        x_1 = (time_id + time_id_after) / 2
                        x_0 = x_1 - time_id


                    elif chunk_number_clicked == chronology_df["ind"][chronology_df.index[-1]]:
                        row_index = chronology_df.index.get_loc(
                            chronology_df[chronology_df["ind"] == chunk_number_clicked].index[0])
                        time_id = chronology_df.loc[row_index]["minute"]
                        row_index_before = chronology_df.index.get_loc(
                            chronology_df[chronology_df["ind"] == chunk_number_clicked - 1].index[0])
                        time_id_before = chronology_df.loc[row_index_before]["minute"]

                        x_0 = (time_id + time_id_before) / 2
                        x_1 = time_id + (time_id - x_0)

                    else:
                        row_index = chronology_df.index.get_loc(
                            chronology_df[chronology_df["ind"] == chunk_number_clicked].index[0])
                        time_id = chronology_df.loc[row_index]["minute"]
                        row_index_before = chronology_df.index.get_loc(
                            chronology_df[chronology_df["ind"] == chunk_number_clicked - 1].index[0])
                        time_id_before = chronology_df.loc[row_index_before]["minute"]
                        row_index_after = chronology_df.index.get_loc(
                            chronology_df[chronology_df["ind"] == chunk_number_clicked + 1].index[0])
                        time_id_after = chronology_df.loc[row_index_after]["minute"]

                        x_0 = (time_id + time_id_before) / 2
                        x_1 = (time_id + time_id_after) / 2

                else:
                    x_0 = click_data_2["points"][0]["x"] - 0.5
                    x_1 = click_data_2["points"][0]["x"] + 0.5

                if ctx_triggered[0]["prop_id"] == "chunk_number_frontpage.data" or "chunk_number_detail.data":
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
                            row_index = chronology_df.index.get_loc(
                                chronology_df[chronology_df["ind"] == chunk_number_storage].index[0])
                            time_id = chronology_df.loc[row_index]["minute"]
                            row_index_before = chronology_df.index.get_loc(
                                chronology_df[chronology_df["ind"] == chunk_number_storage - 1].index[0])
                            time_id_before = chronology_df.loc[row_index_before]["minute"]
                            row_index_after = chronology_df.index.get_loc(
                                chronology_df[chronology_df["ind"] == chunk_number_storage + 1].index[0])
                            time_id_after = chronology_df.loc[row_index_after]["minute"]
                            x_0 = (time_id + time_id_before) / 2
                            x_1 = (time_id + time_id_after) / 2
                    else:
                        x_0 = chunk_number_storage - 0.5
                        x_1 = chunk_number_storage + 0.5

                fig.add_vrect(
                    x0=x_0, x1=x_1,
                    fillcolor="LightSalmon", opacity=0.3,
                    layer="above", line_width=1, )
            title = "Interview " + interview_id
        doc_tops_heatmap = chronology_df.to_json()  # dash only can store json, so this df has to be converted
        return fig, title, interview_id, chunk_number_storage, tc_indicator, doc_tops_heatmap
    else:
        None


#chronology_matrix(input, data)