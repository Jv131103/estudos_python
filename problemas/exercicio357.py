def sem_duplicatas(valores):
    vistos = set()
    resultado = []

    for v in valores:
        if v not in vistos:
            resultado.append(v)
            vistos.add(v)

    return resultado


print(sem_duplicatas([1, 2, 2, 3, 1, 4, 4, 5]))
