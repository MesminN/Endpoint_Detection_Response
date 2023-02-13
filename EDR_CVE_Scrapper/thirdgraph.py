import matplotlib.pyplot as plt
import matplotlib.cm as cm

def nombre_cve_par_solution(data):
    print("Nombre de CVE par solution")
    names = list(data.keys())
    all_values = list(data.values())

    cves = []
    for matrix in all_values:
        cves.append(len(matrix))

    cmap = cm.get_cmap('viridis', len(cves))
    for i, (name, cve) in enumerate(zip(names, cves)):
        plt.bar(i, cve, color=cmap(i), label=name)
    plt.xticks(range(len(data)))
    plt.xlabel("Solution")
    plt.ylabel("Nombre CVE")
    plt.legend()
    plt.show()