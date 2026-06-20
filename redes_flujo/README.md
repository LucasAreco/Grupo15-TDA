# Redes de Flujo

Estamos construyendo una red WAN con n antenas y queremos que tenga un buen nivel
de tolerancia a fallas. Dada una antena, su conjunto de backup de tamaño k es el
conjunto de k antenas que se encuentran a una distancia menor a D. Queremos evitar
que una antena pertenezca al conjunto de backup de más de b antenas, precisamente
para evitar que un fallo pueda afectar a una porción importante de la red. Suponer que
conocemos los valores D, b y k, y que tenemos una matriz d[1..n, 1..n] con las distancias
entre antenas, de forma tal que d[i,j] es la distancia entre la antena i y la j.
Plantear un algoritmo de complejidad polinomial que encuentre el conjunto de backup
de tamaño k de cada una de las n antenas, de forma tal que ninguna aparezca en más
de b conjuntos de backup, o bien, que indique que no existe una solución posible. Debe
apoyarse en el algoritmo estándar de Ford-Fulkerson, la variante escalada o la de
Edmonds-Karp.


Se incluye:
- Implementación del algoritmo en `rf.py`
- Casos de prueba desde archivo en `ejemplos.py`
- Gráfico empírico de complejidad temporal en `tiempos.py`


## Requisitos
Para ejecutar algoritmo en `rf.py`, es necesario tener instalado:
- **Python 3.10** o superior.

Para ejecutar `tiempos.py` y visualizar los gráficos de tiempos de ejecución, es necesario además contar con las siguientes bibliotecas:
-  **NumPy**: Para manejar las secuencias numéricas.
- **Matplotlib**: Para generar el gráfico comparativo de tiempos.

Para ejecutar `ejemplos.py` y leer `datasets.json` es necesario contar con la biblioteca **json**.

Puedes instalarlas fácilmente abriendo una terminal y ejecutar:

```sh 
pip install -r requirements.txt
``` 
*Nota*: Si el comando pip no funciona en tu sistema, intenta con pip3.

## Correr el algoritmo con ejemplos
```py 
python ejemplos.py
``` 
*Nota*: Si el comando python no funciona en tu sistema, intenta con python3 ejemplos.py.

## Correr de gráficos de tiempos de ejecución
```py 
python tiempos.py
``` 
*Nota*: Si el comando python no funciona en tu sistema, intenta con python3 tiempos.py.