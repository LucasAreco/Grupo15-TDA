import time
import math

def pesar(monedas, inicio, fin):
    return sum(monedas[inicio:fin + 1])

def encontrar_moenda_falsa(monedas, inicio, fin):
    if inicio == fin:
        return inicio
    
    n = fin - inicio + 1

    tamanio_grupo = (n + 2) // 3

    fin_a = inicio + tamanio_grupo - 1
    inicio_b = fin_a + 1
    fin_b = inicio_b + tamanio_grupo - 1
    inicio_c = fin_b + 1

    peso_a = pesar(monedas, inicio, fin_a)
    peso_b = pesar(monedas, inicio_b, fin_b)
    
    if peso_a < peso_b:
        return encontrar_moenda_falsa(monedas, inicio, fin_a)
    elif peso_b < peso_a:
        return encontrar_moenda_falsa(monedas, inicio_b, fin_b)
    else:
        return encontrar_moenda_falsa(monedas, inicio_c, fin)
    

def realizar_mediciones():
    n = [100, 500, 1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
    print(f"{'N':>8} | {'Pesadas':>8} | {'Tiempo (s)':>15} | {'Muestras'}")
    print("-" * 60)

    for i in n:
        bolsa = [1] * i
        bolsa[i // 2] = 0
        
        pesadas = math.ceil(math.log(i, 3))
        muestras = 0
        inicio_medicion = time.perf_counter()
        while (time.perf_counter() - inicio_medicion) < 5.0:
            encontrar_moenda_falsa(bolsa, 0, i - 1)
            muestras += 1
        fin_medicion = time.perf_counter()
        
        tiempo_total = fin_medicion - inicio_medicion
        tiempo = tiempo_total / muestras
        
        print(f"{i:8d} | {pesadas:8d} | {tiempo:15.8f} | {muestras}")

realizar_mediciones()