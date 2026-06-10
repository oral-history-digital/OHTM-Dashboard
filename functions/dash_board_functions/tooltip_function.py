from dash import html
import dash_bootstrap_components as dbc


def tooltip_creation(trigger):
    if trigger == "/":
        tooltip = html.Div(
            [
                dbc.Tooltip(
                    """Die Übersicht bietet eine detaillierte Analyse der Topic-Modeling-Ergebnisse mithilfe verschiedener Ebenen. Durch die Auswahl von Interviews in der Heatmap können 
                  diese für die Detailansicht ausgewählt werden.""",
                    target="menu_selection_info",
                ),
                # Page 1 - Overview
                dbc.Tooltip(
                    "Die Corpus Heatmap zeigt die Topic-Verteilung pro Interview. Dabei wird ein Durchschnittswert aus allen Chunks gebildet. Durch klicken auf ein Interview kann die Detailansicht ausgewählt werden",
                    target="Corpus_heatmap_page_1_header",
                ),
                dbc.Tooltip(
                    "Das Balkendiagramm zeigt die Verteilung der Topics innerhalb des gesamten Corpus. Die einzelnen Farben repräsentieren die einzelnen Archive",
                    target="bargraph_page_1_header",
                ),
                dbc.Tooltip(
                    "Hier können die einzelnen Sammlungen für die Corpus-Heatmap ausgewählt werden",
                    target="slct_archiv",
                ),
                dbc.Tooltip(
                    "Der Z-Score berechnet eine Standardverteilung der Heatmap, um eine bessere Darstellung zu bekommen.",
                    target="switch_z_score_global_heatmap",
                ),
                dbc.Tooltip(
                    "Zeigt die Chunknummer des ausgewählten Chunks an.",
                    target="sent_titel",
                ),
                dbc.Tooltip(
                    "Schaltet zum vorangehenden Chunk des ausgewählten Interviews.",
                    target="-_button_frontpage",
                ),
                dbc.Tooltip(
                    "Schaltet zum nächsten Chunk des ausgewählten Interviews.",
                    target="+_button_frontpage",
                ),
                dbc.Tooltip(
                    "Geben Sie hier manuell die Interview-ID des Interviews ein, das Sie angezeigt bekommen möchten.",
                    target="interview_manual_id",
                ),
                dbc.Tooltip(
                    "Zeigt die Interview-ID des ausgewählten Interviews an.",
                    target="interview_titel",
                ),
                dbc.Tooltip(
                    "Mit dem Marker können Sie sich den ausgewählten Chunk farblich in der Heatmap anzeigen lassen.",
                    target="switch_chronology_filter"
                ),
            ]
        )
        return tooltip
    if trigger == "/page-6":
        tooltip = html.Div(
            [
                dbc.Tooltip(
                    """Die Chunk-Analyse bietet eine umfangreiche Möglichkeit, die Topic-Verteilung 
                innerhalb der einzelnen Chunks zu analysieren. Darüber hinaus können auch Korrelationen
                mit anderen Topics untersucht werden.
                """,
                    target="menu_selection_info",
                ),
                # Page 2 -Chunk Analyzation
                dbc.Tooltip(
                    "In wie vielen einzelnen Interviews sind Suchergebnisse gefunden worden?",
                    target="interview_results_header",
                ),
                dbc.Tooltip(
                    "Sortiert die Heatmap entweder nach dem Interviewnamen oder den Werten von Topic 1 und Topic 2",
                    target="dropdown_sort",
                ),
                dbc.Tooltip(
                    "Wählen Sie ein Topic aus, indem sie die Nummer eintragen.",
                    target="topic_cv",
                ),
                dbc.Tooltip(
                    "Wählen Sie ein Gewicht aus, über dem das gesuchte Topic 1 liegen soll. Der Wert muss unter 1 liegen.",
                    target="topic_weight_cv",
                ),
                dbc.Tooltip(
                    "Wenn Sie mindestens ein Topic und ein Gewicht ausgewählt haben, drücken Sie auf diesen Button, um die Suche zu starten.",
                    target="start_search_cv",
                ),
                dbc.Tooltip(
                    "Wählen Sie ein zweites Topic aus, um nach einer Korrelation zwischen Topic 1 und 2 zu suchen. Vorher müssen Sie die Korrelation über den Correlation-Button auswählen.",
                    target="topic_2_cv",
                ),
                dbc.Tooltip(
                    "Wählen Sie ein Gewicht aus, über dem das gesuchte Topic 2 liegen soll. Der Wert muss unter 1 liegen.",
                    target="topic_2_weight_cv2",
                ),
                dbc.Tooltip(
                    "Wenn Sie mindestens ein Topic und ein Gewicht ausgewählt haben, drücken sie auf diesen Button, um die Suche zu starten.",
                    target="correlation_cv",
                ),
                dbc.Tooltip(
                    "Die Heatmap zeigt die Topic-Verteilung innerhalb der einzelnen Chunks an.",
                    target="heat_map_cv",
                ),
                dbc.Tooltip(
                    "Das Balkendiagramm zeigt die Gesamtverteilung innerhalb der gefundenen Chunks an.",
                    target="bar_cv",
                ),
                dbc.Tooltip(
                    "Blättert zum vorherigen Chunk des ausgewählten Interviews.",
                    target="-_button_cv",
                ),
                dbc.Tooltip(
                    "Blättert zum nächsten Chunk des ausgewählten Interviews.",
                    target="+_button_cv",
                ),
                dbc.Tooltip(
                    "Zeigt die Interview-ID und den Chunk des ausgewählten Interviews an.",
                    target="interview_titel_cv",
                ),
                dbc.Tooltip(
                    "Zeigt die Topic-Verteilung im ausgwählten Chunk an.",
                    target="chunk_topic_info",
                ),
                dbc.Tooltip(
                    "Zeigt die summierten Top-5-Topics aller gefundenen Chunks an.",
                    target="chunk_topic_info_all",
                ),
                dbc.Tooltip(
                    "Anzahl der gefundenen Chunks.",
                    target="topic_info_cv",
                ),
            ]
        )
        return tooltip
    if trigger == "/page-2":
        tooltip = html.Div(
            [
                dbc.Tooltip(
                    "Das Balkendiagramm bietet eine grafische Darstellung der Topic-Verteilung innerhalb des gesamten Korpus.",
                    target="menu_selection_info",
                ),
                            # Page 3 -Bar Graph
                dbc.Tooltip(
                    "Zeigt die Topic-Verteilung im gesamten Korpus. Die verschiedenen Farben repräsentieren die einzelnen Archive des Korpus.",
                    target="bar2",
                ),
                dbc.Tooltip(
                    "Geben Sie hier eine gewünschte Nummer des Topics ein, das sie näher betrachten möchten. Anschließend werden die ersten 20 Worte des Topics unterhalb ausgegeben.",
                    target="input1",
                ),
                dbc.Tooltip(
                    "Geben Sie hier eine gewünschte Nummer des Topics ein, das sie näher betrachten möchten. Anschließend werden die ersten 20 Worte des Topics unterhalb ausgegeben.",
                    target="input2",
                ),
                dbc.Tooltip(
                    "Geben Sie hier eine gewünschte Nummer des Topics ein, das sie näher betrachten möchten. Anschließend werden die ersten 20 Worte des Topics unterhalb ausgegeben.",
                    target="input3",
                ),
            ]
        )
        return tooltip
    if trigger == "/page-5":
        tooltip = html.Div(
            [
                dbc.Tooltip(
                    "Die Heatmap repräsentiert die Topic-Verteilung über die einzelnen Interviews.",
                    target="menu_selection_info",
                ),
                            # Page 4 -Heatmap
                dbc.Tooltip(
                    "Wählen Sie ein Archiv aus, um die Korpus-Heatmap für dieses Archiv anzuzeigen.",
                    target="slct_archiv_heat_map_corpus_detail",
                ),
                dbc.Tooltip(
                    "Wählen Sie aus, ob Sie den Z-Score für die Heatmap berechnen und anzeigen lassen möchten. Mit 'Topic Filter' können Sie die Funktion aktivieren, nachdem Sie die Interviews nach ausgewählten Topics und ihrem Gewicht filtern.",
                    target="z_score_corpus_heatmap_detail",
                ),
                dbc.Tooltip(
                    "Geben Sie hier die Nummer eines Topics ein, nach welchem Sie die Heatmap filtern möchten. Funktioniert nur bei aktiviertem Filter-Button.",
                    target="corpus_heatmap_detail_topic",
                ),
                dbc.Tooltip(
                    "Geben Sie hier einen Threshold ein, über dem die gefilterten Topics und Interviews angezeigt werden sollen. Funktioniert nur bei aktiviertem Filter-Button.",
                    target="corpus_heatmap_detail_threshold",
                ),
                dbc.Tooltip(
                    "Die Heatmap zeigt die durchschnittliche Topic-Verteilung pro Interview im ausgewählten Korpus an.",
                    target="heat_map_corpus_detail",
                ),
            ]
        )
        return tooltip
    if trigger == "/page-3":
        tooltip = html.Div(
            [
                dbc.Tooltip(
                    "Die Interview Heatmap zeigt die Topic-Verteilung innerhalb eines einzelnen Interviews.",
                    target="menu_selection_info",
                ),
                            # Page 5 - Interview Heatmap
                dbc.Tooltip(
                    "Geben Sie hier die Interview-ID des Interveiws ein, das Sie analysieren möchten.",
                    target="interview_manual_id_detail",
                ),
                dbc.Tooltip(
                    """
                        Mit dem Z-Score-Schalter können sie eine Standardverteilung der Heatmap berechnen lassen, um eine bessere Darstellung zu bekommen. \n
                        Mit dem Marker können Sie den ausgewählten Chunk in der Heatmap hervorheben. \n
                        """,
                    target="switch_chronology_filter_detail",
                ),
                dbc.Tooltip(
                    "Aktivieren Sie den 'Topic Filter' um die Heatmap nach gewissen Schwellenwerten zu filtern.",
                    target="topic_filter_switch_detail",
                ),
                dbc.Tooltip(
                    "Der Threshold bestimmt die Schwelle, oberhalb der Topics in der Heatmap angezeigt werden. Ein höherer Threshold reduziert die angezeigten Topics (Y-Achse).",
                    target="ica_threshold_top_filter",
                ),
                dbc.Tooltip(
                    "Über den Outlier-Threshold kontrolliert man die Schwelle für Topics, die insgesamt wenig Gewicht im Interviewverlauf haben, aber in einzelnen Chunks stark vertreten sind. Mit einem niedrigen Outlier-Threshold können solche unterrepräsentierten Topics angezeigt werden.",
                    target="ica_outlier_threshold",
                ),
                dbc.Tooltip(
                    "Ausgewähltes Interview",
                    target="interview_title_detail",
                ),
                dbc.Tooltip(
                    "Die Heatmap zeigt die Topic-Verteilung der einzelnen Chunks des ausgewählten Interviews an. Die Chunks sind dabei in chronologischer Reihenfolge auf der X-Achse angebracht. Wenn Sie auf einen Chunk klicken, wird der Text unterhalb angezeigt.",
                    target="heat_map_interview_detail",
                ),
                dbc.Tooltip(
                    "Schaltet zum vorangehenden Chunk des ausgewählten Interviews.",
                    target="-_button_detail",
                ),
                dbc.Tooltip(
                    "Schaltet zum nächsten Chunk des ausgewählten Interviews.",
                    target="+_button_detail",
                ),
                dbc.Tooltip(
                    "Zeigt die Chunknummer des ausgewählten Chunks an.",
                    target="sent_title_detail",
                ),
            ]
        )
        return tooltip
    if trigger == "/page-1":
        tooltip = html.Div(
            [
                dbc.Tooltip(
                    "Die Textsuche bietet die Möglichkeit, nach Chunks mit bestimmter Topic-Gewichtung zu suchen. Die Ergebnisse werden direkt in Textform präsentiert.",
                    target="menu_selection_info",
                ),
                # Page 6 -Chunk Suche
                dbc.Tooltip(
                    "Geben Sie die Nummer des Topics ein, nach dem Sie das Korpus analysieren möchten.",
                    target="topic_print",
                ),
                dbc.Tooltip(
                    "Geben Sie hier den Schwellenwert ein, über dem die Topic-Gewichte liegen müssen, um in der Analyse berücksichtigt zu werden. Der Wert muss unter 1 liegen.",
                    target="weight_print",
                ),
                dbc.Tooltip(
                    "Geben Sie hier die Interview-ID ein, innerhalb der Sie die Chunks durchsuchen möchten. Das funktioniert nur bei ausgewählter 'Interview Search'.",
                    target="interview_id_search",
                ),
                dbc.Tooltip(
                    "Wählen Sie aus, ob Sie die Topic Suche innerhalb des Korpus ('Korpus Search'), oder innerhalb eines Interviews ('Interview Search') durchführen möchten.",
                    target="text_search_options",
                ),
                dbc.Tooltip(
                    "Drücken Sie auf 'Search', um die Suche mit den von Ihnen ausgewählten Optionen zu starten.",
                    target="enter_print",
                ),
            ]
        )
        return tooltip
    if trigger == "/page-4":
        tooltip = html.Div(
            [
                dbc.Tooltip(
                    "Mit der Topic-Wörter-Funktion können Sie die einzelnen Wörter jedes Topics anschauen.",
                    target="menu_selection_info",
                ),
                            # Page 7 -Topic Wörter
                dbc.Tooltip(
                    "Geben Sie die Anzahl der Worte ein, die Sie für jedes Topic angezeigt bekommen möchten. Maximal bis 999",
                    target="word_number",
                ),
                dbc.Tooltip(
                    "Drücken Sie auf 'Enter Topics', um sich die ausgewählte Anzahl an Worten pro Topic anzeigen zu lassen.",
                    target="enter_print_topics",
                ),
            ]
        )
        return tooltip


def menu_label_function(trigger):
    if trigger == "/":
        menu_label = "Overview"
        return menu_label
    if trigger == "/page-6":
        menu_label = "Chunk Analyzation"
        return menu_label
    if trigger == "/page-2":
        menu_label = "Bar Graph"
        return menu_label
    if trigger == "/page-5":
        menu_label = "Heatmap"
        return menu_label
    if trigger == "/page-3":
        menu_label = "Interview Heatmap"
        return menu_label
    if trigger == "/page-1":
        menu_label = "Chunk Suche"
        return menu_label
    if trigger == "/page-4":
        menu_label = "Topic Wörter"
        return menu_label
