import random
import json
import math


def generar_caso_hard_disperso(n, B, i=0, classes=3, frac=0.2, eps=0.01):
    """
    Variante del algoritmo de generación para crear casos "hard dispersos" con una mezcla
    de números grandes basados en B y números pequeños. Esto asegura que el algoritmo tenga que lidiar con una amplia gama de valores, lo que puede aumentar la dificultad de encontrar soluciones óptimas.

    Algoritmo original: https://github.com/JorikJooken/knapsackProblemInstances/blob/master/generator.cpp
    """
    conjunto = []
    
    # Escalamos el rango de los números chicos proporcionalmente a N
    # para garantizar que haya suficiente espacio numérico
    small = max(20, n // 2) 
    
    amount_small = int(n * frac)
    remaining = n - amount_small
    classes_adjusted = max(2, classes)
    am1 = remaining // (classes_adjusted - 1)
    
    denominator = 2.0
    
    # 1. Generar clases exponenciales (elementos grandes dispersos basados en B)
    for j in range(classes_adjusted - 1):
        for _ in range(am1):
            num = random.randint(1, small)
            elemento = int(((1.0 / denominator) + eps) * B + num)
            
            # mantenerlo menor o igual a B
            if 0 < elemento <= B:
                conjunto.append(elemento)
        denominator *= 2
        
    # 2. Rellenar lo que falta con números chicos
    while len(conjunto) < n:
        elemento = random.randint(1, small)
        conjunto.append(elemento)

    # Mezclamos para perder el orden de generación
    random.shuffle(conjunto)
    
    suma_total = sum(conjunto)
    
    # Guardar archivo
    path = f"datasets/caso_hard_disperso_{n}_{B}_{i}.json"
    with open(path, "w") as f:
        json.dump({"conjunto": conjunto, "target": B, "suma_total": suma_total}, f)
        
    return path

def generar_caso_aleatorio(n, B, i=0):
    conjunto = [random.randint(1, B) for _ in range(n)]
    path = f"datasets/caso_aleatorio_{n}_{B}_{i}.json"
    with open(path, "w") as f:
        json.dump({"conjunto": conjunto, "target": B, "suma_total": sum(conjunto)}, f)
    return path

def generar_caso_trivial(n, B, i=0):
    conjunto = [random.randint(1, B) for _ in range(n)]

    B = sum(conjunto) + random.randint(1, 10)  # Aseguramos que B sea mayor que la suma de A
    path = f"datasets/caso_trivial_{n}_{B}_{i}.json"
    with open(path, "w") as f:
        json.dump({"conjunto": conjunto, "target": B, "suma_total": sum(conjunto)}, f)
    return path

def generar_caso_general(n, i=0):
    conjunto = sorted(list(set(random.randint(1, n ** 2) for _ in range(n * 2))))[:n]
    random.shuffle(conjunto)

    k = random.randint(max(2, n // 3), max(2, n // 2))
    subconjunto_solucion = random.sample(conjunto, k)
    target = int(sum(subconjunto_solucion) * random.uniform(0.5, 0.8))

    path = f"datasets/caso_general_{n}_{target}_{i}.json"
    with open(path, "w") as f:
        json.dump({"conjunto": conjunto, "target": target, "suma_total": sum(conjunto)}, f)
    return path

TAMAÑOS = [10, 50, 100, 500, 1000]
TIPOS_TARGET = ["trivial", "general", "aleatorio", "hard_disperso"]

def generar_datasets():
    datasets = {tipo: [] for tipo in TIPOS_TARGET}
    
    for n in TAMAÑOS:
        for tipo in TIPOS_TARGET:
            print(f"Generando caso para tipo: {tipo}, tamaño: {n}")
            b_base = n * random.randint(500, 1000)
            if tipo == "aleatorio":
                path = generar_caso_aleatorio(n=n, B=b_base)
            elif tipo == "hard_disperso":
                path = generar_caso_hard_disperso(n=n, B=b_base)
            elif tipo == "trivial":
                path = generar_caso_trivial(n=n, B=b_base)
            elif tipo == "general":
                path = generar_caso_general(n=n)
    
            datasets[tipo].append(path)
    
    return datasets

if __name__ == "__main__":
    generar_datasets()