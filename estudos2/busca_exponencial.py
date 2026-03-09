def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:

        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio

        elif lista[meio] < alvo:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1


def exponential_search(arr, x):

    if arr[0] == x:
        return 0

    i = 1

    while i < len(arr) and arr[i] <= x:
        i *= 2

    return busca_binaria(arr, x)


lista = range(100_000)
print(exponential_search(lista, 0))
print(exponential_search(lista, 15))
print(exponential_search(lista, 50_000))
print(exponential_search(lista, 75_000))
print(exponential_search(lista, 99_000))
