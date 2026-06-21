import pulp

def solve():
    stops = {
        'A': 30,
        'B80': 80,
        'B120': 120,
        'C': 75,
        'D': 50,
        'E': 2,
        'F': 20,
        'G': 100,
    }
    profit = {
        'A': 50000,
        'B80': 100000,
        'B120': 120000,
        'C': 100000,
        'D': 80000,
        'E': 5000,
        'F': 40000,
        'G': 90000,
    }

    prob = pulp.LpProblem('TP2_Problema1', pulp.LpMaximize)

    # variables binarias
    x = {k: pulp.LpVariable(f'x_{k}', cat='Binary') for k in profit}

    # funcion objetivo
    prob += pulp.lpSum(profit[k] * x[k] for k in profit)

    # restriccion de plazas totales (200 paradas)
    prob += pulp.lpSum(stops[k] * x[k] for k in stops) <= 200

    # restriccion de exclusividad entre B80 y B120: no pueden estar simultaneamente
    prob += x['B80'] + x['B120'] <= 1

    # restriccion de exclusividad entre A y D: no pueden estar simultaneamente
    prob += x['A'] + x['D'] <= 1

    # resolver
    solver = pulp.PULP_CBC_CMD(msg=False)
    prob.solve(solver)

    chosen = {k: int(pulp.value(x[k])) for k in x}
    total_profit = pulp.value(prob.objective)
    total_stops = sum(stops[k] * chosen[k] for k in chosen)

    out_lines = []
    out_lines.append('Solución al problema TP2 - Problema 1')
    out_lines.append('Seleccionados:')
    for k in sorted(chosen):
        if chosen[k]:
            out_lines.append(f'- {k}: beneficio ${profit[k]} / paradas {stops[k]}')
    out_lines.append(f'Total beneficio: ${int(total_profit)}')
    out_lines.append(f'Total paradas usadas: {total_stops} / 200')

    result_text = '\n'.join(out_lines)
    print(result_text)

    with open('resultados.txt', 'w') as f:
        f.write(result_text)

if __name__ == '__main__':
    solve()
