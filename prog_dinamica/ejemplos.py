from numero_min_palindromos import obtener_menor_cantidad_palindromos

def leer_casos(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    return lineas


def probar_casos(nombre_archivo):
    casos = leer_casos(nombre_archivo)
    for caso in casos:
        caso = caso.strip()
        resultado = obtener_menor_cantidad_palindromos(caso)
        print(f"Para {caso}: {resultado}")

probar_casos("ejemplos.txt")