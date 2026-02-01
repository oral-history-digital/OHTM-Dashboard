def option_switch_sidebar_function(chronologie_analyse):
    if chronologie_analyse:
        sideboard_options = [
            {
                "label": "Tooltips anzeigen",
                "value": "tooltip_on",
            },
            {
                "label": "Topic Labels",
                "value": "topic_labels_on",
            },
            {
                "label": "Topic Clusters",
                "value": "topic_cluster_on",
            },
            {
                "label": "IHC",
                "value": "ihc",
            },
        ]

    else:
        sideboard_options = [
            {
                "label": "Tooltips anzeigen",
                "value": "tooltip_on",
            },
            {
                "label": "Topic Labels",
                "value": "topic_labels_on",
            },
            {
                "label": "Topic Clusters",
                "value": "topic_cluster_on",
            },
        ]
    return sideboard_options
