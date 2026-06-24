
def inverter_inplace(lista):
    i = 0
    j = len(lista) - 1

    while i < j:
        lista[i], lista[j] = lista[j], lista[i]
        i += 1
        j -= 1

    return lista


def inverter_nao_inplace(lista):
    novo = []

    for i in range(len(lista) - 1, -1, -1):
        novo.append(lista[i])

    return novo


def inverter_nao_inplace2(lista):
    return lista[::-1]


lista = [1, 2, 3, 4]
print(inverter_inplace(lista.copy()))
print(inverter_nao_inplace(lista))
print(inverter_nao_inplace2(lista))
