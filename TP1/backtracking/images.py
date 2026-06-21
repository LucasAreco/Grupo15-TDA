# import matplotlib.pyplot as plt
# import numpy as np

# # 1. Tus datos (n, m, tiempo)
# datos_raw = []
# with open("data/results_avg.csv", "r") as file:
#     for line in file:
#         n, m, t = line.strip().split(",")
#         datos_raw.append((int(n), int(m), float(t)))

# # 2. Procesamiento de datos
# areas = np.array([n * m for n, m, t in datos_raw])
# tiempos = np.array([t for n, m, t in datos_raw])

# # Ordenar por área para que las líneas del gráfico no se crucen
# indices = np.argsort(areas)
# areas = areas[indices]
# tiempos = tiempos[indices]

# # 3. Calcular la curva teórica O(n*m)
# # Usamos el último punto para calcular la constante de ajuste (c)
# c = tiempos[-1] / areas[-1]
# tiempos_teoricos = c * areas

# # 4. Creación del gráfico
# plt.figure(figsize=(10, 6))

# # Dibujar curva empírica (tus puntos)
# plt.plot(areas, tiempos, 'o-', label='Curva Empírica (Mediciones)', color='blue', markersize=4)

# # Dibujar curva teórica
# plt.plot(areas, tiempos_teoricos, '--', label='Curva Teórica O(N*M)', color='red', alpha=0.7)

# # Configuración de etiquetas
# plt.title('Complejidad Temporal: Laberinto Backtracking', fontsize=14)
# plt.xlabel('Tamaño del problema (N x M celdas)', fontsize=12)
# plt.ylabel('Tiempo de ejecución (segundos)', fontsize=12)
# plt.grid(True, linestyle='--', alpha=0.6)
# plt.legend()

# # Mostrar gráfico
# plt.savefig("backtracking_complexity_avg.png")
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# 1. Datos cargados
data_raw = """
1000,1000,0.0228
1000,1000,0.0230
100,100,0.0022
100,100,0.0015
100,100,0.0009
1100,1100,0.0245
1100,1100,0.0233
1100,1100,0.0236
1200,1200,0.0291
1200,1200,0.0373
1200,1200,0.0271
1300,1300,0.0288
1300,1300,0.0289
1300,1300,0.0290
1400,1400,3.9661
1400,1400,0.0363
1400,1400,0.0310
1500,1500,0.0410
1500,1500,4.5976
200,200,0.0625
200,200,0.0036
200,200,0.0026
300,300,0.0065
300,300,0.0062
300,300,0.0051
400,400,0.0111
400,400,0.0078
400,400,0.0098
500,500,0.0128
500,500,0.0098
500,500,0.0107
50,50,0.0008
50,50,0.0012
50,50,0.0006
600,600,0.6869
600,600,0.0105
600,600,0.6797
700,700,0.0161
700,700,0.0149
700,700,0.0159
800,800,0.0176
800,800,1.2704
900,900,0.0198
900,900,1.6339
"""

# 2. Procesar y agrupar (promediar tiempos por cada área N*M)
resultados = defaultdict(list)
for line in data_raw.strip().split('\n'):
    n, m, t = map(float, line.split(','))
    resultados[n * m].append(t)

# Calcular el promedio de tiempo para cada área
areas = sorted(resultados.keys())
tiempos_promedio = [np.mean(resultados[a]) for a in areas]

# 3. Graficar
plt.figure(figsize=(10, 6))

# Curva empírica promediada
plt.plot(areas, tiempos_promedio, 'o-', label='Promedio de mediciones', color='green')

# Tendencia (solo para visualizar el crecimiento)
plt.title('Complejidad Temporal: Caso Promedio (Agrupado)', fontsize=14)
plt.xlabel('Área del laberinto (N x M celdas)', fontsize=12)
plt.ylabel('Tiempo promedio (segundos)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

plt.savefig("backtracking_complexity_avg_grouped.png")
plt.show()