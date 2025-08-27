def print_details_cv_function(data):
    topic_labels = {
        0: "Umbruch und Transformation",
        1: "Arbeit und Industrie",
        2: "Arbeit und Bau",
        3: "Stahlindustrie/Ruhrgebiet",
        4: "Arbeitsmigration",
        5: "Justiz",
        6: "Judentum",
        7: "Kleidung und Mode",
        8: "Erziehung (auch: Erziehungseinrichtungen)",
        9: "Krieg (Häufig WK II/Ostfront)",
        10: "Natur",
        11: "Politische Jugendorganisationen/DDR",
        12: "Judenverfolgung und Deportation",
        13: "Colonia Dignidad/Strukturen",
        14: "Haushalt und Hausarbeit",
        15: "Urlaub und Reisen",
        16: "Krankheit und Medizinische Versorgung",
        17: "Familie und Familienleben/Kernfamilie",
        18: "Innerdeutsche Grenze/Zwangsumsiedlung und ländlicher Raum",
        19: "Empfindungen (Häufig: positive E.)",
        20: "Versorgung",
        21: "Naturschutz",
        22: "Arbeit/Bergbau",
        23: "Interessenverbände und Gremien",
        24: "Paratext",
        25: "Genussmittel",
        26: "Landwirtschaft und Bauernhof",
        27: "Familie und Schicksalsschlag/Verlust",
        28: "Ausbildung",
        29: "Bauen und Wohnen",
        30: "Parteien und Politik",
        31: "Colonia Dignidad/Alltag",
        32: "Bahnfahren und Transport",
        33: "Universität",
        34: "Judentum in Südosteuropa und Zwangsarbeit",
        35: "Orte/NRW",
        36: "Familie und Krieg/Osteuropa",
        37: "Feiern und Festtage",
        38: "Christentum",
        39: "NS/Organisationen",
        40: "Paratext",
        41: "WK II/Zwangsarbeit",
        42: "Neuapostolische Kirche und Sekten",
        43: "Empfindungen",
        44: "Migration und Sprache",
        45: "Finanzen",
        46: "Erinnerung und Erinnerungskultur",
        47: "Ruhrgebiet",
        48: "Sucht",
        49: "Mobilität und Fahrzeuge",
        50: "Arbeit (auch: Einstellung zu A.)",
        51: "Subkultur",
        52: "Lager/Sowjetische Speziallager",
        53: "WK II/Lager",
        54: "Studium",
        55: "(Bomben)Krieg/WK II",
        56: "Krieg (Häufig: WK II/Front)",
        57: "Arbeit und Stahlindustrie/DDR",
        58: "Systemvergleich und Systemwechsel",
        59: "Länder und Nationen",
        60: "Literatur und Printmedien",
        61: "Rundfunk und Fernsehen",
        62: "Israel",
        63: "Familie/Heirat und Geburt",
        64: "Arbeit und Wirtschaft/DDR",
        65: "Familie",
        66: "verrauscht",
        67: "Gewerkschaft und Betriebsrat",
        68: "Lebensmittel und Ernährung",
        69: "WK II/Lager",
        70: "Sport/Freizeit und Vereinswesen",
        71: "verrauscht",
        72: "Fotografie und Bildende Kunst",
        73: "Interviewsituation",
        74: "Empfindungen und Erinnern",
        75: "Lebenslauf",
        76: "Soziale Bewegungen",
        77: "Wohnung und Wohnen",
        78: "Printmedien",
        79: "WK II/Lager und Kriegsgefangenschaft",
        80: "Film und Fernsehen",
        81: "Politische Haft/SBZ und DDR",
        82: "Militär",
        83: "WKII/Kriegsende und Alliierte",
        84: "Industrie und Wirtschaft",
        85: "Flucht und Vertreibung",
        86: "Tagesrhythmus",
        87: "Soziale Kontakte und Freizeit",
        88: "Familie/Verwandtschaft und Vorfahren",
        89: "Bürokratie",
        90: "Gewalt und Repression",
        91: "Kriegsende und Nachkriegszeit",
        92: "verrauscht",
        93: "Reflexion",
        94: "Vergangenheit und Verarbeitung",
        95: "Schule",
        96: "Frauen in NS-Organisationen",
        97: "Erschwerte Lebensbedingungen",
        98: "Bühne/Musik und Schauspiel",
        99: "Osteuropa und Österreich-Ungarn"
        }
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
        results_2.append("Topic " + str(a) + " (" + str(sorted_by_values[a])+ ")" + "- " + str(topic_labels[int(a)]))
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
        detail_results_archive.append(archive + ": " + str(len(set(sum[archive]))) + "\n")
        total += len(set(sum[archive]))
    detail_results_archive.append("Total: " + str(total))

    



    return detail_results, detail_results_archive
