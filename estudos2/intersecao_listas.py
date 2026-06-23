def modelo1(lista1, lista2):
    novo = []
    for valor in lista1:
        for item in lista2:
            if valor == item:
                novo.append(valor)

    return novo


def modelo2(lista1, lista2):
    novo = []

    for valor in lista2:
        if valor in lista1:
            novo.append(valor)

    return novo


def modelo3(lista1, lista2):
    lista1 = sorted(lista1)
    lista2 = sorted(lista2)

    novo = []

    i = 0
    j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] == lista2[j]:
            novo.append(lista1[i])
            i += 1
            j += 1
        elif lista1[i] < lista2[j]:
            i += 1
        else:
            j += 1

    return novo


lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

print(modelo1(lista1, lista2))
print(modelo2(lista1, lista2))
print(modelo3(lista1, lista2))
