def ordenar(lista):
    lista = lista.copy()
    novo = []

    while len(lista) != 0:
        menor = min(lista)
        novo.append(menor)
        lista.remove(menor)

    return novo


def ordenar2(lista):
    lista = lista.copy()
    novo = []

    while len(lista) != 0:
        menor = lista[0]

        for x in lista:
            if x < menor:
                menor = x

        novo.append(menor)
        lista.remove(menor)

    return novo


print(ordenar([1, 3, 2, 4, 6, 10, 0, -1]))
print(ordenar2([-1, 3, 2, 4, 6, 10, 0, -1, 12, 32, 9, -2]))
