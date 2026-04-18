def crear_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(False)
        matriz.append(fila)
    return matriz
            
def obtener_menor_cantidad_palindromos(palabra):
    n = len(palabra)
    cantidad_de_palindromos = [n] * n
    es_pal = crear_matriz(n)

    for i in range(n):
        es_pal[i][i] = True
    cantidad_de_palindromos[0] = 1

    for i in range(1, n):
        mejor_actual = cantidad_de_palindromos[i-1] + 1
        for j in range(i, -1, -1):
            if palabra[j] == palabra[i]:
                if i - j <= 1:
                    es_pal[j][i] = True
                else:
                    if es_pal[j+1][i-1]:
                        es_pal[j][i] = True

                if es_pal[j][i]:
                    nueva_opcion = cantidad_de_palindromos[j-1] + 1 
                    if j == 0:
                        nueva_opcion = 1
                    
                    mejor_actual = min(mejor_actual, nueva_opcion)
        
        cantidad_de_palindromos[i] = mejor_actual

    return cantidad_de_palindromos[n - 1]
















