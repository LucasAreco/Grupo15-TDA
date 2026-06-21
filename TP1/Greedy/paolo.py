def dijkstra_paolo():

    N = int(input("INGRESE EL NUMERO DE VERTICES: "))
    print()
    
    COST = [[0] * (N + 1) for _ in range(N + 1)]
    DIST = [0] * (N + 1)
    SOL = [0] * (N + 1)
    
    print("INGRESE EL CUADRO DE COSTOS (INGRESE 0,0 PARA TERMINAR)\n")
    
    while True:
        entrada = input("EL EJE (A,B): ")
        A, B = map(int, entrada.split(','))
        if A == 0:
            break
        costo = int(input("COSTO DEL EJE: "))
        COST[A][B] = costo

    for I in range(1, N + 1):
        for J in range(1, N + 1):
            if COST[I][J] == 0:
                COST[I][J] = 15000

    for I in range(1, N + 1):
        for J in range(1, I + 1):
            menor_costo = min(COST[I][J], COST[J][I])
            COST[I][J] = menor_costo
            COST[J][I] = menor_costo

    while True:
        V = int(input("\nINGRESE EL VERTICE DE SALIDA: "))

        for I in range(1, N + 1):
            DIST[I] = COST[V][I]
            SOL[I] = 0

        SOL[V] = 1
        DIST[V] = 0
        
        for _ in range(1, N): 
            min_dist = 15000 
            U = -1
            
            for J in range(1, N + 1):
                if DIST[J] <= min_dist and SOL[J] == 0:
                    min_dist = DIST[J]
                    U = J
                
            SOL[U] = 1
            
            for J in range(1, N + 1):
                if DIST[J] >= (DIST[U] + COST[U][J]):
                    DIST[J] = DIST[U] + COST[U][J]

        print(f"\n{'SALIDA':<10} {'LLEGADA':<10} {'DISTANCIA'}")
        for I in range(1, N + 1):
            if DIST[I] < 15000:
                print(f"{V:<10} {I:<10} {DIST[I]}")

        res = input("\nOTRA VEZ? (SI/NO): ").strip().upper()
        if res == "NO":
            break
            
        for I in range(1, N + 1):
            SOL[I] = 0
            DIST[I] = 0

if __name__ == "__main__":
    dijkstra_paolo()