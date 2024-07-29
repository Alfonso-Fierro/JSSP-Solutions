import random
import lector
import constructivo
import poblacion
import mutacion
import torneo_binario
import cruce
import grupos
import copy
def algoritmo_genetico(nombre_archivo, tamano_poblacion,generaciones,
                       dominancia,probabilidad_mutacion):
    num_trabajos, num_maquinas, tiempos, secuencias = lector.leer_txt(nombre_archivo)
    grups   = grupos.agrupamiento(num_trabajos,num_maquinas,secuencias,tiempos)
    poblacn = poblacion.generar_poblacion(tamano_poblacion,grups)
    for generacion in range(generaciones):
        poblacion_hijos = cruce.cruce_poblacional(poblacn, dominancia,grups)
        for hijo in poblacion_hijos:
            dado = random.random()
            if dado < probabilidad_mutacion:
                hijo = mutacion.mutacion(num_maquinas, num_trabajos, hijo,grups)
        poblacn = torneo_binario.torneo_binario(num_maquinas, num_trabajos,
                                                poblacion_hijos, grups)
    mejor_solucion = poblacn[0]
    makespan_mjr_sol = constructivo.makespan(num_maquinas, num_trabajos,
                                             mejor_solucion, grups)
    for programa in poblacn:
        makespan_programa = constructivo.makespan(num_maquinas, num_trabajos,
                                                  programa, grups)
        if makespan_programa <= makespan_mjr_sol:
            mejor_solucion = copy.deepcopy(programa)
            makespan_mjr_sol = makespan_programa
        
    return mejor_solucion
    