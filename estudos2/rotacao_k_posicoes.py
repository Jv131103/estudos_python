def rotacionar_direita(lista, k):
    n = len(lista)
    k = k % n

    return lista[-k:] + lista[:-k]


def rotacionar_direita2(lista, k):
    n = len(lista)

    k = k % n

    for _ in range(k):
        ultimo = lista[-1]

        for i in range(n - 1, 0, -1):
            lista[i] = lista[i - 1]

        lista[0] = ultimo

    return lista


def rotacionar_esquerda(lista, k):
    n = len(lista)
    k = k % n

    return lista[k:] + lista[:k]


def rotacionar_esquerda2(lista, k):
    n = len(lista)

    k = k % n

    for _ in range(k):
        primeiro = lista[0]

        for i in range(n - 1):
            lista[i] = lista[i + 1]

        lista[-1] = primeiro

    return lista


lista = [1, 2, 3, 4, 5]
print(rotacionar_direita(lista.copy(), 2))
print(rotacionar_direita2(lista.copy(), 2))
print()
print(rotacionar_esquerda(lista.copy(), 2))
print(rotacionar_esquerda2(lista.copy(), 2))
