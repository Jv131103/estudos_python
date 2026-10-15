def contar_repeticoes(lista):
    if not lista:
        return []

    repeticoes = [0] * len(lista)

    cont = 1

    repeticoes[0] = 1
    anterior = lista[0]
    for indice in range(1, len(lista)):
        if anterior == lista[indice]:
            cont += 1
        else:
            anterior = lista[indice]
            cont = 1
        repeticoes[indice] = cont

    return repeticoes


def contar_repeticoes2(lista):
    if not lista:
        return []

    repeticoes = [0] * len(lista)

    cont = 1

    for indice in range(0, len(lista)):
        if lista[indice] == lista[indice - 1]:
            cont += 1
        else:
            cont = 1
        repeticoes[indice] = cont

    return repeticoes


lista = [2, 2, 2, 5, 5, 3, 3, 3, 1]

print(contar_repeticoes(lista))
print(contar_repeticoes2(lista))
