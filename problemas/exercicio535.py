"""
Faça um programa que:

    Receba uma lista de números

    Receba um número k

    Faça a rotação à direita de k posições in place

Não use slicing para criar uma nova lista

"""


def rotacionar(lista, k):
    if not lista:
        return

    n = len(lista)

    novo = [0] * len(lista)
    for i in range(n):
        novo_indice = (i + k) % n   # Esquerda: (i - k) % n
        novo[novo_indice] = lista[i]

    return novo


def rotacionar2(lista, k):
    if not lista:
        return lista

    n = len(lista)
    k %= n

    def reverter(i, j):
        while i < j:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1

    # 1) reverte tudo
    reverter(0, n - 1)

    # 2) reverte os primeiros k
    reverter(0, k - 1)

    # 3) reverte o restante
    reverter(k, n - 1)

    return lista


print(rotacionar([1, 2, 3, 4, 5], 2))
print(rotacionar([1, 2, 3, 4, 5], 3))
print()
print(rotacionar2([1, 2, 3, 4, 5], 2))
print(rotacionar2([1, 2, 3, 4, 5], 3))
