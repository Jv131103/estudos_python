def soma_estrutural1(lista):
    soma = 0

    for valor in lista:
        soma += valor

    return soma


def soma_estrutural2(lista):
    soma = 0

    for valor in range(len(lista)):
        soma += lista[valor]

    return soma


def soma_estrutural3(lista):
    soma = 0

    i = 0
    for _ in range(len(lista)):
        soma += lista[i]
        i += 1

    return soma
