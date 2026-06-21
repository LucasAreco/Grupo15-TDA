import sys
import os
import glob
import json
from time import time

from algoritmo_greedy import hallar_subconjunto_factible
from generador import generar_datasets

def mostrar_resultado_individual(path_archivo):
    """Procesa un único archivo .json y muestra el resultado formateado."""
    if not os.path.exists(path_archivo):
        print(f"ERROR: El archivo '{path_archivo}' no existe.")
        return

    with open(path_archivo, "r") as f:
        data = json.load(f)
    
    A = data["conjunto"]
    B = data["target"]

    print("\n" + "="*50)
    print("EVALUACIÓN DE INSTANCIA INDIVIDUAL".center(50))
    print("="*50)
    print(f"Archivo:    {os.path.basename(path_archivo)}")
    print(f"Tamaño N:   {len(A)}")
    print(f"Target (B): {B:,}")
    print(f"Conjunto A: {A if len(A) <= 15 else str(A[:15])[:-1] + '... (truncado)'}")
    print("-"*50)

    inicio = time()
    solucion = hallar_subconjunto_factible(A, B)
    tiempo_us = (time() - inicio) * 1_000_000

    suma_alcanzada = sum(solucion)
    gap_absoluto = B - suma_alcanzada
    gap_porc = (gap_absoluto / B) * 100 if B > 0 else 0

    print("RESULTADOS DE LA OPTIMIZACIÓN:".center(50))
    print("-"*50)
    print(f"Suma máxima alcanzada: {suma_alcanzada:,}")
    print(f"Gap / Error absoluto:  {gap_absoluto:,}")
    print(f"Gap porcentual:        {gap_porc:.2f}%")
    print(f"Tiempo de ejecución:   {tiempo_us:.2f} μs")
    print(f"Subconjunto factible hallado:  {solucion if len(solucion) <= 15 else str(solucion[:15])[:-1] + '... (truncado)'}")
    print("="*50 + "\n")


def obtener_archivos_datasets():
    """Busca todos los archivos .json en la carpeta 'datasets/' y devuelve sus rutas."""
    archivos = glob.glob("datasets/*.json")
    if not archivos:
        print("WARNING: No se encontraron archivos .json en la carpeta 'datasets/'.")
        print("Generando algunos casos de prueba automáticamente...")
        generar_datasets()
        archivos = glob.glob("datasets/*.json")
    return sorted(archivos)

def procesar_archivo(path_archivo, tabla_datos):
    nombre_archivo = os.path.basename(path_archivo)
        
    partes = nombre_archivo.split('_')
    if len(partes) >= 3:
        tipo = " ".join([p for p in partes[1:-3]]).title()
    else:
        tipo = "Desconocido"

    with open(path_archivo, "r") as f:
        data = json.load(f)
    
    A = data["conjunto"]
    B = data["target"]

    inicio = time()
    solucion = hallar_subconjunto_factible(A, B)
    tiempo_us = (time() - inicio) * 1_000_000
    
    suma_alcanzada = sum(solucion)
    gap_porc = ((B - suma_alcanzada) / B) * 100 if B > 0 else 0

    tabla_datos.append([
        tipo,
        len(A),
        f"{B}",
        f"{suma_alcanzada}",
        f"{gap_porc:.2f}",
        f"{tiempo_us:.2f}"
    ])

def procesar_carpeta_datasets():
    """Busca todos los .json de la carpeta datasets y arma una tabla resumen."""

    archivos = obtener_archivos_datasets()
    if not archivos:
        print("ERROR: No hay archivos para procesar.")
        return

    print("Procesando todos los datasets de la carpeta...")
    
    tabla_datos = []

    for path in sorted(archivos):
        procesar_archivo(path, tabla_datos)

    headers = [
        "TipodeInstancia", 
        "N", 
        "Target(B)", 
        "SumaConseguida", 
        "Gap(%)", 
        "Tiempo(μs)"
    ]

    resultado = [headers] + tabla_datos

    with open("resultados/resultados_resumen.csv", "w") as f:
        for fila in resultado:
            f.write(";".join(f'{col}' for col in fila) + "\n")

if __name__ == "__main__":
    # Verificamos si se pasó un parámetro por consola
    # sys.argv[0] es el nombre del script (main.py), sys.argv[1] sería el archivo
    if len(sys.argv) > 1:
        archivo_parametro = sys.argv[1]
        mostrar_resultado_individual(archivo_parametro)
    else:
        procesar_carpeta_datasets()