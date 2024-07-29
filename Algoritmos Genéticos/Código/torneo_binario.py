import constructivo
def torneo_binario(num_maquinas, num_trabajos, programas, grupos):
    tamano_inicial = len(programas)
    indices_elite = []
    indice = 0
    while len(programas)-indice>(tamano_inicial/2):
        makespan_inic = constructivo.makespan(num_maquinas, num_trabajos,
                                           programas[indice], grupos)
        makespan_fin  = constructivo.makespan(num_maquinas, num_trabajos,
                                           programas[-1-indice], grupos)  
        if makespan_inic < makespan_fin:
            indices_elite.append(indice)
        else:
            indices_elite.append(-1-indice)
        indice += 1
    poblacion_elite = []

    for elemento in indices_elite:
        poblacion_elite.append(programas[elemento])
    return poblacion_elite