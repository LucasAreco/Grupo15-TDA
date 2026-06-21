def armar_red_flujo(n, D, distancias, k, b):
     red_flujo = {}
     red_flujo["s"] = {}

     for i in range(1, n+1):
          red_flujo["s"][f"a{i}"] = k

     for i in range(1, n+1):
          red_flujo[f"a{i}"] = {}
          for j in range(1, n+1):
               if i != j and distancias[i-1][j-1] < D:
                    red_flujo[f"a{i}"][f"c{j}"] = 1

     for i in range(1, n+1):
          red_flujo[f"c{i}"] = {}
          red_flujo[f"c{i}"]["t"] = b

     red_flujo["t"] = {}
     return red_flujo


def convertir_a_grafo_residual(n, D, distancias, red):
     for i in range(1, n+1):
          red[f"a{i}"]["s"] = 0

     for i in range(1, n+1):
          for j in range(1, n+1):
               if i != j and distancias[i-1][j-1] < D:
                    red[f"c{j}"][f"a{i}"] = 0

     for i in range(1, n+1):
          red["t"][f"c{i}"] = 0

     return red

def reconstruir_camino(padres, fin, inicio):
     camino = [fin]
     nodo = padres[fin]
     while nodo != inicio:
          camino.append(nodo)
          nodo = padres[nodo]
          
     camino.append(inicio)
     return camino[::-1]

def obtener_camino_minimo(residual, fuente, sumidero):
     padres = {} 
     cola = [fuente]
     visitados = {fuente}
     while len(cola) > 0:
          actual = cola.pop(0)
          vecinos_actual = residual[actual]
          for vecino in vecinos_actual.keys():
               if vecino not in visitados and residual[actual][vecino] > 0: 
                    cola.append(vecino)
                    visitados.add(vecino)
                    padres[vecino] = actual

                    if vecino == sumidero:
                         return reconstruir_camino(padres, vecino, fuente)
     return None


def obtener_flujo_maximo(residual, n, fuente, sumidero):
     camino = obtener_camino_minimo(residual, fuente, sumidero)
     while camino != None:
          capacidad_min = float('inf')
          for i in range(len(camino) - 1):
               if residual[camino[i]][camino[i+1]] < capacidad_min:
                    capacidad_min = residual[camino[i]][camino[i+1]]
          
          for i in range(1, len(camino)):
               residual[camino[i-1]][camino[i]] -= capacidad_min
               residual[camino[i]][camino[i-1]] += capacidad_min

          camino = obtener_camino_minimo(residual, fuente, sumidero)

     max_flow = 0
     for i in range(1, n+1):
          max_flow += residual[f"a{i}"][fuente]

     return max_flow, residual

def obtener_backups(red_flujo, n):
    backups = {}
    for i in range(1, n+1):
        backups[f"a{i}"] = []
        for j in range(1, n+1):
            if i != j and f"c{j}" in red_flujo[f"a{i}"]:
                if red_flujo[f"c{j}"][f"a{i}"] == 1:
                    backups[f"a{i}"].append(j)
    return backups

def resolver_backups(D, distancias, k, b):
     if k > b:
          return None

     n = len(distancias)
     red = armar_red_flujo(n, D, distancias, k, b)
     residual = convertir_a_grafo_residual(n, D, distancias, red)
     flujo_max, residual = obtener_flujo_maximo(residual, n, "s", "t")
     if n * k == flujo_max:
          return obtener_backups(residual, n)
     return None