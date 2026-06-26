def particionar(lista, pivo):
    valor_pivo = lista[pivo]
    lista[pivo], lista[-1] = lista[-1], lista[pivo]

    i = 0

    for j in range(len(lista) - 1):
        if lista[j] <= valor_pivo:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1

    lista[i], lista[-1] = lista[-1], lista[i]

    return lista


print(particionar([8, 3, 1, 7, 0, 10, 2], 2))
