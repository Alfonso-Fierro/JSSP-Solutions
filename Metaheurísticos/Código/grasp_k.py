"""Grasp algoithm based on k"""
import time
from insertion          import process_activity
from selection          import rank_job_machines
from selection          import insertion_order
from reader             import read_txt
from reader             import jobs_char
from reader             import machines_char
from verification       import work_matrix
from grasp_k_selection  import restricted_list

def grasp(archivo, iters = 5, k=4):
    """Método de solución grasp"""
    doc = read_txt(archivo)
    trabajos = jobs_char(doc)
    maquinas = machines_char(doc)
    start = time.time()
    rangos   = rank_job_machines(trabajos,maquinas)
    rango  = insertion_order(rangos)
    indices = restricted_list(trabajos,rango,k)
    for i in indices:
        process_activity(trabajos[i],maquinas,trabajos,0)
    end = time.time()
    elapsed_time = (end - start)* 1000
    sol = work_matrix(maquinas,int(elapsed_time))
    for i in range(iters):
        trabajos = jobs_char(doc)
        maquinas = machines_char(doc)
        indices = restricted_list(trabajos,rango,k)
        for i in indices:
            process_activity(trabajos[i],maquinas,trabajos,0)
        end = time.time()
        elapsed_time = (end - start)* 1000
        sol2 = work_matrix(maquinas,int(elapsed_time))
        if sol[-1][0]>sol2[-1][0]:
            sol = sol2
    sol[-1][1] = sol2[-1][1]
    return sol
