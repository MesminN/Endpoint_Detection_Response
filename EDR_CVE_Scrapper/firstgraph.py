import matplotlib.pyplot as plt


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
            sum +=1
        mean /= sum
        cves.append(mean)
    plt.bar(range(len(data)), cves)
    plt.legend(names)
    plt.show()