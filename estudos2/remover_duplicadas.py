def remover_duplicadas(lista):
    novo = []
    for valor in lista:
        if valor not in novo:
            novo.append(valor)

    return novo


def remover_duplicadas_inplace(lista):
    i = 0
    visto = []

    for j in range(len(lista)):
        if lista[j] not in visto:
            visto.append(lista[j])
            lista[i] = lista[j]
            i += 1

    del lista[i:]
    return lista


print(remover_duplicadas([4, 7, 4, 2, 7, 9, 2, 10]))
print(remover_duplicadas_inplace([4, 7, 4, 2, 7, 9, 2, 10]))
