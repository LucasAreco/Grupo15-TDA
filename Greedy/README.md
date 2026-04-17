# Greedy

### Problema a Resolver



El código encontrado resuelve el problema del Camino Mínimo desde un Origen en un grafo ponderado. Dado un vértice de inicio (salida) ingresado por el usuario, el programa calcula la distancia mínima total requerida para viajar desde ese punto hacia todos los demás vértices conectados en la red.


---



### Algoritmo y Estructuras de Datos

El algoritmo conocido que replica este código es el Algoritmo de Dijkstra. Para lograr su objetivo, el programa hace uso de tres estructuras de datos principales:

- **COST (N,N):** Es la matriz de adyacencia del grafo. Almacena el "costo" o "distancia" de viajar directamente de un vértice a otro. Si no hay conexión directa entre dos nodos, el programa le asigna un valor artificialmente alto (`15000`), que actúa conceptualmente como infinito.

- **DIST (N):** Es un arreglo de distancias. Su función es mantener un registro de la distancia mínima conocida hasta el momento desde el vértice de salida hacia cada uno de los demás vértices.

- **SOL (N):** Es un arreglo de estados (booleanos). Funciona como un conjunto de vértices ya procesados. Un valor de `0` significa que la distancia mínima a ese vértice aún no es definitiva, mientras que un `1` indica que el camino más corto hacia él ya ha sido asegurado.


---


### Naturaleza Greedy y Optimidad

#### ¿Por qué se considera un algoritmo Greedy?

Se clasifica dentro de la familia de algoritmos Greedy porque en cada paso iterativo toma la decisión que parece más óptima en ese instante exacto (óptimo local), sin reevaluar decisiones pasadas, con el objetivo de construir la solución óptima global.

#### Regla de Elección

La regla que aplica en cada iteración es: De todos los vértices que aún no han sido procesados (SOL(J) = 0), elegir siempre aquel que tenga la distancia acumulada (DIST) más pequeña.
Una vez seleccionado este vértice, se marca como procesado y se utiliza como puente para intentar mejorar las distancias de todos sus vecinos adyacentes.

#### Justificación de la Solución Óptima

El algoritmo de Dijkstra **garantiza encontrar siempre la solución óptima** (el camino mínimo real), **siempre y cuando el grafo no contenga aristas con pesos negativos**. Al elegir el nodo no visitado con la menor distancia actual, el algoritmo asume con seguridad que no existe otra ruta más corta para llegar a él a través de otros nodos no visitados (ya que cualquier otro camino implicaría sumar pesos positivos a una distancia que ya es mayor). Por lo tanto, cada vez que un nodo se marca con `SOL(I) = 1`, su distancia mínima hallada es definitiva y óptima.

---

### Diseño: Pseudocódigo

A continuación, se presenta el pseudocódigo general del algoritmo implementado:

```text
ALGORITMO Dijkstra_CaminoMinimo(Grafo, Origen)
    INICIALIZAR Matriz de adyacencia COST con infinito en conexiones nulas
    INICIALIZAR arreglo DIST donde DIST[i] = COST[Origen][i]
    INICIALIZAR arreglo SOL con 0 (falso) para todos los nodos
    
    SOL[Origen] = 1
    DIST[Origen] = 0
    
    REPETIR (N - 1) veces:
        min_dist = Infinito
        u = NULO
        
        // Regla Greedy: Buscar nodo no procesado con menor distancia
        PARA CADA nodo j EN Grafo:
            SI DIST[j] <= min_dist Y SOL[j] == 0:
                min_dist = DIST[j]
                u = j
            
        SOL[u] = 1 // Marcar como definitivo
        
        // Relajar conexiones
        PARA CADA nodo j EN Grafo:
            SI DIST[j] > DIST[u] + COST[u][j]:
                DIST[j] = DIST[u] + COST[u][j]
                
    MOSTRAR DIST
```
---

### Seguimiento de Ejemplo

Utilizando los datos de prueba del enunciado (11 vértices) y eligiendo el Vértice 11 como origen, el seguimiento de las primeras iteraciones es el siguiente:

1. Inicialización:
    - Origen = 11.
    - SOL[11] = 1.
    - DIST inicial desde 11: DIST[8] = 56, DIST[10] = 30. El resto de los nodos inician en infinito (15000).
2. Iteración 1:
    - Se evalúan los nodos no visitados. El menor es el nodo 10 (DIST[10] = 30).
    - Se marca SOL[10] = 1.
    -Se relajan sus vecinos: Desde el 10 se puede ir al 9 (costo 46). Nueva distancia al 9: DIST[9] = DIST[10] + 46 = 76.
3. Iteración 2:
    - De los no visitados (8 con 56, 9 con 76, resto infinito), el menor es el nodo 8.
    - Se marca SOL[8] = 1.
    - Se relajan sus vecinos: Desde el 8 se va al 7 (costo 69) y al 9 (costo 45).
        - Camino al 7: DIST[7] = 56 + 69 = 125.
        - Camino al 9 vía 8: 56 + 45 = 101. Como 101 NO es menor que 76 (camino actual al 9), NO se actualiza.
4. Iteraciones subsiguientes:
    - El algoritmo continúa nodo a nodo (9, luego 7, 6, 5, etc.) expandiendo los caminos más cortos hasta que todos los SOL están en 1.
    - Resultado final relevante: La distancia desde 11 hacia 9 es óptima en 76, y hacia 1 es 593.

---


### Análisis de Complejidad


Definiendo $N$ como la cantidad total de vértices en el grafo:

#### Complejidad Espacial

El orden de complejidad espacial es $O(N^2)$.
La estructura que domina el uso de memoria es la matriz bidimensional COST de tamaño $N \times N$. Los arreglos auxiliares DIST y SOL ocupan un espacio de $O(N)$, así que la matriz termina dictando la complejidad espacial total del programa.

#### Complejidad Temporal

El orden de complejidad temporal es $O(N^2)$.Esto se deduce del flujo principal del programa (subrutina en la línea 1000):

1. Existe un bucle principal que se repite $N-1$ veces.
2. Dentro de este bucle, se ejecuta un recorrido de $N$ pasos para encontrar el vértice no visitado con la distancia mínima.
3. Luego, se ejecuta otro recorrido de $N$ pasos para actualizar las distancias de los vecinos.
El trabajo total dentro del bucle es proporcional a $2N$, lo que multiplicado por las $N$ iteraciones exteriores resulta en un tiempo de ejecución proporcional a $N^2$. Adicionalmente, la inicialización de la matriz de adyacencia toma un tiempo $O(N^2)$. Por lo tanto, el tiempo total es cuadrático.


---


### Código Fuente en Python

El código fuente completo y ejecutable se encuentra en el archivo adjunto `paolo.py`.

#### Correcciones aplicadas al algoritmo original

Durante la traducción del código bas a Python, se identificaron y corrigieron dos errores lógicos presentes en el algoritmo original que afectaban el resultado si los datos no se ingresaban en un orden específico:

1. Corrección de la matriz simétrica
    - Error original: La instrucción `COST(I,J) = COST(J,I)` borraba conexiones (asignando el infinito `15000`) si los ejes se ingresaban de mayor a menor (ej. 11,10).
    - Solución: Se implementó `min(COST[i][j], COST[j][i])` para conservar siempre el costo real, garantizando una matriz simétrica sin importar el orden de ingreso.
2. Corrección del bucle Greedy
    - Error original: Se utilizaba la misma variable `U` para almacenar dos datos incompatibles: la distancia mínima (`U=15000`) y el índice del nodo (`U=J`), lo que rompía la lógica de búsqueda.
    - Solución: Se separó el uso en dos variables independientes: `min_dist` exclusivamente para la distancia y `U` para el índice del nodo.

---

### Requisitos Técnicos

- **Versión de Python:** Python 3.8 o superior.
- **Bibliotecas requeridas:** Ninguna (el código utiliza únicamente funciones *built-in* de Python).


---

### Referencias

Algoritmo de Dijkstra. (2021, August 21). Wikipedia. https://es.wikipedia.org/wiki/Algoritmo_de_Dijkstra