"""Tests for algorithms"""

import xlsxwriter
import reader
import selection
import pandas       as pd
import VND          as vnd
archivos = ["Instancias\JSSP1.txt","Instancias\JSSP2.txt",
            "Instancias\JSSP3.txt","Instancias\JSSP4.txt",
            "Instancias\JSSP5.txt","Instancias\JSSP6.txt",
            "Instancias\JSSP7.txt","Instancias\JSSP8.txt",
            "Instancias\JSSP9.txt","Instancias\JSSP10.txt",
            "Instancias\JSSP11.txt","Instancias\JSSP12.txt",
            "Instancias\JSSP13.txt","Instancias\JSSP14.txt",
            "Instancias\JSSP15.txt","Instancias\JSSP16.txt"]

time_limt = [2,2,2,2,75,75,75,75,75,75,150,150,300,300,1800,1800]
makespan_VND = []

workbook = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_VND.xlsx')
i=0
for archive in archivos:
    print(i)
    worksheet = workbook.add_worksheet(name=archive[11:])
    input_matrix = reader.read_txt(archive)
    num_machines = input_matrix[1]
    num_jobs     = input_matrix[0]
    activities = reader.activities_char(input_matrix)
    jobs = reader.jobs_char(input_matrix)
    machines = reader.machines_char(input_matrix)
    ranks = selection.rank_job_machines(jobs,machines)
    order = selection.insertion_order(ranks)
    acts_order = selection.activities_order(order,jobs,activities,num_machines)
    a = vnd.VND(acts_order,input_matrix,activities,time_limt[i])
    makespan_VND.append(a[-1][0])
    col = 0
    for row, data in enumerate(a):
        worksheet.write_row(row,col, data)
    i += 1
workbook.close()

cols = ["VND"]

rows =  ["JSSP1.txt","JSSP2.txt",
        "JSSP3.txt","JSSP4.txt",
        "JSSP5.txt","JSSP6.txt",
        "JSSP7.txt","JSSP8.txt",
        "JSSP9.txt","JSSP10.txt",
        "JSSP11.txt","JSSP12.txt",
        "JSSP13.txt","JSSP14.txt",
        "JSSP15.txt","JSSP16.txt"]

data_matrix = [makespan_VND]

frame = pd.DataFrame(data_matrix,index=cols,columns=rows)
frame = frame.T
frame.to_excel("makespanVND.xlsx")