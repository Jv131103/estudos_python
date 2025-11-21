def pesquisa(lista, valor):
    return valor in lista


def pesquisa2(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False


def pesquisa3(lista, valor):
    lista = sorted(lista)

    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            return True

        if valor < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return False


def pesquisa4(lista, valor):
    # pesquisa interpolada
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim and lista[inicio] <= valor <= lista[fim]:
        meio = inicio + (valor - lista[inicio]) * (fim - inicio) // (lista[fim] - lista[inicio])

        if lista[meio] == valor:
            return True

        if lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return False


print(pesquisa(list("abcde"), 'a'))
print(pesquisa2(list("abcde"), 'a'))
print(pesquisa3(list("abcde"), 'a'))
print(pesquisa4(list("abcde"), 'a'))
