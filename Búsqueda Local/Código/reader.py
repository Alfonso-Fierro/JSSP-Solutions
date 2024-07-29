"""Lectura de datos"""

import numpy as np


def read_txt(txt_file_name):
    """Function to iterate over txt and return parameters for the problem"""
    #txt_file_name.
    matriz = []
    with open(txt_file_name,'r',encoding="utf-8") as archive:
        for linea in archive:
            elementos = linea.split()
            fila = [int(elemento) for elemento in elementos]
            # Agrega la fila a la matriz
            matriz.append(fila)
    jobs        = matriz[0][0]
    machines    = matriz[0][1]
    index_cor   = np.ones(machines)
    times   = np.array(matriz[1:jobs+1])
    sequences = np.array(matriz[jobs+1:]-index_cor).astype(int)
    archive.close()
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

def process_char(input_matrix):
    """Create processes list"""
    # a process is a tuple (machine,time)
    # Process_char is a triplet (job, process)
    processes = []
    i = 0
    num_jobs = input_matrix[0]
    while i < num_jobs:
        jobs = input_matrix[2]
        for index1, job in enumerate(jobs):
            char=[index1]
            for index2, time in enumerate(job):
                machine_time = (input_matrix[3][index1][index2],time)
                char.append(machine_time)
            processes.append(char)
        i += 1
    return processes

def activities_char(input_matix):
    """return list of activities in order"""
    activities = []
    sequences = input_matix[3]
    for index, proc in enumerate(sequences):
        for element in proc:
            activities.append([index,element])
    return activities

def precedence_matrix(activities):
    "Create matrix to validate insertion"
    precedence = np.zeros([len(activities),len(activities)], dtype= int)
    for i,activity1 in enumerate(activities):
        for j, activity2 in enumerate(activities):
            if activity1[0]==activity2[0]:  #We compare the same job
                if i < j :
                    precedence[i,j]=1
    return precedence
