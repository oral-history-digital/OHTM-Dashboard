def sideboard_info_function(ohtm_file):
    output = []
    output.append("Interviews Total: " + str(ohtm_file["settings"]["interviews"]["total"]) + "\n")
    output.append("Topics: " + str(ohtm_file["settings"]["topic_modeling"]["topics"])+ "\n")
    output.append("Chunk Length: " + str(ohtm_file["settings"]["preprocessing"]["chunk_setting"]) + "\n")
    chunk_count = 0
    for archive in ohtm_file["weight"]:
        for interview in ohtm_file["weight"][archive]:
            for chunk in ohtm_file["weight"][archive][interview]:
                chunk_count += 1
    output.append("Chunks: " + str(chunk_count))      

    return output