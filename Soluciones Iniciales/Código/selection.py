"""Select job to use in the solution"""

def rank_job_machines(jobs,machines):
    """order machines by occupacy, order jobs by total time"""
    #Return machines sorted by how many jobs they can process
    #(job, [times], [sequence])
    # job 0->n-1
    # [sequence]$[times] -> 1->m
    candidates=[]
    for machine in machines:
        counter = 0
        job_ids = []
        for j in jobs:
            job = []
            if j[2][0]==machine[0]:
                counter+=1
                job.append(j[0])#append id
                job.append(sum(j[1])) #append time of processing
                job_ids.append(job)
        if counter != 0:
            job_ids.sort(key = lambda x: x[1])
            jobi = [j[0] for j in job_ids]
            pair = [machine[0],counter,jobi]
            candidates.append(pair)
    candidates.sort(key = lambda x: x[1],reverse=False)
    # [machine_indx, #jobs, [[job_indx, ttl_time]]]
    # [machine [jobs]]
    #candidates  = [i[:1]+i[2:] for i in candidates]
    candidates  = ([i[2:][0] for i in candidates])
    return candidates

def insertion_order(ranked):
    """return list of indices with jobs to process"""
    indxs = [] #Order of jobs to enter in the machines
    u = len(ranked)
    while ranked[-1]:
        for i in range(u):
            if ranked[i]:
                indxs.append(ranked[i][0])
                ranked[i]=ranked[i][1:]
    return indxs
