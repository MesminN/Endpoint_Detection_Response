import matplotlib.pyplot as plt
import matplotlib.cm as cm
from datetime import datetime


def plot(data, names, cves, x_label_title, y_label_title):
    cmap = cm.get_cmap('viridis', len(cves))
    for i, (name, cve) in enumerate(zip(names, cves)):
        plt.bar(i, cve, color=cmap(i), label=name)
    plt.xticks(range(len(data)))
    plt.xlabel(x_label_title)
    plt.ylabel(y_label_title)
    plt.legend()
    plt.show()


def get_gravite_moyenne_par_solution(data):
    result = {}
    names = list(data.keys())
    all_values = list(data.values())

    for index, matrix in enumerate(all_values):
        mean = 0.0
        sum = 0
        for line in matrix:
            mean += float(line[5])
            sum += 1
        mean /= sum
        result[names[index]] = mean

    return result


def gravite_moyenne_par_solution(data):
    print("Gravité moyenne par solution")
    tab = get_gravite_moyenne_par_solution(data)
    names = list(tab.keys())
    cves = list(tab.values())

    plot(tab, names, cves, "Solution", "Gravité Moyenne")


def get_jours_moyens_path_par_solution(data):
    result = {}
    names = list(data.keys())
    all_values = list(data.values())

    for index, matrix in enumerate(all_values):
        mean = 0.0
        sum = 0
        for line in matrix:
            detection_date = datetime.strptime(line[3], "%Y-%m-%d")
            resolved_date = datetime.strptime(line[4], "%Y-%m-%d")
            delta = resolved_date - detection_date
            mean += delta.days
            sum += 1
        mean /= sum
        result[names[index]] = mean

    return result


def jours_moyens_patch_par_solution(data):
    print("Nombre de jours moyens avant patch par solution")
    tab = get_jours_moyens_path_par_solution(data)
    names = list(tab.keys())
    cves = list(tab.values())

    plot(tab, names, cves, "Solution", "Nombre de jours moyen avant patch")


def get_nombre_cves_par_solution(data):
    result = {}
    names = list(data.keys())
    all_values = list(data.values())

    for index, matrix in enumerate(all_values):
        nb_cves = len(matrix)
        result[names[index]] = nb_cves

    return result


def nombre_cves_par_solution(data):
    print("Nombre de CVE par solution")
    tab = get_nombre_cves_par_solution(data)
    names = list(tab.keys())
    cves = list(tab.values())

    plot(tab, names, cves, "Solution", "Nombre CVE")
