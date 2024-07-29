import numpy as np
import random
import copy
import verificaciones
def cruce(programa_1, programa_2, dominancia,grupo):
    c_prog1 = copy.deepcopy(programa_1)
    c_prog2 = copy.deepcopy(programa_2)
    numero_alelos = len(programa_1)
    cromosoma_cruzado = []
    while len(cromosoma_cruzado) < numero_alelos:
        suerte = random.random()
        alel_dominante = []
        if suerte < dominancia:
            alel_dominante = c_prog1[0]
        else:
            alel_dominante = c_prog2[0]
        cromosoma_cruzado.append(alel_dominante)
        c_prog1.remove(alel_dominante)
        c_prog2.remove(alel_dominante)

    if verificaciones.verificar_presedencia(cromosoma_cruzado,grupo):
        return cromosoma_cruzado
    
def cruce_poblacional(poblacion, dominancia, grupo):
    c_poblacion     = copy.deepcopy(poblacion)
    indices_disp    = list(range(len(poblacion)))
    indices_parejas = np.random.choice(indices_disp,
                                       size=[len(poblacion),2],
                                       replace=True)
    for pareja in indices_parejas:
        cromosoma_1 = poblacion[pareja[0]]
        cromosoma_2 = poblacion[pareja[1]]
        hijo        = cruce(cromosoma_1,cromosoma_2,dominancia,grupo)
        c_poblacion.append(hijo)
    return c_poblacion
