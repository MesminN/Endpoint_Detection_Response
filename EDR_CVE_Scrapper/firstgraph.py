import matplotlib.pyplot as plt
import matplotlib.cm as cm


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

    cmap = cm.get_cmap('viridis', len(cves))
    for i, (name, cve) in enumerate(zip(names, cves)):
        plt.bar(i, cve, color=cmap(i), label=name)
    plt.xticks(range(len(data)))
    plt.xlabel("Solution")
    plt.ylabel("Gravité Moyenne")
    plt.legend()
    plt.show()