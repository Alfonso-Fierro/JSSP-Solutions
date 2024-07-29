import numpy as np

def agrupamiento(num_trabajos,num_maquinas, secuencias,tiempos):
    actividades = []
    for t in range(num_trabajos):
        grupo = []
        for m in range(num_maquinas):
            trabajo     = t
            maquina     = secuencias[t,m]
            tiempo      = tiempos[t,m]
            actividad   = [trabajo,maquina,tiempo]
            grupo.append(actividad)
        actividades.append(grupo)
    return actividades
