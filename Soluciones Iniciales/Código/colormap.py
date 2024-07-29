import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample DataFrame
data = {
    'Job': ['Job1', 'Job2', 'Job3', 'Job4'],
    'Machine': ['M1', 'M2', 'M1', 'M3'],
    'Time_of_Start': [0, 2, 4, 6],
    'Time_of_Completion': [3, 5, 7, 9]
}

df = pd.DataFrame(data)

# Create a list of unique jobs
unique_jobs = df['Job'].unique()

# Create a colormap with a fixed number of colors
num_colors = len(unique_jobs)
colors = plt.cm.rainbow(np.linspace(0, 1, num_colors))

# Create a dictionary to map each job to its assigned color
job_colors = {job: color for job, color in zip(unique_jobs, colors)}

# Sort DataFrame by start time
df = df.sort_values(by='Time_of_Start')

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 5))

# Plot Gantt chart
for i, row in df.iterrows():
    job_color = job_colors[row['Job']]
    ax.barh(row['Machine'], width=row['Time_of_Completion'] - row['Time_of_Start'],
            left=row['Time_of_Start'], color=job_color, label=row['Job'])

# Set labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Machine')
ax.set_title('Gantt Chart')
ax.invert_yaxis()  # Invert the y-axis to have Machine 1 at the top

# Add a legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

plt.show()