"""Script to test functions"""

import reader
import selection
import local_search

input_matrix = reader.read_txt(r"instancias\debug.txt")

num_machines = input_matrix[1]
num_jobs     = input_matrix[0]
processes = reader.process_char(input_matrix)
activities = reader.activities_char(input_matrix)
precendence = reader.precedence_matrix(activities)

jobs = reader.jobs_char(input_matrix)
machines = reader.machines_char(input_matrix)

ranks = selection.rank_job_machines(jobs,machines)
order = selection.insertion_order(ranks)
acts_order = selection.activities_order(order,jobs,activities,num_machines)
neighbours = selection.back_insertion(acts_order,activities,2)


#print(acts_order)
#print(machines[0])


c1 = local_search.constructivo(r"instancias\debug.txt")
print(c1)
# c2 = local_search.bi_back_insertion(r"instancias\JSSP1.txt")
# c3 = local_search.fi_forward_insertion(r"instancias\JSSP1.txt")
# c4 = local_search.bi_forward_insertion(r"instancias\JSSP1.txt")
# c5 = local_search.fi_interchange(r"instancias\JSSP1.txt")
# c6 = local_search.bi_interchange(r"instancias\JSSP1.txt")
