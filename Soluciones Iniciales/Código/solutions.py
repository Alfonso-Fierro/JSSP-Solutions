"""Tests for algorithms"""

import xlsxwriter
import constructive as cn
import grasp_alpha  as gralph
import grasp_k      as grask

archivos = ["Instancias\JSSP1.txt","Instancias\JSSP2.txt",
            "Instancias\JSSP3.txt","Instancias\JSSP4.txt",
            "Instancias\JSSP5.txt","Instancias\JSSP6.txt",
            "Instancias\JSSP7.txt","Instancias\JSSP8.txt",
            "Instancias\JSSP9.txt","Instancias\JSSP10.txt",
            "Instancias\JSSP11.txt","Instancias\JSSP12.txt",
            "Instancias\JSSP13.txt","Instancias\JSSP14.txt",
            "Instancias\JSSP15.txt","Instancias\JSSP16.txt"]

workbook = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_constructivo.xlsx')
for archive in archivos:
    worksheet = workbook.add_worksheet()
    a = cn.constructivo(archive)
    col = 0
    for row, data in enumerate(a):
        worksheet.write_row(row,col, data)

workbook.close()

# workbook2 = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_GRASP1.xlsx')
# for archive in archivos:
#     worksheet = workbook2.add_worksheet()
#     a = gralph.grasp(archive,iters=100,alpha=0.7)
#     col = 0
#     for row, data in enumerate(a):
#         worksheet.write_row(row,col, data)
# workbook2.close()

# workbook3 = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_GRASP2.xlsx')
# for archive in archivos:
#     worksheet = workbook3.add_worksheet()
#     a = grask.grasp(archive,iters=100,k=5)
#     col = 0
#     for row, data in enumerate(a):
#         worksheet.write_row(row,col, data)
# workbook3.close()
