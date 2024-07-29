"""Solutions"""
import time
from insertion      import process_activity
from selection      import back_insertion, frwrd_insertion, rank_job_machines
from selection      import insertion_order
from selection      import activities_order
from selection      import interchange
from selection      import priority_search
from reader         import read_txt
from reader         import jobs_char
from reader         import machines_char
from reader         import activities_char
from verification   import work_matrix
from verification   import precedence_matrix
from constructive   import makespan
from verification   import intervals
from verification   import schedule_visual

five_min = 60000

def fi_back_insertion(archivo):
    """Método de solución constructiva"""
    doc = read_txt(archivo)
    trabajos = jobs_char(doc)
    maquinas = machines_char(doc)
    actividades = activities_char(doc)
    prioridades = priority_search(trabajos,actividades)
    prec_matrix = precedence_matrix(actividades)
    start = time.time()
    rangos   = rank_job_machines(trabajos,maquinas)
    indices  = insertion_order(rangos)
    acts_ind = activities_order(indices,trabajos,actividades,doc[1])
    process_activity(acts_ind,actividades,maquinas,trabajos)
    end = time.time()
    elapsed_time = (end - start)* 1000
    sol = work_matrix(maquinas,elapsed_time)
    makespan = sol[-1][0]
    start = time.time()
    for i in prioridades:
        i_nghbr = interchange(acts_ind,actividades,i,prec_matrix)
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

def local_search_1(initial_sol, doc, actividades, t_l):
    t_l = t_l*1000
    jobs = jobs_char(doc)
    machines = machines_char(doc)
    prec_matrix = precedence_matrix(actividades)
    matches  = priority_search(jobs,actividades)

    sol = makespan(jobs, machines, actividades,initial_sol)
    sol_msp = sol[-1][0]

    start = time.time() 
    
    now = time.time()
    tiempo = now-start
    while (tiempo < t_l) and matches:
        match = matches[0] #Initialize Iterated local search
        del matches[0]
        neighb  = interchange(initial_sol,actividades,match,prec_matrix)
        
        for s_prime in neighb:
            jobs = jobs_char(doc)
            machines = machines_char(doc)
            sol_prime = makespan(jobs, machines, actividades,s_prime)
            prime_msp = sol_prime[-1][0]
            now = time.time()
            tiempo = now-start

            if tiempo > t_l:
                return [sol, initial_sol]
            elif prime_msp < sol_msp:
                #print(prime_msp)
                initial_sol = s_prime.copy()
                sol = sol_prime
                sol_msp = prime_msp
                break #First improvement
            now = time.time()
            tiempo = now-start
    return [sol, initial_sol]

def local_search_2(initial_sol, doc, actividades, t_l):
    t_l = t_l*1000
    jobs = jobs_char(doc)
    machines = machines_char(doc)
    prec_matrix = precedence_matrix(actividades)
    matches  = priority_search(jobs,actividades)

    sol = makespan(jobs, machines, actividades,initial_sol)
    sol_msp = sol[-1][0]

    start = time.time() 
    
    now = time.time()
    tiempo = now-start
    while (tiempo < t_l) and matches:
        match = matches[0] #Initialize local search
        del matches[0]
        neighb  = frwrd_insertion(initial_sol,actividades,match,prec_matrix)
        
        for s_prime in neighb:
            jobs = jobs_char(doc)
            machines = machines_char(doc)
            sol_prime = makespan(jobs, machines, actividades,s_prime)
            prime_msp = sol_prime[-1][0]
            now = time.time()
            tiempo = now-start

            if tiempo > t_l:
                return [sol, initial_sol]
            elif prime_msp < sol_msp:
                #print(prime_msp)
                initial_sol = s_prime
                sol = sol_prime
                sol_msp = prime_msp
                break #First improvement
            now = time.time()
            tiempo = now-start
    return [sol, initial_sol]

def local_search_3(initial_sol, doc, actividades, t_l):
    t_l = t_l*1000
    jobs = jobs_char(doc)
    machines = machines_char(doc)
    prec_matrix = precedence_matrix(actividades)
    matches  = priority_search(jobs,actividades)

    sol = makespan(jobs, machines, actividades,initial_sol)
    sol_msp = sol[-1][0]

    start = time.time() 
    
    now = time.time()
    tiempo = now-start
    while (tiempo < t_l) and matches:
        match = matches[0] #Initialize local search
        del matches[0]
        neighb  = back_insertion(initial_sol,actividades,match,prec_matrix)
        
        for s_prime in neighb:
            jobs = jobs_char(doc)
            machines = machines_char(doc)
            sol_prime = makespan(jobs, machines, actividades,s_prime)
            prime_msp = sol_prime[-1][0]
            now = time.time()
            tiempo = now-start

            if tiempo > t_l:
                return [sol, initial_sol]
            elif prime_msp < sol_msp:
                #print(prime_msp)
                initial_sol = s_prime
                sol = sol_prime
                sol_msp = prime_msp
                break #First improvement
            now = time.time()
            tiempo = now-start
    return [sol, initial_sol]