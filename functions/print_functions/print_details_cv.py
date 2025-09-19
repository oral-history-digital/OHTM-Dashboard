def print_details_cv_function(data, options, labels):
    data.sort(reverse=True, key=lambda x: x[0])
    links = {}
    for entrys in data:
        for i in entrys[4]:
            if i.split(",")[0] not in links:
                links[i.split(",")[0]] = 1
            else:
                links[i.split(",")[0]] += 1
    sorted_by_values = dict(sorted(links.items(), key=lambda item: item[1], reverse=True))
    results_2 = []
    for a in sorted_by_values:
        if "topic_labels_on" in options:
            results_2.append("Topic " + str(a) + " (" + str(sorted_by_values[a])+ ")" + "- " + str(labels[a]))
        else:
            results_2.append("Topic " + str(a) + " (" + str(sorted_by_values[a])+ ")")
    detail_results = "\n".join(results_2)
    detail_results = "\n".join(results_2)

    sum = {}
    total = 0
    for archive in data:
        if archive[3] not in sum:
            sum[archive[3]] = []
            sum[archive[3]].append(archive[1])
        else:
            sum[archive[3]].append(archive[1])

    detail_results_archive =[]
    total = 0
    for archive in sum:
        detail_results_archive.append(archive + ": " + str(len(set(sum[archive])))+ " ")
        total += len(set(sum[archive]))
    detail_results_archive.append("Total: " + str(total)+ " ")

    detail_results_archive_sorted = sorted(detail_results_archive, key=lambda x: int(x.split(': ')[1]), reverse=True)
    return detail_results, detail_results_archive_sorted
