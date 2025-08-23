def print_details_cv_function(data):
    data.sort(reverse=True, key=lambda x: x[0])
    links = {}
    for entrys in data:
        for i in entrys[3]:
            if i.split(",")[0] not in links:
                links[i.split(",")[0]] = 1
            else:
                links[i.split(",")[0]] += 1
    sorted_by_values = dict(sorted(links.items(), key=lambda item: item[1], reverse=True))
    results_2 = []
    for a in sorted_by_values:
        results_2.append("Topic " + str(a) + " (" + str(sorted_by_values[a])+ ")")
    detail_results = "\n".join(results_2)

    

    return detail_results
