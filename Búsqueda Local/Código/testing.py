#Lectura de datos
import numpy as np

def read_txt(txt_file_name):
    """Function to iterate over txt and return parameters for the problem"""
    #txt_file_name.
    matriz = []
    with open(txt_file_name,'r') as input:
        for linea in input:
            elementos = linea.split()   
            fila = [int(elemento) for elemento in elementos]          
            # Agrega la fila a la matriz
            matriz.append(fila)
    jobs        = matriz[0][0]
    machines    = matriz[0][1]
    index_cor   = np.ones(machines)
    times   = np.array(matriz[1:jobs+1])
    sequences = np.array(matriz[jobs+1:]-index_cor).astype(int)
    input.close()
    return [jobs, machines, times, sequences]

def jobs_char(input_matrix):

    """Create 4plet (job, sequence, work_times, arrival_time)"""

    jobs = [[]]

    i = 0

    while i < input_matrix[0]:

        jobs[i].append(i)

        jobs[i].append(input_matrix[2][i])

        jobs[i].append(input_matrix[3][i])

        jobs[i].append(np.zeros(input_matrix[1]+1).astype(int))

        if i < input_matrix[0]-1:

            jobs.append([])

        i += 1

    return jobs


def machines_char(input_matrix):

    """#Create 4plet (machine, job_queue, release_time)"""

    #time work, is a list and must begin with 0

    #time_work is supposed to compute the time of end for every job

    machines = [[]]

    i = 0

    while i < input_matrix[1]:

        machines[i].append(i)

        machines[i].append([])#queue of works

        machines[i].append(np.zeros(input_matrix[0]).astype(int))#time_work

        if i < input_matrix[1]-1:

            machines.append([])

        i += 1
    return machines

def first_queue(jobs,num_m,num_j):
    """Find which machine has the most jobs starting in it"""
    #(job, [times], [sequence])
    # job 0->n-1
    # [sequence]$[times] -> 1->m
    machines = np.zeros(num_m)
    i=0 #machine ID
    while i < num_m:
        count = 0
        j = 0
        while j < num_j:
            if jobs[j][2][0] == i:
                count += 1
            j += 1
        machines[i]=count
        i+=1
    ovrwlmd = np.where(machines==max(machines))[0] #where returns a tuple
    return ovrwlmd

def queue_of_jobs(jobs, ovrwlmd):
    priority = [[]] #List of jobs that start with the most occupied machines
    #first most occupied machine
    ov_machine = 0
    while ov_machine < len(ovrwlmd):
        job = 0
        while job < len(jobs):
            if jobs[job][2][0] == ovrwlmd[ov_machine]:
                priority[ov_machine].append(job)
            job += 1
        ov_machine += 1
        if ov_machine < len(ovrwlmd)-1:
            priority.append([])
    return priority

def release_arrival_time2(job,machine):
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
        job[3][q_index+1] = release_time
    else:
        previous_release_time = machine[2][q_index-1]
        if max(arrival_time,previous_release_time)==arrival_time:
            release_time = arrival_time+job_time
            machine[2][q_index] = release_time
            job[3][q_index+1] = release_time
        else:
            release_time = previous_release_time+job_time
            machine[2][q_index] = release_time #Finish time for this job
            job[3][arrive_index+1] = release_time #Arrival time to next machine
    return job, machine

def insertion_machine(job,machine,job_set):
    """Carries the first machine a job enters"""
    #We only control order job_set enter the system.
    #JOB -> (index, [times],[sequence],[arrival_times])
    #MACHINE -> (index, [queue], [release_times])
    queue = machine[1] #job_set are named with their indices
    position = 0
    arrival_index = np.where(job[2]==machine[0])[0][0]
    arrival_time = job[3][arrival_index]
    for element in queue:  #job_set are named with their indices
        sqnc_indx = np.where(job_set[element][2]==machine[0])[0][0] #index search
        element_time = job_set[element][3][sqnc_indx] #time of arriving machine
        if arrival_time > element_time:
            position += 1
        else:
            break
    machine[1][position]=job[0]
    #Luego hay que recalcular todos los otros trabajos
    return machine

def insertion_machine2(job,machine,jobs_set):
    """Insert job in queue"""
    #JOB -> (index, [times m],[sequence m],[arrival_times m])
    #MACHINE -> (index, [queue n], [release_times n])
    arrival_index = np.where(job[2]==machine[0])[0][0]
    arrival_time = job[3][arrival_index]
    queue = machine[1]
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
            if job[1][arrival_index] > jobs_set[q_job][1][q_job_index]:
                #it takes more time to process, so it must go second
                q_index += 1
            else:
                #it takes less or equal time in this machine
                break
        else:
            #we found a job
            break       
    machine[1].insert(q_index,job[0])
    return machine


instance1 = read_txt('JSSP1.txt')

jobs = jobs_char(instance1)

num_j= instance1[0]

num_m= instance1[1]

machines = machines_char(instance1)

fila = first_queue(jobs, num_m,num_j)

#priority_jobs = queue_of_jobs(jobs,queue)

instance0 = read_txt('JSSP0.txt')

jobs0 = jobs_char(instance0)

num_j0= instance0[0]

num_m0= instance0[1]

machines0 = machines_char(instance0)

job0 = jobs0[0]
job1 = jobs0[1]
job2 = jobs0[2]

machine0 = machines0[job0[2][0]]
machine1 = machines0[job1[2][0]]

insertion_machine2(job0,machine0,jobs0)
insertion_machine2(job2,machine0,jobs0)

release_arrival_time2(job2,machine0)
release_arrival_time2(job0,machine0)

insertion_machine2(job1,machine1,jobs0)
release_arrival_time2(job1,machine1)
insertion_machine2(job0,machine1,jobs0)
insertion_machine2(job2,machine1,jobs0)
release_arrival_time2(job2,machine1)
release_arrival_time2(job0,machine1)