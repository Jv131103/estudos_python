def soma(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


def soma_recursiva(lista, i=0):
    if i >= len(lista):
        return 0

    return lista[i] + soma_recursiva(lista, i + 1)


print(soma([1, 2, 3, 4]))
print(soma_recursiva([1, 2, 3, 4]))
