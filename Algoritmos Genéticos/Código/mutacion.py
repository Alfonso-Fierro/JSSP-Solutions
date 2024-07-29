import random
import constructivo
import copy
import numpy as np
random.seed(21)
def mutacion(num_maquinas, num_trabajos, programa, grupos):
    c_programa = copy.deepcopy(programa)
    makespan_ini = constructivo.makespan(num_maquinas, num_trabajos, programa, grupos)
    indice_mutado = np.random.choice(len(programa))
    cromosoma_mutado = busqueda_local(num_maquinas, num_trabajos, c_programa, grupos, indice_mutado, makespan_ini)
    return cromosoma_mutado

def busqueda_local(num_maquinas, num_trabajos, programa, grupos, indice_mutado, makespan):
    c_programa = copy.deepcopy(programa)
    vecindario = intercambio(c_programa, indice_mutado)
    for prog in vecindario:
        nuevo_makespan = constructivo.makespan(num_maquinas, num_trabajos, prog, grupos)
        if nuevo_makespan <= makespan:
            c_programa = copy.deepcopy(prog)
            makespan = nuevo_makespan
            # Puedes agregar aquí una lógica para salir temprano si se cumple cierta condición
    return c_programa

def intercambio(programa, indice_mutado):
    """Swap elements in neighborhood"""
    cambios = []
    c_programa = copy.deepcopy(programa)
    
    if indice_mutado < 0 or indice_mutado >= len(c_programa)-1:
        # Manejar el caso en que el índice_mutado está fuera de rango
        return cambios

    actividad = c_programa.pop(indice_mutado)
    trabajo = actividad[0]
    indice = indice_mutado
    actividad_m = copy.deepcopy(c_programa[indice][0])
    while actividad_m != trabajo and indice < len(c_programa)-1:
        c_programa.insert(indice, actividad)
        indice += 1
        actividad_m = copy.deepcopy(c_programa[indice][0])
        cambios.append(copy.deepcopy(c_programa))
        c_programa.remove(actividad)
    return cambios
