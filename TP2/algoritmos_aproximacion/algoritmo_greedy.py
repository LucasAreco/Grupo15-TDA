def hallar_subconjunto_factible(set_a, b_max):
    if sum(set_a) <= b_max: return set_a

    set_ord = sorted(set_a, reverse=True)
    s = []
    t = 0

    for a in set_ord:
        if t + a <= b_max:
           s.append(a)
           t += a
    return s 

