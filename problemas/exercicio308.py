def soma_acumulada(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma


def soma_acumulada_versatil(lista):
    return sum(lista)


print(soma_acumulada([1, 2, 3, 4]))
print(soma_acumulada_versatil([1, 2, 3, 4]))
