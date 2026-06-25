def quadrados_ordenados(lista):
    quadrados = [valor**2 for valor in lista]

    i = 0
    j = len(lista) - 1

    novo = [0] * len(quadrados)
    k = len(quadrados) - 1
    while i <= j:
        if quadrados[i] > quadrados[j]:
            novo[k] = quadrados[i]
            i += 1
        else:
            novo[k] = quadrados[j]
            j -= 1

        k -= 1

    return novo


# Se a lista estiver ordenada, ok
print(quadrados_ordenados([-4, -1, 0, 3, 10]))
