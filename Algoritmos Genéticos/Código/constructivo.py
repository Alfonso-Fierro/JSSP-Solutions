import ocupacion
import numpy as np
def constructivo(num_maquinas, num_trabajos, programa, grupos):
    llegadas, salidas, espacios = ocupacion.ocupacion(num_maquinas, num_trabajos,
                                                      programa, grupos)
    makespan = np.max(salidas)
    for i in range(len(espacios)):
        for j in range(len(espacios[1])):
            espacios[i][j]+=1
    espacios.append([makespan,0])
    return espacios

def makespan(num_maquinas, num_trabajos, programa, grupos):
    llegadas, salidas, espacios = ocupacion.ocupacion(num_maquinas, num_trabajos,
                                                      programa, grupos)
    makespan = np.max(salidas)
    return makespan
