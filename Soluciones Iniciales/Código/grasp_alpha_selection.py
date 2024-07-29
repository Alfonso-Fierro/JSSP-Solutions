"""Create restricted candidate list"""
import numpy as np

def restricted_list(trabajos, indices,alpha):
    """Crear lista restringida basada en alpha"""
    rcl = []
    indices_c = indices.copy() #No alterar indices normales
    cost = [] #Lista de tiempos totales
    for i in indices_c:
        cost.append(sum(trabajos[i][1]))
    #Find indices min/max elemet
    max_cost = np.argmax(cost)
    min_cost = np.argmin(cost)

    candidates = bench_list(alpha, cost, max_cost, min_cost) #index of candidates
    selection_order = np.random.choice(candidates,len(candidates),replace=False)
    for i in selection_order:
        rcl.append(indices_c[i])
    for i in rcl:
        if i in indices_c:
            indices_c.remove(i)

    while indices_c:
        cost = [] #Lista de tiempos totales
        for i in indices_c:
            cost.append(sum(trabajos[i][1]))
        #Find indices min/max elemet
        max_cost = np.argmax(cost)
        min_cost = np.argmin(cost)

        candidates = bench_list(alpha, cost, max_cost, min_cost) #index of candidates
        selection_order = np.random.choice(candidates,len(candidates),replace=False)
        for i in selection_order:
            rcl.append(indices_c[i])
        for i in rcl:
            if i in indices_c:
                indices_c.remove(i)


    return rcl

def bench_list(alpha, cost, max_cost, min_cost):
    "Crear sublista para escoger candidatos"
    bench = alpha*(cost[max_cost]-cost[min_cost])+cost[min_cost]
    candidates = []
    for i in enumerate(cost):
        if i[1] <= bench:
            candidates.append(i[0])
    return candidates
