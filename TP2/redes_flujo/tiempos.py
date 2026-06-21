import matplotlib.pyplot as plt
import numpy as np
import time
import random
from rf import resolver_backups

def generar_distancias(n, semilla):
    random.seed(semilla)
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0 if i == j else random.randint(1, 100))
        matriz.append(fila)
    return matriz

k = 2
b = 3
D = 50

tamanios = []
tiempos = []

for n in [20, 40, 60, 80, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
    distancias = generar_distancias(n, 74)
    inicio = time.perf_counter()
    sol = resolver_backups(D, distancias, k, b)
    fin = time.perf_counter()
    tiempo = fin - inicio
    tamanios.append(n)
    tiempos.append(tiempo)
    print(f"n = {n} | Tiene sol {sol != None} | tiempo = {tiempo:.6f} segundos")

n_array = np.array(tamanios)
t_array = np.array(tiempos)

t_teorico_puntos = np.power(n_array, 5)
factor_escala = np.max(t_array / t_teorico_puntos)

n_teorico = np.linspace(min(tamanios), max(tamanios), 100)
t_teorico_normalizado = np.power(n_teorico, 5) * factor_escala

fig, ax = plt.subplots()
ax.plot(tamanios, tiempos, "o-", label="Curva empírica")
ax.plot(n_teorico, t_teorico_normalizado, "--", label="Curva teórica de ajuste O(n^5)")
ax.set_yscale("log") 
ax.set_xlabel("Cantidad de antenas (n)")
ax.set_ylabel("Tiempo (s)")
ax.set_title("Tiempo empírico vs tiempo teórico")
ax.grid(True)
ax.legend()
plt.show()