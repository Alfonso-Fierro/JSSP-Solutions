"""Lectura de datos"""

import numpy as np

def leer_txt(txt_file_name):
    """Function to iterate over txt and return parameters for the problem"""
    #txt_file_name.
    matriz = []
    with open(txt_file_name,'r',encoding="utf-8") as archivo:
        for linea in archivo:
            elementos = linea.split()
            fila = [int(elemento) for elemento in elementos]
            # Agrega la fila a la matrix
            matriz.append(fila)
    num_trabajos            = matriz[0][0]
    num_maqus        = matriz[0][1]
    corrector_indc = np.ones(num_maqus)
    tiempos   = np.array(matriz[1:num_trabajos+1])
    secuencias = np.array(matriz[num_trabajos+1:]-corrector_indc).astype(int)
    archivo.close()
    return num_trabajos, num_maqus, tiempos, secuencias