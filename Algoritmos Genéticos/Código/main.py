import numpy as np
import xlsxwriter
import algoritmo_genetico
import lector
import grupos
import poblacion
import constructivo
ARCHIVOS = ["Instancias\JSSP1.txt","Instancias\JSSP2.txt",
            "Instancias\JSSP3.txt","Instancias\JSSP4.txt",
            "Instancias\JSSP5.txt","Instancias\JSSP6.txt",
            "Instancias\JSSP7.txt","Instancias\JSSP8.txt",
            "Instancias\JSSP9.txt","Instancias\JSSP10.txt",
            "Instancias\JSSP11.txt","Instancias\JSSP12.txt",
            "Instancias\JSSP13.txt","Instancias\JSSP14.txt",
            "Instancias\JSSP15.txt","Instancias\JSSP16.txt"]

libro = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_genetico.xlsx')
for archivo in ARCHIVOS:
    hoja = libro.add_worksheet(name=archivo[11:])
    num_trabajos,num_maquinas,tiempos,secuencias = lector.leer_txt(archivo)
    grupo       = grupos.agrupamiento(num_trabajos,num_maquinas,secuencias,tiempos)
    solucion = algoritmo_genetico.algoritmo_genetico(archivo,10,10,0.5,0.05)
    sol   = constructivo.constructivo(num_maquinas,num_trabajos,solucion,grupo)
    col = 0
    for row, data in enumerate(sol):
        hoja.write_row(row,col, data)
libro.close()

# libro = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_genetico_p5.xlsx')
# for archivo in ARCHIVOS:
#     hoja = libro.add_worksheet(name=archivo[11:])
#     num_trabajos,num_maquinas,tiempos,secuencias = lector.leer_txt(archivo)
#     grupo       = grupos.agrupamiento(num_trabajos,num_maquinas,secuencias,tiempos)
#     actividades = poblacion.orden_actividades(grupo)
#     solucion = algoritmo_genetico.algoritmo_genetico(archivo,5,10,0.5,0.05)
#     sol   = constructivo.constructivo(num_maquinas,num_trabajos,solucion,grupo)
#     col = 0
#     for row, data in enumerate(sol):
#         hoja.write_row(row,col, data)
# libro.close()

# libro = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_genetico_p15.xlsx')
# for archivo in ARCHIVOS:
#     hoja = libro.add_worksheet(name=archivo[11:])
#     num_trabajos,num_maquinas,tiempos,secuencias = lector.leer_txt(archivo)
#     grupo       = grupos.agrupamiento(num_trabajos,num_maquinas,secuencias,tiempos)
#     actividades = poblacion.orden_actividades(grupo)
#     solucion = algoritmo_genetico.algoritmo_genetico(archivo,15,10,0.5,0.05)
#     sol   = constructivo.constructivo(num_maquinas,num_trabajos,solucion,grupo)
#     col = 0
#     for row, data in enumerate(sol):
#         hoja.write_row(row,col, data)
# libro.close()

# libro = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_genetico_g5.xlsx')
# for archivo in ARCHIVOS:
#     hoja = libro.add_worksheet(name=archivo[11:])
#     num_trabajos,num_maquinas,tiempos,secuencias = lector.leer_txt(archivo)
#     grupo       = grupos.agrupamiento(num_trabajos,num_maquinas,secuencias,tiempos)
#     actividades = poblacion.orden_actividades(grupo)
#     solucion = algoritmo_genetico.algoritmo_genetico(archivo,10,5,0.5,0.05)
#     sol   = constructivo.constructivo(num_maquinas,num_trabajos,solucion,grupo)
#     col = 0
#     for row, data in enumerate(sol):
#         hoja.write_row(row,col, data)
# libro.close()

# libro = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_genetico_g15.xlsx')
# for archivo in ARCHIVOS:
#     hoja = libro.add_worksheet(name=archivo[11:])
#     num_trabajos,num_maquinas,tiempos,secuencias = lector.leer_txt(archivo)
#     grupo       = grupos.agrupamiento(num_trabajos,num_maquinas,secuencias,tiempos)
#     actividades = poblacion.orden_actividades(grupo)
#     solucion = algoritmo_genetico.algoritmo_genetico(archivo,10,15,0.5,0.05)
#     sol   = constructivo.constructivo(num_maquinas,num_trabajos,solucion,grupo)
#     col = 0
#     for row, data in enumerate(sol):
#         hoja.write_row(row,col, data)
# libro.close()

# libro = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_genetico_d03.xlsx')
# for archivo in ARCHIVOS:
#     hoja = libro.add_worksheet(name=archivo[11:])
#     num_trabajos,num_maquinas,tiempos,secuencias = lector.leer_txt(archivo)
#     grupo       = grupos.agrupamiento(num_trabajos,num_maquinas,secuencias,tiempos)
#     actividades = poblacion.orden_actividades(grupo)
#     solucion = algoritmo_genetico.algoritmo_genetico(archivo,10,10,0.3,0.05)
#     sol   = constructivo.constructivo(num_maquinas,num_trabajos,solucion,grupo)
#     col = 0
#     for row, data in enumerate(sol):
#         hoja.write_row(row,col, data)
# libro.close()

# libro = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_genetico_d07.xlsx')
# for archivo in ARCHIVOS:
#     hoja = libro.add_worksheet(name=archivo[11:])
#     num_trabajos,num_maquinas,tiempos,secuencias = lector.leer_txt(archivo)
#     grupo       = grupos.agrupamiento(num_trabajos,num_maquinas,secuencias,tiempos)
#     actividades = poblacion.orden_actividades(grupo)
#     solucion = algoritmo_genetico.algoritmo_genetico(archivo,10,10,0.7,0.05)
#     sol   = constructivo.constructivo(num_maquinas,num_trabajos,solucion,grupo)
#     col = 0
#     for row, data in enumerate(sol):
#         hoja.write_row(row,col, data)
# libro.close()

# libro = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_genetico_m01.xlsx')
# for archivo in ARCHIVOS:
#     hoja = libro.add_worksheet(name=archivo[11:])
#     num_trabajos,num_maquinas,tiempos,secuencias = lector.leer_txt(archivo)
#     grupo       = grupos.agrupamiento(num_trabajos,num_maquinas,secuencias,tiempos)
#     actividades = poblacion.orden_actividades(grupo)
#     solucion = algoritmo_genetico.algoritmo_genetico(archivo,10,10,0.5,0.1)
#     sol   = constructivo.constructivo(num_maquinas,num_trabajos,solucion,grupo)
#     col = 0
#     for row, data in enumerate(sol):
#         hoja.write_row(row,col, data)
# libro.close()

# libro = xlsxwriter.Workbook('JSSP_Alfonso_Fierro_genetico_m015.xlsx')
# for archivo in ARCHIVOS:
#     hoja = libro.add_worksheet(name=archivo[11:])
#     num_trabajos,num_maquinas,tiempos,secuencias = lector.leer_txt(archivo)
#     grupo       = grupos.agrupamiento(num_trabajos,num_maquinas,secuencias,tiempos)
#     actividades = poblacion.orden_actividades(grupo)
#     solucion = algoritmo_genetico.algoritmo_genetico(archivo,10,10,0.5,0.15)
#     sol   = constructivo.constructivo(num_maquinas,num_trabajos,solucion,grupo)
#     col = 0
#     for row, data in enumerate(sol):
#         hoja.write_row(row,col, data)
# libro.close()