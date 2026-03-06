def inverter(lista, inicio, fim):

    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1


def rotacionar(lista, k):

    n = len(lista)
    k %= n

    inverter(lista, 0, n - 1)
    inverter(lista, 0, k - 1)
    inverter(lista, k, n - 1)


lista = [1, 2, 3, 4]
rotacionar(lista, 2)
print(lista)
