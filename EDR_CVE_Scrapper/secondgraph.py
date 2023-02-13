from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.cm as cm


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

    cmap = cm.get_cmap('viridis', len(cves))
    for i, (name, cve) in enumerate(zip(names, cves)):
        plt.bar(i, cve, color=cmap(i), label=name)
    plt.xticks(range(len(data)))
    plt.xlabel("Solution")
    plt.ylabel("Nombre de jours moyen avant patch")
    plt.legend()
    plt.show()
