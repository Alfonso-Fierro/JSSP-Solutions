"""Code to verify implementation"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def intervals(jobs, num_j, num_m):
    """Obtain the propper work intervals in machines"""
    # JOB MACHINE START FINISH
    # JOB -> (index, [times m],[sequence m],[arrival_times m])
    matrix = np.zeros([num_j * num_m, 4], dtype=int)
    for i in range(num_j):
        for j in range(num_m):
            matrix[i * num_m + j, 0] = i + 1
            matrix[i * num_m + j, 1] = jobs[i][2][j] + 1
            matrix[i * num_m + j, 2] = jobs[i][3][j + 1] - jobs[i][1][j]
            matrix[i * num_m + j, 3] = jobs[i][3][j + 1]
    data_frame = pd.DataFrame(
        matrix, columns=["Job", "Machine", "Time_of_Start", "Time_of_Completion"]
    )
    data_frame = data_frame.sort_values(by="Time_of_Start")
    return data_frame

def schedule_visual(data_frame, num_m):
    """Returns grantt chart to viualize solution"""
    # Create a figure and axis
    # Create a list of unique jobs
    unique_jobs = data_frame["Job"].unique()

    # Create a colormap with a fixed number of colors
    num_colors = len(unique_jobs)
    colors = plt.cm.Set3(np.linspace(0, 1, num_colors))

    # Create a dictionary to map each job to its assigned color
    job_colors = {job: color for job, color in zip(unique_jobs, colors)}
    fig, axis = plt.subplots(figsize=(10, 5))
    # Create a legend dictionary to store unique job labels
    legend_dict = {}

    # Plot Gantt chart
    for i, row in data_frame.iterrows():
        job_color = job_colors[row["Job"]]
        if row["Job"] not in legend_dict:
            legend_dict[row["Job"]] = axis.barh(
            row["Machine"],
            width=row["Time_of_Completion"] - row["Time_of_Start"],
            left=row["Time_of_Start"],
            color=job_color,
            label=row["Job"],
            )
        else:
            axis.barh(
            row["Machine"],
            width=row["Time_of_Completion"] - row["Time_of_Start"],
            left=row["Time_of_Start"],
            color=job_color,
            )

    # Set labels and title
    axis.set_xlabel("Time")
    axis.set_ylabel("Machine")
    axis.set_title("Schedule")

    axis.set_yticks(range(1, num_m + 1))
    max_completion_time = data_frame["Time_of_Completion"].max()
    axis.set_xticks(range(max_completion_time + 1))

    # Create a legend with unique job labels
    handles = [legend_dict[job][0] for job in unique_jobs]
    axis.legend(handles, unique_jobs, loc="upper right",title = "Jobs")
    plt.show()

def work_matrix(machines, exec_time):
    """Return matrix with the work process as a dataframe"""
    matrix = []
    work_time = 0
    for m in enumerate(machines):
        matrix.append(np.array(machines[m[0]][1])+np.ones(len(machines[m[0]][1]),dtype=int))
        work_time = max(work_time , machines[m[0]][2][-1])
    matrix.append([work_time,exec_time])
    return matrix
