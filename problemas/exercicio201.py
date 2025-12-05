def indices_de(lista, valor):
    lista_indices = []

    for indice in range(len(lista)):
        if lista[indice] == valor:
            lista_indices.append(indice)

    return lista_indices


print(indices_de([1, 3, 3, 5, 3, 8], 3))
