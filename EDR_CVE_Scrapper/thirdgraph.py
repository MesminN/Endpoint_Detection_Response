import matplotlib.pyplot as plt


def nombre_moyen_par_solution(data):
    print("Nombre moyen de CVE par solution")
    names = list(data.keys())
    all_values = list(data.values())

    cves = []
    for matrix in all_values:
        cves.append(len(matrix))

    plt.bar(range(len(data)), cves)
    plt.legend(names)
    plt.show()