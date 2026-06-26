def trocar1(lista, i, j):
    if i >= len(lista) or j >= len(lista):
        raise IndexError(f"Indice ultrapassa tamanho da lista de {len(lista)}")

    lista[i], lista[j] = lista[j], lista[i]
    return lista


def trocar2(lista, i, j):
    if i >= len(lista) or j >= len(lista):
        raise IndexError(f"Indice ultrapassa tamanho da lista de {len(lista)}")

    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp
    return lista


print(trocar1([10, 20, 30, 40], 1, 3))
print(trocar2([10, 20, 30, 40], 1, 3))
