import numpy as np
import copy

def verificar_actividades(num_trabajos,num_maquinas, secuencias,tiempos):
    actividades = []
    for t in range(num_trabajos):
        for m in range(num_maquinas):
            trabajo     = t
            maquina     = secuencias[t,m]
            tiempo      = tiempos[t,m]
            actividad   = [trabajo,maquina,tiempo]
            actividades.append(actividad)
    return actividades

def matriz_precedencias(grupos):
    #Crear una matriz para cada grupo:
    grupo = grupos[0]
    precedencia_trabajo = np.zeros([len(grupo),len(grupo)], dtype= int)
    for i,activity1 in enumerate(precedencia_trabajo):
        for j, activity2 in enumerate(precedencia_trabajo): 
            if i < j :
                precedencia_trabajo[i,j]=1
    return precedencia_trabajo

def verificar_presedencia(actividades,grupos):
    actividades_c   = copy.deepcopy(actividades)
    orden           = True
    act_evaluada    = actividades_c[-1]
    grupo_evaluado  = act_evaluada[0]
    grupo           = grupos[grupo_evaluado]
    etapa_evaluada  = grupo.index(act_evaluada)
    if etapa_evaluada > 0:
        #La etapa anterior debe ser la más cercana    
        cola = list(reversed(actividades))
        for act_comparada in cola[1:]:
            grupo_comparado = act_comparada[0]
            if grupo_comparado != grupo_evaluado:
                continue
            else:
                etapa_comparada = grupo.index(act_comparada)
                orden           = etapa_evaluada-etapa_comparada == 1
                return orden
    else:
        return orden
