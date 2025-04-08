""" """


def create_dropdown_list(ohtm_file):
    drop_down_list = []
    for archives in ohtm_file["corpus"]:
        a = {"label": archives, "value": archives}
        drop_down_list.append(a)

    drop_down_list.append({"label": "Corpus", "value": "all"})
    return drop_down_list
