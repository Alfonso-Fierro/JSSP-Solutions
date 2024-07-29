"""Solutions"""
import time
from insertion      import process_activity
from selection      import rank_job_machines
from selection      import insertion_order
from selection      import activities_order
from selection      import frwrd_insertion
from selection      import back_insertion
from selection      import interchange
from reader         import read_txt
from reader         import jobs_char
from reader         import machines_char
from reader         import activities_char
from verification   import work_matrix
from verification   import intervals
from verification   import schedule_visual

five_min = 60000

def fi_back_insertion(archivo):
    """Método de solución constructiva"""
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
    sol = work_matrix(maquinas,elapsed_time)
    makespan = sol[-1][0]

    for i in range(doc[1]*doc[0]):
        i_nghbr = back_insertion(acts_ind,actividades,i)
        for change in i_nghbr:
            trabajos = jobs_char(doc)
            maquinas = machines_char(doc)
            process_activity(change,actividades,maquinas,trabajos)
            end = time.time()
            elapsed_time = (end - start)* 1000
            c_sol = work_matrix(maquinas,elapsed_time)
            c_makespan = c_sol[-1][0]
            if elapsed_time > five_min:
                return sol
            if c_makespan < makespan:
                #print(c_makespan)
                sol = c_sol.copy()
                makespan = sol[-1][0]
                acts_ind = change.copy()
                break
    end = time.time()
    elapsed_time = (end - start)* 1000
    sol[-1][1] = elapsed_time
    # u_mat = intervals(trabajos,doc[0],doc[1])
    # schedule_visual(u_mat,doc[1])
    return sol

def fi_forward_insertion(archivo):
    """Método de solución constructiva"""
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
    sol = work_matrix(maquinas,elapsed_time)
    makespan = sol[-1][0]

    for i in range(doc[1]*doc[0]):
        i_nghbr = frwrd_insertion(acts_ind,actividades,i)
        for change in i_nghbr:
            trabajos = jobs_char(doc)
            maquinas = machines_char(doc)
            process_activity(change,actividades,maquinas,trabajos)
            end = time.time()
            elapsed_time = (end - start)* 1000
            c_sol = work_matrix(maquinas,elapsed_time)
            c_makespan = c_sol[-1][0]
            if elapsed_time > five_min:
                return sol
            if c_makespan < makespan:
                #print(c_makespan)
                sol = c_sol.copy()
                makespan = sol[-1][0]
                acts_ind = change.copy()
                break
    end = time.time()
    elapsed_time = (end - start)* 1000
    sol[-1][1] = elapsed_time
    # u_mat = intervals(trabajos,doc[0],doc[1])
    # schedule_visual(u_mat,doc[1])
    return sol

def fi_interchange(archivo):
    """Método de solución constructiva"""
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
    sol = work_matrix(maquinas,elapsed_time)
    makespan = sol[-1][0]

    for i in range(doc[1]*doc[0]):
        i_nghbr = interchange(acts_ind,actividades,i)
        for change in i_nghbr:
            trabajos = jobs_char(doc)
            maquinas = machines_char(doc)
            process_activity(change,actividades,maquinas,trabajos)
            end = time.time()
            elapsed_time = (end - start)* 1000
            c_sol = work_matrix(maquinas,elapsed_time)
            c_makespan = c_sol[-1][0]
            if elapsed_time > five_min:
                return sol
            if c_makespan < makespan:
                #print(c_makespan)
                sol = c_sol.copy()
                makespan = sol[-1][0]
                acts_ind = change.copy()
                break
    end = time.time()
    elapsed_time = (end - start)* 1000
    sol[-1][1] = elapsed_time
    # u_mat = intervals(trabajos,doc[0],doc[1])
    # schedule_visual(u_mat,doc[1])
    return sol

def bi_back_insertion(archivo):
    """Método de solución constructiva"""
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
    sol = work_matrix(maquinas,elapsed_time)
    makespan = sol[-1][0]

    for i in range(doc[1]*doc[0]):
        i_nghbr = back_insertion(acts_ind,actividades,i)
        for change in i_nghbr:
            trabajos = jobs_char(doc)
            maquinas = machines_char(doc)
            process_activity(change,actividades,maquinas,trabajos)
            end = time.time()
            elapsed_time = (end - start)* 1000
            c_sol = work_matrix(maquinas,elapsed_time)
            c_makespan = c_sol[-1][0]
            if elapsed_time > five_min:
                return sol
            if c_makespan < makespan:
                #print(c_makespan)
                sol = c_sol.copy()
                makespan = sol[-1][0]
                acts_ind = change.copy()
    end = time.time()
    elapsed_time = (end - start)* 1000
    sol[-1][1] = elapsed_time
    # u_mat = intervals(trabajos,doc[0],doc[1])
    # schedule_visual(u_mat,doc[1])
    return sol

def bi_forward_insertion(archivo):
    """Método de solución constructiva"""
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
    sol = work_matrix(maquinas,elapsed_time)
    makespan = sol[-1][0]

    for i in range(doc[1]*doc[0]):
        i_nghbr = frwrd_insertion(acts_ind,actividades,i)
        for change in i_nghbr:
            trabajos = jobs_char(doc)
            maquinas = machines_char(doc)
            process_activity(change,actividades,maquinas,trabajos)
            end = time.time()
            elapsed_time = (end - start)* 1000
            c_sol = work_matrix(maquinas,elapsed_time)
            c_makespan = c_sol[-1][0]
            if elapsed_time > five_min:
                return sol
            if c_makespan < makespan:
                #print(c_makespan)
                sol = c_sol.copy()
                makespan = sol[-1][0]
                acts_ind = change.copy()
    end = time.time()
    elapsed_time = (end - start)* 1000
    sol[-1][1] = elapsed_time
    # u_mat = intervals(trabajos,doc[0],doc[1])
    # schedule_visual(u_mat,doc[1])
    return sol

def bi_interchange(archivo):
    """Método de solución constructiva"""
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
    sol = work_matrix(maquinas,elapsed_time)
    makespan = sol[-1][0]

    for i in range(doc[1]*doc[0]):
        i_nghbr = interchange(acts_ind,actividades,i)
        for change in i_nghbr:
            trabajos = jobs_char(doc)
            maquinas = machines_char(doc)
            process_activity(change,actividades,maquinas,trabajos)
            end = time.time()
            elapsed_time = (end - start)* 1000
            c_sol = work_matrix(maquinas,elapsed_time)
            c_makespan = c_sol[-1][0]
            if elapsed_time > five_min:
                return sol
            if c_makespan < makespan:
                #print(c_makespan)
                sol = c_sol.copy()
                makespan = sol[-1][0]
                acts_ind = change.copy()
    end = time.time()
    elapsed_time = (end - start)* 1000
    sol[-1][1] = elapsed_time
    # u_mat = intervals(trabajos,doc[0],doc[1])
    # schedule_visual(u_mat,doc[1])
    return sol
