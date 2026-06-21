# Algoritmos de Aproximación

Este módulo contiene la resolución del problema de aproximación para obtener la mayor suma de un subconjunto sin sobrepasar un valor determinado. Una instancia de este problema debe incluir obligatoriamente un conjunto de números enteros positivos y un target entero positivo. Se proporciona un script para generar set de datos que permiten probar el algoritmo implementado.

## Estructura del Proyecto

El repositorio está organizado de la siguiente manera:
- `algoritmo_greedy.py`: Contiene la función `hallar_subconjunto_factible(set_a, b_max)` que resuelve la heurística de aproximación.
- `generador.py`: Script encargado de construir los datasets de prueba de forma reproducible bajo cuatro categorías (*Trivial, General, Aleatorio, Hard Disperso*).
- `main.py`: programa que ejecuta casos de prueba para el algoritmo propuesto.
- `graficos.py`: Script auxiliar en Python que procesa los resultados obtenidos y exporta los gráficos de calidad (*Gaps*) y complejidad temporal.
- `datasets/`: Carpeta donde se almacenan las instancias de prueba en formato `.json`.
- `resultados/`: Carpeta donde se almacenan los resultados obtenidos y los gráficos generados

## Requisitos

Para ejecutar el algoritmo y el entorno de pruebas masivas por consola de manera nativa, solo se requiere:
- **Python 3.10** o superior (sin dependencias externas).

Si desea ejecutar el script `graficador.py` para regenerar las curvas del informe, necesitará contar con las siguientes bibliotecas adicionales:
- **NumPy**
- **Pandas**
- **Matplotlib**

Puede instalarlas fácilmente abriendo una terminal y ejecutando:
```sh
pip install pandas numpy matplotlib
```

## Como ejecutar los scripts

El algoritmo se puede ejecutar con archivos indivisuales que deben cumplir el siguiente formato:

```python
{
    "conjunto": [...],
    "target": X
}
```

Para ejecutar un caso en particular se debe estar posicionado en la carpeta de `TP2/algoritmos_aproximacion` y ejecutar el comando `python -m main path/al/dataset`. En caso de que no se proporcione ningún archivo se ejecutarán todos los casos incluidos en la carpeta `datasets` y se guardarán los resultados en `resultados/resultados_resumen.csv`.

En caso de querer generar gráficos que resuman visualmente las ejecuciones se puede ejecutar, en la misma carpeta ya mencionada, `python -m graficos` **luego** de haber obtenido el archivo `resultados/resultados_resumen.csv`. Los gráficos generados se guardarán en la carpeta `resultados/`.