import copy
import numpy as np

def ocupacion(num_maquinas, num_trabajos, programa, grupos):
    #[trabajo, maquina, tiempo]
    LLEGADAS    = np.zeros([num_maquinas,num_trabajos], dtype=int)
    SALIDAS     = np.zeros([num_maquinas,num_trabajos], dtype=int)
    espacios    = disponibilidad_inicial(num_maquinas)
    for actividad in programa:
        introducir_actividad(LLEGADAS, SALIDAS, actividad, espacios, grupos)
    return LLEGADAS, SALIDAS, espacios
             
def disponibilidad_inicial(num_maquinas):
    ESPACIOS    = []
    for maquina in range(num_maquinas):
        espacios_maquina    = []
        ESPACIOS.append(espacios_maquina)
    return ESPACIOS

def introducir_actividad(LLEGADAS, SALIDAS, actividad, espacios, grupos):
    trabajo_intro   = actividad[0]
    maquina_intro   = actividad[1]
    tiempo_pedido   = actividad[2]
    tiempo_llegada  = LLEGADAS[maquina_intro][trabajo_intro]

    fila_c          = copy.deepcopy(espacios)
    fila            = fila_c[maquina_intro]
    posicion_fila   = 0

    for trabajo_fila in fila:
        llegada_tr_fila  = LLEGADAS[maquina_intro][trabajo_fila]
        trabajo_previo   = fila[posicion_fila-1] if posicion_fila > 0 else None
        salida_tr_previo = SALIDAS[maquina_intro][trabajo_previo] if trabajo_previo is not None else 0
        espacio_blanco   = llegada_tr_fila - salida_tr_previo

        if tiempo_llegada > llegada_tr_fila:
            posicion_fila += 1
        elif tiempo_pedido > espacio_blanco:
            posicion_fila += 1
        else:
            break

    espacios[maquina_intro].insert(posicion_fila, trabajo_intro)
    tiempos_ocupacion(LLEGADAS, SALIDAS, actividad, espacios, grupos)
    trabajos_desplazados = fila_c[maquina_intro][posicion_fila+1:]
    
    for i in range(len(trabajos_desplazados)):
        espacios[maquina_intro][posicion_fila+1+i] = fila_c[maquina_intro][posicion_fila+i]


def tiempos_ocupacion(LLEGADAS, SALIDAS, actividad, espacios, grupos):
    trabajo_intro   = actividad[0]
    maquina_intro   = actividad[1]
    tiempo_pedido   = actividad[2]
    pos_llegada     = espacios[maquina_intro].index(trabajo_intro)
    tiempo_llegada  = LLEGADAS[maquina_intro][trabajo_intro]

    indc_secuencia  = grupos[trabajo_intro].index(actividad)
    act_siguiente = []
    if indc_secuencia < len(grupos[trabajo_intro])-1:
        act_siguiente   = grupos[trabajo_intro][indc_secuencia+1]
        maquina_sgte    = act_siguiente[1]
    if pos_llegada == 0:
        tiempo_salida = tiempo_llegada + tiempo_pedido
        SALIDAS[maquina_intro][trabajo_intro] = tiempo_salida
        if act_siguiente:
            LLEGADAS[maquina_sgte][trabajo_intro] = tiempo_salida
    else:
        indc_tr_previo   = espacios[maquina_intro].index(trabajo_intro)-1
        trabajo_previo   = espacios[maquina_intro][indc_tr_previo]
        salida_tr_previo = SALIDAS[maquina_intro][trabajo_previo]
        tiempo_salida    = max(salida_tr_previo, tiempo_llegada)+tiempo_pedido
        SALIDAS[maquina_intro][trabajo_intro] = tiempo_salida
        if act_siguiente:
            LLEGADAS[maquina_sgte][trabajo_intro] = tiempo_salida
