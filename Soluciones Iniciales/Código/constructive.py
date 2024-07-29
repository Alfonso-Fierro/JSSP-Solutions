"""Constructive algorithm"""
import time
from insertion      import process_line
from selection      import rank_job_machines
from selection      import insertion_order
from reader         import read_txt
from reader         import jobs_char
from reader         import machines_char
from verification   import work_matrix
# from verification   import intervals
# from verification   import schedule_visual
def constructivo(archivo):
    """Método de solución constructiva"""
    doc = read_txt(archivo)
    trabajos = jobs_char(doc)
    maquinas = machines_char(doc)
    start = time.time()
    rangos   = rank_job_machines(trabajos,maquinas)
    indices  = insertion_order(rangos)
    for i in indices:
        process_line(trabajos[i],maquinas,trabajos,0)
    end = time.time()
    elapsed_time = (end - start)* 1000
    sol = work_matrix(maquinas,int(elapsed_time))
    # u_mat = intervals(trabajos,doc[0],doc[1])
    # schedule_visual(u_mat,doc[1])
    return sol
