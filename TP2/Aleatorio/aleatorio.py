import csv
import os
import random


def leer_dataset(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        n = int(next(archivo).strip())

        lector = csv.reader(archivo)
        aristas = [(int(u), int(v)) for u, v in lector if u and v]

    return n, aristas


def contar_satisfechas(aristas, color):
    return sum(1 for u, v in aristas if color[u] != color[v])


def coloreo_aleatorio(n, aristas):
    color = [random.randint(0, 2) for _ in range(n)]
    return contar_satisfechas(aristas, color)


def calcular_c(n, aristas):
    if n > 13:
        # Si el grafo es grande, no podemos sacar c* exacto por fuerza bruta.
        return None

    total_coloreos = 3**n
    mejor = 0

    for numero in range(total_coloreos):
        color = []
        resto = numero
        for _ in range(n):
            color.append(resto % 3)
            resto //= 3

        satisfechas = contar_satisfechas(aristas, color)
        if satisfechas > mejor:
            mejor = satisfechas

    return mejor


def main():
    carpeta = "datasets"
    if not os.path.exists(carpeta):
        print(f"Error: La carpeta '{carpeta}' no existe.")
        return

    archivos = sorted([f for f in os.listdir(carpeta) if f.endswith(".csv")])
    repeticiones = 50000
    resultados = []

    for nombre_archivo in archivos:
        ruta = os.path.join(carpeta, nombre_archivo)
        n, aristas = leer_dataset(ruta)
        m = len(aristas)

        c = calcular_c(n, aristas)

        cota_referencia = (2 / 3) * c if c is not None else (2 / 3) * m

        suma_satisfechas = sum(
            coloreo_aleatorio(n, aristas) for _ in range(repeticiones)
        )
        promedio = suma_satisfechas / repeticiones

        cumple = "SI" if promedio >= cota_referencia else "NO"

        c_str = str(c) if c is not None else "O(3^n) indef."
        print(
            f"{nombre_archivo} | n={n}, m={m} | c*={c_str} | "
            f"Cota={cota_referencia:.3f} | Promedio={promedio:.3f} | Cumple={cumple}"
        )

        resultados.append(
            {
                "dataset": nombre_archivo,
                "n": n,
                "m": m,
                "c": c_str,
                "cota": round(cota_referencia, 3),
                "promedio": round(promedio, 3),
                "cumple": cumple,
            }
        )

    with open("resultados.csv", "w", newline="", encoding="utf-8") as salida:
        campos = ["dataset", "n", "m", "c", "cota", "promedio", "cumple"]
        escritor = csv.DictWriter(salida, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(resultados)

if __name__ == "__main__":
    main()