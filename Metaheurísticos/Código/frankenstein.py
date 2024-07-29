# Generate multiple initial solutions from the GRASP algorithm
"""Solutions"""
import time
import numpy        as np
from local_search   import local_search_1
from selection      import rank_job_machines
from selection      import insertion_order
from selection      import activities_order
from reader         import read_txt
from reader         import jobs_char
from reader         import machines_char
from reader         import activities_char
from verification   import work_matrix
from verification   import precedence_matrix
from constructive   import makespan
from grasp_k_selection import restricted_list
def frankenstein(archivo, ninis, t_l, T_0, T_f):
    """Método de solución con múltiples estrategias"""
    doc = read_txt(archivo)
    trabajos = jobs_char(doc)
    maquinas = machines_char(doc)
    actividades = activities_char(doc)
    rangos   = rank_job_machines(trabajos,maquinas)
    indices  = insertion_order(rangos)
    init_ordrs = []
    for i in range(ninis):
        init_ordrs.append(restricted_list(trabajos,indices))
    
    init_sols = []
    for order in init_ordrs:
        init_sols.append(activities_order(order,trabajos,actividades,doc[1]))
    

    start = time.time()
    now   = time.time()
    lapse = now-start
    L = 100
    s = init_sols[0].copy()
    s_star = s.copy()
    while (lapse < t_l) and init_sols:
        s = init_sols[0].copy()
        del init_sols[0]
        s_star = s.copy()
        while init_sols:
            T = T_0
            while T > T_f:
                l=0
                while l < L:
                    l = l+1
                    s_prime  = local_search_1(s,doc,actividades,t_l)[1]
                    trs1     = jobs_char(doc)
                    mqs1     = machines_char(doc)
                    s_prime_ms = makespan(trs1,mqs1,actividades,s_prime)[-1][0]
                    print(s_prime)
                    trs2     = jobs_char(doc)
                    mqs2     = machines_char(doc)
                    s_ms       = makespan(trs2,mqs2,actividades,s)[-1][0]
                    d = s_prime_ms-s_ms
                    if d < 0:
                        s = s_prime.copy()
                        trs3     = jobs_char(doc)
                        mqs3     = machines_char(doc)
                        s_star_ms = makespan(trs3,mqs3,actividades,s_star)[-1][0]
                        if s_ms < s_star_ms:
                            s_star = s.copy()
                    else:
                        random = np.random.rand()
                        if random < np.exp(-d/T):
                            s = s_prime.copy()
                T = 0.6*T
    tr     = jobs_char(doc)
    mq     = machines_char(doc)
    sol = makespan(tr,mq,actividades,s_star)
    return sol