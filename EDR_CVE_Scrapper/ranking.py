from edr_cve_graphs \
    import plot, get_gravite_moyenne_par_solution, get_jours_moyens_path_par_solution, get_nombre_cves_par_solution


def get_nb_min_cves(data):
    result = 1500
    nb_cves_list = list(data.values())
    for nb_cves in nb_cves_list:
        result = min(result, nb_cves)

    return result


def get_nb_max_cves(data):
    result = 0
    nb_cves_list = list(data.values())
    for nb_cves in nb_cves_list:
        result = max(result, nb_cves)

    return result


def determine_weight(min_echelle, max_echelle, min_values, max_values, value):
    if value > max_values:
        value = max_values

    if value < min_values:
        value = min_values

    # print("Min: " + str(min_values))
    # print("Max: " + str(max_values))
    # print("Value: " + str(value))
    # print("Echelle: [" + str(min_echelle) + ", " + str(max_echelle) + "]")

    a = (max_echelle - min_echelle) / (max_values - min_values)
    b = max_echelle - a * max_values

    return round(max_echelle - ((value * a) + b), 2)


def get_rank_dictionary(data):
    solutions = list(data.keys())
    ranking = {}
    gravite_par_solution = get_gravite_moyenne_par_solution(data)
    jours_moyens = get_jours_moyens_path_par_solution(data)
    nb_cves = get_nombre_cves_par_solution(data)

    # print(jours_moyens)
    # print(gravite_par_solution)
    # print(nb_cves)
    for index, solution in enumerate(solutions):
        val1 = jours_moyens[solution]
        val2 = gravite_par_solution[solution]
        val3 = nb_cves[solution]
        min_val3 = get_nb_min_cves(nb_cves)
        max_val3 = get_nb_max_cves(nb_cves)
        # print(solution + ": [" + str(val1) + "; " + str(val2) + "; "+ "( " + str(min_val3) + "," + str(val3) +
        # "," + str(max_val3) + ")" + "]")

        reaction_note = determine_weight(0, 5, 1, 21, val1)
        gravite_note = determine_weight(0, 4, 0, 10, val2)
        cves_note = determine_weight(0, 1, min_val3, max_val3, val3)
        # print("[" + str(reaction_note) + ", " + str(gravite_note) + ", " + str(cves_note) + "]")
        ranking[solution] = reaction_note + gravite_note + cves_note

    return dict(sorted(ranking.items(), key=lambda item: item[1], reverse=True))


def display_ranking(data):
    print("Ranking:")
    solutions = list(data.keys())
    grades = list(data.values())
    for index, grade in enumerate(grades):
        print(str(index) + " - " + solutions[index] + ": " + str(grade))
    print()


def plot_ranking(data):
    solutions = list(data.keys())
    grades = list(data.values())
    plot(data, solutions, grades, "Solution EDR", "Note de la solution sur 10")