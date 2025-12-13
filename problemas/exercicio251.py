def percorrer(lista):  # in-place
    for idx, valor in enumerate(lista):
        lista[idx] = valor * 2

    return lista


def percorrer2(lista):
    return [valor * 2 for valor in lista]


numeros = [2, 4, 6, 8, 10]
print(percorrer(numeros.copy()))
print(percorrer2(numeros.copy()))
