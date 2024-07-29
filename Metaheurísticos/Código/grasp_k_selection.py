"""Create restricted candidate list"""
import numpy as np


def restricted_list(trabajos, indices, k=4):
    """Crear lista restringida basada en alpha"""
    rcl = []
    indices_c = indices.copy()  # do not change regular index
    cost = []  # total time list
    for i in indices_c:
        cost.append(sum(trabajos[i][1]))
    # Find k best elemets
    candidates = bench_list(k, cost)  # index of candidates
    selection_order = np.random.choice(candidates, len(candidates), replace=False)
    for i in selection_order:
        rcl.append(indices_c[i])
    for i in rcl:
        if i in indices_c:
            indices_c.remove(i)

    while indices_c:
        cost = []
        for i in indices_c:
            cost.append(sum(trabajos[i][1]))
        candidates = bench_list(k, cost)
        selection_order = np.random.choice(candidates, len(candidates), replace=False)
        for i in selection_order:
            rcl.append(indices_c[i])
        for i in rcl:
            if i in indices_c:
                indices_c.remove(i)
    return rcl


def bench_list(k, cost):
    "Create list to choose k candidates"
    candidates = []
    for i in enumerate(cost):
        if i[0] < k:
            candidates.append(i[0])
    return candidates
