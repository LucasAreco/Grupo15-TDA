import matplotlib.pyplot as plt
from numero_min_palindromos import obtener_menor_cantidad_palindromos
import numpy as np
import time
import random

def calcular_tiempo(cadena):
    t1 = time.time()
    obtener_menor_cantidad_palindromos(cadena)
    t2 = time.time()
    return t2-t1


random.seed(25)
def generar_cadena(n):
    letras = "ABCD"
    resultado = ""
    for i in range(n):
        resultado += random.choice(letras)

    return resultado

rangos = [100, 300, 500, 700, 1000, 1300, 1500, 1700, 2000, 2300, 2500, 2700, 3000]
tiempos_reales = []
tiempos_y_rangos = []
for rango in rangos:
    cadena = generar_cadena(rango)
    tiempo_real = calcular_tiempo(cadena)
    tiempos_y_rangos.append((rango, tiempo_real))
    tiempos_reales.append(tiempo_real)


n_teorico = np.linspace(min(rangos), max(rangos), 100)
t_teorico = np.pow(n_teorico, 2)

for rango, tiempo_real in tiempos_y_rangos:
    print(f"Para n = {rango}, t = {tiempo_real}")

    
factor_escala = tiempos_reales[-1] / t_teorico[-1]
tiempos_teoricos_normalizados = t_teorico * factor_escala

# Curva empírica vs teórica
fig, ax = plt.subplots()
ax.plot(rangos, tiempos_reales, 'o-', color='red', label='Curva Empírica')
ax.plot(n_teorico, tiempos_teoricos_normalizados, linestyle='--', color='blue', label='Curva Teórica O(N^2)')
ax.set_xlabel('Tamaño de la entrada (n)')
ax.set_ylabel('Tiempo(segundos)')
ax.set_title('Tiempo empírico contra tiempo teórico de ejecución')
ax.get_xaxis().get_major_formatter().set_scientific(False)
ax.grid(True)
ax.legend()
plt.xticks(rotation=45)
plt.show()


# Regresión Lineal
x = np.array(rangos)
y = np.array(tiempos_reales)
coef = np.polyfit(x**2, y, 1)

y_ajuste = coef[0]  * (x**2) + coef[1]
regresion = f"t ≈ {coef[0]:.8f} * n^2 + {coef[1]:.8f}"

fig, ax = plt.subplots()
ax.scatter(x**2, y, color='red', label='Datos empíricos')
ax.plot(x**2, y_ajuste, color='blue', label=f'Ajuste lineal: {regresion}')
ax.set_xlabel('n^2 (tamaño de entrada al cuadrado)')
ax.set_ylabel('Tiempo (segundos)')
ax.set_title('Regresión lineal de tiempo vs n^2')
ax.ticklabel_format(style='plain', axis='x')
ax.grid(True)
ax.legend()
plt.show()
