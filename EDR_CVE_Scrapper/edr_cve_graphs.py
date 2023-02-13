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


def gravite_moyenne_par_solution(data):
    print("Gravité moyenne par solution")
    names = list(data.keys())
    all_values = list(data.values())

    cves = []
    for matrix in all_values:
        mean = 0.0
        sum = 0
        for line in matrix:
            mean += float(line[5])
            sum += 1
        mean /= sum
        cves.append(mean)

    plot(data, names, cves, "Solution", "Gravité Moyenne")


def jours_moyen_patch_par_solution(data):
    print("Nombre de jours moyens avant patch par solution")
    names = list(data.keys())
    all_values = list(data.values())

    cves = []
    for matrix in all_values:
        mean = 0.0
        sum = 0
        for line in matrix:
            detection_date = datetime.strptime(line[3], "%Y-%m-%d")
            resolved_date = datetime.strptime(line[4], "%Y-%m-%d")
            delta = resolved_date - detection_date
            mean += delta.days
            sum +=1
        mean /= sum
        cves.append(mean)

    plot(data, names, cves, "Solution", "Nombre de jours moyen avant patch")


def nombre_cve_par_solution(data):
    print("Nombre de CVE par solution")
    names = list(data.keys())
    all_values = list(data.values())

    cves = []
    for matrix in all_values:
        cves.append(len(matrix))

    plot(data, names, cves, "Solution", "Nombre CVE")