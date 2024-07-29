"""Script to test functions"""

from frankenstein import frankenstein
import reader
import selection
import local_search
import VND
import verification
import grasp_k_selection
input_matrix = reader.read_txt(r"instancias\JSSP1.txt")

num_machines = input_matrix[1]
num_jobs     = input_matrix[0]
processes = reader.process_char(input_matrix)
activities = reader.activities_char(input_matrix)
precendence = verification.precedence_matrix(activities)

jobs = reader.jobs_char(input_matrix)
machines = reader.machines_char(input_matrix)
jobs[0]
ranks = selection.rank_job_machines(jobs,machines)
order = selection.insertion_order(ranks)
init_sols = []
for i in range(4):
    init_sols.append(grasp_k_selection.restricted_list(jobs,order))
acts_order = selection.activities_order(order,jobs,activities,num_machines)
priority_act = selection.priority_search(jobs,activities)

# c2 = local_search.local_search_1(acts_order,input_matrix,activities,2)
# # print(c2)
# sol = VND.VND(acts_order,input_matrix,activities,300)
sol2 = frankenstein("instancias\debug.txt",2,100,100,40)