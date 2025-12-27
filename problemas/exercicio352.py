def unicos(lista):
    novo = []
    for valor in lista:
        cont = 0
        for idy in range(len(lista)):
            if lista[idy] == valor:
                cont += 1

        if cont == 1:
            novo.append(valor)

    return novo


def unicos1(lista):
    d = {}

    for valores in lista:
        d[valores] = d.get(valores, 0) + 1

    novo = []
    for key in d.keys():
        if d[key] == 1:
            novo.append(key)

    return novo


print(unicos([1, 2, 2, 3, 4, 4, 5]))
print(unicos1([1, 2, 2, 3, 4, 4, 5]))
