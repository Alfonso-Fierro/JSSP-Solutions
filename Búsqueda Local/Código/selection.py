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
    unit = len(ranked)
    while ranked[-1]:
        for i in range(unit):
            if ranked[i]:
                indxs.append(ranked[i][0])
                ranked[i]=ranked[i][1:]
    return indxs

def activities_order(indxs, jobs, activities, num_machines):
    "job, seq in 0"
    pairs = []
    for i in range(num_machines):
        for job in indxs:
            pairs.append([job,jobs[job][2][i]])
    acts = []
    for pair in pairs:
        acts.append(activities.index(pair))
    return acts

def interchange(order, activities, activity):
    """Swap elements in neighborhood"""
    #All activities are bounded, they cannot be performed
    #after of before their immediate follower
    flips = []
    cpy_activities = order.copy()
    activity_index = order.index(activity)
    tail           = cpy_activities[:activity_index]
    head           = cpy_activities[activity_index+1:]
    #First interchange backwards
    act = activities[activity]
    for swapped in reversed(tail):
        swap = activities[swapped]
        if swap[0] != act[0]:
            swap_index = order.index(swapped)
            flips.append(swap_positions(cpy_activities,swap_index,activity_index))
        else:
            break
    for swapped in head:
        swap = activities[swapped]
        if swap[0] != act[0]:
            swap_index = order.index(swapped)
            flips.append(swap_positions(cpy_activities,swap_index,activity_index))
        else:
            break
    return flips

def swap_positions(lista, pos1, pos2):
    "Swap two elements"
    displaced = lista.copy()
    displaced[pos1], displaced[pos2] = displaced[pos2], displaced[pos1]
    return displaced

def displace_positions(lista, pos1, element):
    "Permutations"
    displaced = lista.copy()
    displaced.remove(element)
    displaced.insert(pos1,element)
    return displaced

def back_insertion(order, activities, activity):
    """Insert in elements back"""
    #All activities are bounded, they cannot be performed
    #after of before their immediate follower
    flips = []
    cpy_activities = order.copy()
    activity_index = order.index(activity)
    tail           = cpy_activities[:activity_index]
    #First interchange backwards
    act = activities[activity]
    for disp in reversed(tail):
        displaced = activities[disp]
        if displaced[0] != act[0]:
            displace_index = order.index(disp)
            flips.append(displace_positions(cpy_activities,displace_index,activity))
        else:
            break
    return flips


def frwrd_insertion(order, activities, activity,):
    """Insert in elements frwrd"""
    #All activities are bounded, they cannot be performed
    #after of before their immediate follower
    flips = []
    cpy_activities = order.copy()
    activity_index = order.index(activity)
    head           = cpy_activities[activity_index+1:]
    #First interchange backwards
    act = activities[activity]
    for disp in head:
        displaced = activities[disp]
        if displaced[0] != act[0]:
            displace_index = order.index(disp)
            flips.append(displace_positions(cpy_activities,displace_index,activity))
        else:
            break
    return flips
