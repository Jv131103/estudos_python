def shift_direita(lista):
    n = len(lista)

    # começa do fim para não sobrescrever valores
    for i in range(n - 1, 0, -1):
        lista[i] = lista[i - 1]

    lista[0] = 0  # valor novo entra no começo

    return lista


def shift_esquerda(lista):
    n = len(lista)

    for i in range(n - 1):
        lista[i] = lista[i + 1]

    lista[n - 1] = 0  # novo valor no final

    return lista


def shift_circular_direita(lista):
    n = len(lista)
    ultimo = lista[n - 1]

    for i in range(n - 1, 0, -1):
        lista[i] = lista[i - 1]

    lista[0] = ultimo

    return lista


def shift_circular_esquerda(lista):
    n = len(lista)
    primeiro = lista[0]

    for i in range(0, n - 1):
        lista[i] = lista[i + 1]

    lista[-1] = primeiro

    return lista


def remover_inicio_shift(lista):
    n = len(lista)

    for i in range(n - 1):
        lista[i] = lista[i + 1]

    lista.pop()  # remove o último (agora duplicado)

    return lista


a = [1, 2, 3, 4]
# print(shift_direita(a))
# print(shift_esquerda(a))
# print(shift_circular_direita(a))
# print(shift_circular_esquerda(a))
print(remover_inicio_shift(a))
