def rotacionar_direita(lista):
    ultimo = lista[-1]

    for i in range(len(lista) - 1, 0, -1):
        lista[i] = lista[i - 1]

    lista[0] = ultimo
    return lista


def rotacionar_esquerda(lista):
    primeiro = lista[0]

    for i in range(len(lista) - 1):
        lista[i] = lista[i + 1]

    lista[-1] = primeiro
    return lista


lista = [1, 2, 3, 4, 5]
print(rotacionar_direita(lista))
print(rotacionar_direita(lista))
print(rotacionar_direita(lista))
print(rotacionar_direita(lista))
print(rotacionar_direita(lista))
print()
print(rotacionar_esquerda(lista))
print(rotacionar_esquerda(lista))
print(rotacionar_esquerda(lista))
print(rotacionar_esquerda(lista))
print(rotacionar_esquerda(lista))
