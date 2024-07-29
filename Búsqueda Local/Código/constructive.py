"""Constructive algorithm"""
import time
from insertion      import process_activity
from selection      import rank_job_machines
from selection      import insertion_order
from selection      import activities_order
from reader         import read_txt
from reader         import jobs_char
from reader         import machines_char
from reader         import activities_char
from verification   import work_matrix
# from verification   import intervals
# from verification   import schedule_visual

def constructivo(archivo):
    """Método de solución constructiva"""
    print('Constructivo de ls')
    doc = read_txt(archivo)
    trabajos = jobs_char(doc)
    maquinas = machines_char(doc)
    actividades = activities_char(doc)
    start = time.time()
    rangos   = rank_job_machines(trabajos,maquinas)
    indices  = insertion_order(rangos)
    acts_ind = activities_order(indices,trabajos,actividades,doc[1])
    process_activity(acts_ind,actividades,maquinas,trabajos)
    end = time.time()
    elapsed_time = (end - start)* 1000
    sol = work_matrix(maquinas,int(elapsed_time))
    # u_mat = intervals(trabajos,doc[0],doc[1])
    # schedule_visual(u_mat,doc[1])
    return sol
