import numpy as np
import copy

def orden_actividades(grupos):
    actividades =[]
    #grupos[i]    = actividades del trabajo i
    #grupos[i][j] = actividad j del trabajo i
    grupos_c = copy.deepcopy(grupos)
    piscina = []
    for grupo in grupos_c:
        act = grupo.pop(0)
        piscina.append(act)
    while piscina:
        indice       = np.random.choice(len(piscina))  
        act_escogida = piscina.pop(indice)
        grupo        = act_escogida[0]
        if grupos_c[grupo]:
            act_siguiente = grupos_c[grupo].pop(0)
            piscina.append(act_siguiente)
        actividades.append(act_escogida)
    return actividades

def generar_poblacion(tamano, grupos):
    population = []
    for i in range(tamano):
        population.append(orden_actividades(grupos))
    return population