def remover1(lista):
    novo = []
    jafoi = []

    for valor in lista:
        if valor not in jafoi:
            novo.append(valor)

        jafoi.append(valor)

    return novo


def remover2(lista):
    d = {}

    for valor in lista:
        d[valor] = d.get(valor, 0) + 1

    novo = []
    for valor in d:
        novo.append(valor)

    return novo


def remover3(lista):
    lista.sort()

    left = 0

    for right in range(1, len(lista)):
        if lista[left] != lista[right]:
            left += 1
            lista[left] = lista[right]

    return lista[:left + 1]


print(remover1([1, 2, 2, 3, 1, 4, 3]))
print(remover2([1, 2, 2, 3, 1, 4, 3]))
print(remover3([1, 2, 2, 3, 1, 4, 3]))
