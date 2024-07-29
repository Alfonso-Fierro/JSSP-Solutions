"""Insert job in machines"""
import numpy as np
from verification import work_matrix
from verification import intervals
from verification import schedule_visual
    #Jobs must be added to every machine, following their sequence

def caut_rel_arral_time(job,machine):
    """Calculate time machine finishes job queued"""
    #JOB -> (index, [times],[sequence],[arrival_times])
    #MACHINE -> (index, [queue], [release_times])
    #calcular release time y arrival time (son lo mismo)
    arrive_index = np.where(job[2]==machine[0])[0][0]
    q_index      = np.where(np.array(machine[1])==job[0])[0][0]
    arrival_time = job[3][arrive_index]
    job_time     = job[1][arrive_index]
    if q_index == 0:
        #processing the first job
        release_time = arrival_time+job_time
        machine[2][q_index] = release_time
        job[3][arrive_index+1] = release_time
    else:
        previous_release_time = machine[2][q_index-1]
        release_time = max(previous_release_time,arrival_time)+job_time
        machine[2][q_index] = release_time #Finish time for this job
        job[3][arrive_index+1] = release_time #Arrival time to next machine

def cautive_append(job,machine,jobs_set):
    """Insert job in machine queue"""
    #JOB -> (index, [times m],[sequence m],[arrival_times m])
    #MACHINE -> (index, [queue n], [release_times n])
    arrival_index = np.where(job[2]==machine[0])[0][0]
    arrival_time = job[3][arrival_index]
    queue = machine[1]
    copy_release = np.copy(machine[2]) #Copy original list

    q_index = 0
    for q_job in queue:
        #find at what time q_job arrived to the machine
        q_job_index = np.where(jobs_set[q_job][2]==machine[0])[0][0]
        q_job_arr = jobs_set[q_job][3][q_job_index+1]-jobs_set[q_job][1][q_job_index]
        white_space = q_job_arr - machine[2][q_index-1]
        if q_index == 0:
            white_space = q_job_arr
        if arrival_time >= q_job_arr:
            #the job in the queue arrived earlier than us
            q_index += 1
        elif job[1][arrival_index]>white_space:
            q_index += 1
        else:
            break
    machine[1].insert(q_index,int(job[0]))
    caut_rel_arral_time(job,machine)
    change_jobs = queue[q_index+1:]
    for i in range(len(change_jobs)):
        machine[2][q_index+1+i]=copy_release[q_index+i]

def process_activity(order,activities,machine_set,job_set):
    """Initialize every job in their machine"""
    #JOB -> (index, [times m],[sequence m],[arrival_times m])
    #MACHINE -> (index, [queue n], [release_times n])
    #start_machines = [[] for i in range(machines[-1][0]+1)]
    for element in order:
        act = activities[element]
        job_p = job_set[act[0]]
        machine = machine_set[act[1]]
        cautive_append(job_p,machine,job_set)
        # sol = work_matrix(machine_set,int(1))
        # u_mat = intervals(job_set,len(machine_set),len(job_set))
        # schedule_visual(u_mat,len(job_set))
