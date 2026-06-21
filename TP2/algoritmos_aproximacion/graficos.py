import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
import os

if not os.path.exists("resultados/resultados_resumen.csv"):
    print("ERROR: El archivo 'resultados/resultados_resumen.csv' no existe.")
    sys.exit(1)

df = pd.read_csv("resultados/resultados_resumen.csv", sep=";")
print(df.info())
df = df.sort_values(by=['TipodeInstancia', 'N']).reset_index(drop=True)

colores = {
    'Trivial': '#2ca02c',        # Verde
    'General': '#ff7f0e',        # Naranja
    'Aleatorio': '#1f77b4',      # Azul
    'Hard Disperso': '#d62728'    # Rojo destacado
}
marcadores = {'Trivial': 'o', 'General': 's', 'Aleatorio': '^', 'Hard Disperso': 'X'}
tamaños_ticks = [10, 50, 100, 500, 1000]

# GRÁFICO A: COMPARATIVA DEL GAP RELATIVO PORCENTUAL
plt.figure(figsize=(10, 6), dpi=300)

for tipo in colores.keys():
    sub_df = df[df['TipodeInstancia'] == tipo]
    if not sub_df.empty:
        plt.plot(sub_df['N'], sub_df['Gap'], 
                 marker=marcadores[tipo], color=colores[tipo], 
                 linestyle='-', linewidth=2, markersize=8, label=tipo)

plt.xscale('log')
plt.xticks(tamaños_ticks, [str(t) for t in tamaños_ticks])
plt.ylim(-1, 26)

plt.title('Análisis Comparativo del Error de Optimización (Gap %)', fontsize=13, pad=15, fontweight='bold')
plt.xlabel('Tamaño del Conjunto ($N$)', fontsize=11, labelpad=8)
plt.ylabel('Gap Relativo Promedio ($\%$ respecto a $B$)', fontsize=11, labelpad=8)
plt.grid(True, linestyle='--', alpha=0.5, which='both')
plt.legend(title='Categoría de Instancia', fontsize=10, title_fontsize=11, loc='upper left')
plt.tight_layout()

plt.savefig('resultados/comparativa_gaps.png')
plt.show()


# GRÁFICO B: TIEMPOS DE EJECUCIÓN CON CURVA TEÓRICA N LOG N
plt.figure(figsize=(10, 6), dpi=300)

for tipo in colores.keys():
    sub_df = df[df['TipodeInstancia'] == tipo]
    if not sub_df.empty:
        plt.plot(sub_df['N'], sub_df['Tiempo'], 
                 marker=marcadores[tipo], color=colores[tipo], 
                 linestyle='-', linewidth=2, markersize=8, label=tipo)

n_teorico = np.linspace(10, 1000, 500)
y_teorico = n_teorico * np.log2(n_teorico)

max_tiempo_real = df['Tiempo'].max()
c = max_tiempo_real / y_teorico[-1]
plt.plot(n_teorico, c * y_teorico, color='#555555', linestyle='--', linewidth=2, 
         label='Complejidad Teórica O(N log N)')

plt.xscale('log')
plt.xticks(tamaños_ticks, [str(t) for t in tamaños_ticks])

plt.title('Complejidad Temporal Empírica vs. Curva Teórica Asintótica', fontsize=13, pad=15, fontweight='bold')
plt.xlabel('Tamaño del Conjunto ($N$)', fontsize=11, labelpad=8)
plt.ylabel('Tiempo Promedio ($\mu s$ - Microsegundos)', fontsize=11, labelpad=8)
plt.grid(True, linestyle='--', alpha=0.5, which='both')
plt.legend(title='Referencias', fontsize=10, title_fontsize=11, loc='upper left')
plt.tight_layout()

plt.savefig('resultados/tiempos_aprox.png')
plt.show()

print("Imágenes guardadas en /resultados")