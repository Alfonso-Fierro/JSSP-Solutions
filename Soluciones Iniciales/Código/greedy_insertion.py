"""Insertion based constructive algorithm"""

import numpy as np
    #Jobs must be added to every machine, following their sequence

def release_arrival_time(job,machine):
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
        if max(arrival_time,previous_release_time)==arrival_time:
            release_time = arrival_time+job_time
            machine[2][q_index] = release_time
            job[3][arrive_index+1] = release_time
        else:
            release_time = previous_release_time+job_time
            machine[2][q_index] = release_time #Finish time for this job
            job[3][arrive_index+1] = release_time #Arrival time to next machine

def process_line(job_p,machines,job_set,start):
    """Initialize every job in their machine"""
    #JOB -> (index, [times m],[sequence m],[arrival_times m])
    #MACHINE -> (index, [queue n], [release_times n])
    #start_machines = [[] for i in range(machines[-1][0]+1)]
    sequence = job_p[2]
    sequence = sequence[start:]
    for machine in sequence:
        cautive_insertion(job_p,machines[machine],job_set,machines)

def insertion_machine(job,machine,jobs_set,machine_set):
    """Insert job in machine queue"""
    #JOB -> (index, [times m],[sequence m],[arrival_times m])
    #MACHINE -> (index, [queue n], [release_times n])

    arrival_index = np.where(job[2]==machine[0])[0][0]
    arrival_time = job[3][arrival_index]
    queue = machine[1]


    #Eliminate avery other instance of the job in the queue
    if job[0] in queue:
        machine[1].remove(job[0])

    q_index = 0

    for q_job in queue:
        #find at what time q_job arrived to the machine
        q_job_index = np.where(jobs_set[q_job][2]==machine[0])[0][0]
        q_job_arr = jobs_set[q_job][3][q_job_index]

        if arrival_time > q_job_arr:
            #the job in the queue arrived earlier than us
            q_index += 1

        elif arrival_time == q_job_arr:
            #jobs arrived at the same time
            #Compare times in the machine

            if job[1][arrival_index] >= jobs_set[q_job][1][q_job_index]:
                #it takes more time to process, so it must go second
                q_index += 1
            else:
                #it takes less or equal time in this machine
                break
        else:
            #we found a job
            break
    machine[1].insert(q_index,job[0])
    release_arrival_time(job,machine)
    change_jobs = queue[q_index+1:]
    for af_job in change_jobs:
        arrival_index = np.where(jobs_set[af_job][2]==machine[0])[0][0]
        process_line(jobs_set[af_job],machine_set,jobs_set,arrival_index)

def cautive_insertion(job,machine,jobs_set,machine_set):
    """Insert job in machine queue"""
    #JOB -> (index, [times m],[sequence m],[arrival_times m])
    #MACHINE -> (index, [queue n], [release_times n])

    arrival_index = np.where(job[2]==machine[0])[0][0]
    arrival_time = job[3][arrival_index]
    queue = machine[1]
    copy_release = np.copy(machine[2]) #Copy original list
    #Eliminate avery other instance of the job in the queue
    if job[0] in queue:
        machine[1].remove(job[0])

    q_index = 0

    for q_job in queue:
        #find at what time q_job arrived to the machine
        q_job_index = np.where(jobs_set[q_job][2]==machine[0])[0][0]
        q_job_arr = jobs_set[q_job][3][q_job_index]

        if arrival_time > q_job_arr:
            #the job in the queue arrived earlier than us
            q_index += 1

        elif arrival_time == q_job_arr:
            #jobs arrived at the same time
            #Compare times in the machine

            if job[1][arrival_index] >= jobs_set[q_job][1][q_job_index]:
                #it takes more time to process, so it must go second
                q_index += 1
            else:
                #it takes less or equal time in this machine
                break
        else:
            #we found a job
            break
    machine[1].insert(q_index,job[0])
    release_arrival_time(job,machine)

    #Check if the job entered in a white time space
    #If it did, then it is not necessary to re process the other jobs
    change_jobs = queue[q_index+1:]
    if change_jobs:
        n_arrival_index = np.where(jobs_set[queue[q_index+1]][2]==machine[0])[0][0]
        n_arrival_time = jobs_set[queue[q_index+1]][3][n_arrival_index]
        altered_pipeline = job[3][arrival_index+1]>n_arrival_time
        if altered_pipeline:
            for af_job in change_jobs:
                arrival_index = np.where(jobs_set[af_job][2]==machine[0])[0][0]
                process_line(jobs_set[af_job],machine_set,jobs_set,arrival_index)
        else:
            for i in range(len(change_jobs)):
                machine[2][q_index+1+i]=copy_release[q_index+i]
                