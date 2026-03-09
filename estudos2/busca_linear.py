lista = [10, 20, 30, 40, 50]


def busca_linear(lista, alvo):

    for i in range(len(lista)):
        if lista[i] == alvo:
            return i

    return -1


print(busca_linear(lista, 10))
print(busca_linear(lista, 30))
print(busca_linear(lista, 50))
