import time
from constructive import makespan
from reader         import jobs_char
from reader         import machines_char
from local_search   import local_search_1
from local_search   import local_search_2
from local_search   import local_search_3

def VND(initial_sol, doc, actividades, t_l):
    s = initial_sol
    start = time.time()
    
    sol1 = local_search_1(initial_sol, doc, actividades, t_l)
    now = time.time()
    lapse = now - start
    if lapse > t_l:
        trabajos = jobs_char(doc)
        maquinas = machines_char(doc)
        return makespan(trabajos,maquinas,actividades,s)
    s = sol1[-1]

    sol2 = local_search_2(s, doc, actividades, t_l)
    now = time.time()
    lapse = now - start
    if lapse > t_l:
        trabajos = jobs_char(doc)
        maquinas = machines_char(doc)
        return makespan(trabajos,maquinas,actividades,s)
    s = sol2[-1]

    sol3 = local_search_3(s, doc, actividades, t_l)
    now = time.time()
    lapse = now - start
    if lapse > t_l:
        trabajos = jobs_char(doc)
        maquinas = machines_char(doc)
        return makespan(trabajos,maquinas,actividades,s)
    s = sol3[0]
    return s


