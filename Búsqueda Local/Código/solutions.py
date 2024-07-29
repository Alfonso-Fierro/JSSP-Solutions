"""Tests for algorithms"""

import xlsxwriter
import pandas       as pd
import constructive as cn
import grasp_alpha  as gralph
import grasp_k      as grask
import local_search as ls
archivos = ["Instancias\JSSP1.txt","Instancias\JSSP2.txt",
            "Instancias\JSSP3.txt","Instancias\JSSP4.txt",
            "Instancias\JSSP5.txt","Instancias\JSSP6.txt",
            "Instancias\JSSP7.txt","Instancias\JSSP8.txt",
            "Instancias\JSSP9.txt","Instancias\JSSP10.txt",
            "Instancias\JSSP11.txt","Instancias\JSSP12.txt",
            "Instancias\JSSP13.txt","Instancias\JSSP14.txt",
            "Instancias\JSSP15.txt","Instancias\JSSP16.txt"]

makespan_cons = []

workbook = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_constructive.xlsx')
for archive in archivos:
    worksheet = workbook.add_worksheet(name=archive[11:])
    a = cn.constructivo(archive)
    makespan_cons.append(a[-1][0])
    col = 0
    for row, data in enumerate(a):
        worksheet.write_row(row,col, data)

workbook.close()

makespan_grasp1 = []
workbook2 = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_GRASP1.xlsx')
for archive in archivos:
    worksheet = workbook2.add_worksheet(name=archive[11:])
    a = gralph.grasp(archive,iters=10,alpha=0.7)
    makespan_grasp1.append(a[-1][0])
    col = 0
    for row, data in enumerate(a):
        worksheet.write_row(row,col, data)
workbook2.close()

makespan_grasp2 = []
workbook3 = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_GRASP2.xlsx')
for archive in archivos:
    worksheet = workbook3.add_worksheet(name=archive[11:])
    a = grask.grasp(archive,iters=10,k=5)
    makespan_grasp2.append(a[-1][0])
    col = 0
    for row, data in enumerate(a):
        worksheet.write_row(row,col, data)
workbook3.close()

makespan_fi_bi = []
workbook4 = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_LS1.xlsx')
for archive in archivos:
    worksheet = workbook4.add_worksheet(name=archive[11:])
    a = ls.fi_back_insertion(archive)
    makespan_fi_bi.append(a[-1][0])
    col = 0
    for row, data in enumerate(a):
        worksheet.write_row(row,col, data)
workbook4.close()

makespan_bi_bi = []
workbook5 = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_LS2.xlsx')
for archive in archivos:
    worksheet = workbook5.add_worksheet(name=archive[11:])
    a = ls.bi_back_insertion(archive)
    makespan_bi_bi.append(a[-1][0])
    col = 0
    for row, data in enumerate(a):
        worksheet.write_row(row,col, data)
workbook5.close()

makespan_fi_fi = []
workbook6 = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_LS3.xlsx')
for archive in archivos:
    worksheet = workbook6.add_worksheet(name=archive[11:])
    a = ls.fi_forward_insertion(archive)
    makespan_fi_fi.append(a[-1][0])
    col = 0
    for row, data in enumerate(a):
        worksheet.write_row(row,col, data)
workbook6.close()

makespan_bi_fi = []
workbook7 = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_LS4.xlsx')
for archive in archivos:
    worksheet = workbook7.add_worksheet(name=archive[11:])
    a = ls.bi_forward_insertion(archive)
    makespan_bi_fi.append(a[-1][0])
    col = 0
    for row, data in enumerate(a):
        worksheet.write_row(row,col, data)
workbook7.close()

makespan_fi_int = []
workbook8 = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_LS5.xlsx')
for archive in archivos:
    worksheet = workbook8.add_worksheet(name=archive[11:])
    a = ls.fi_interchange(archive)
    makespan_fi_int.append(a[-1][0])
    col = 0
    for row, data in enumerate(a):
        worksheet.write_row(row,col, data)
workbook8.close()

makespan_bi_int = []
workbook9 = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_LS6.xlsx')
for archive in archivos:
    worksheet = workbook9.add_worksheet(name=archive[11:])
    a = ls.bi_interchange(archive)
    makespan_bi_int.append(a[-1][0])
    col = 0
    for row, data in enumerate(a):
        worksheet.write_row(row,col, data)
workbook9.close()

rows = archivos =  ["JSSP1.txt","JSSP2.txt",
                    "JSSP3.txt","JSSP4.txt",
                    "JSSP5.txt","JSSP6.txt",
                    "JSSP7.txt","JSSP8.txt",
                    "JSSP9.txt","JSSP10.txt",
                    "JSSP11.txt","JSSP12.txt",
                    "JSSP13.txt","JSSP14.txt",
                    "JSSP15.txt","JSSP16.txt"]

cols = ["Constructivo","GRASP1","GRASP2",
        "LS1","LS2","LS3","LS4","LS5","LS6"]

data_matrix = [makespan_cons,makespan_grasp1,makespan_grasp2,
               makespan_fi_bi,makespan_bi_bi,makespan_fi_fi,
               makespan_bi_fi,makespan_fi_int,makespan_bi_int]

frame = pd.DataFrame(data_matrix,index=cols,columns=rows)
frame = frame.T
frame.to_excel("makespan.xlsx")
