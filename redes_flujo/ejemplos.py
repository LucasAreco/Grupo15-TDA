import json
import time
from rf import resolver_backups

with open("dataset.json", "r") as f:
    datasets = json.load(f)

for caso in datasets:
    print(f"- {caso['nombre']} -")
    print(f"D={caso['D']}, k={caso['k']}, b={caso['b']}")

    inicio = time.perf_counter()
    resultado = resolver_backups(caso["D"], caso["distancias"], caso["k"], caso["b"])
    fin = time.perf_counter()
    tiempo = fin - inicio

    print("Resultado:", resultado)
    print(f"Tiempo: {tiempo:.6f} segundos\n")
