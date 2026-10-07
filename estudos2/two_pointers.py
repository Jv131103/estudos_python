def encontrar_pares(lista, alvo):
    lista = sorted(lista)

    esquerda = 0
    direita = len(lista) - 1

    pares = []

    while esquerda < direita:
        soma = lista[esquerda] + lista[direita]

        if soma == alvo:
            pares.append([lista[esquerda], lista[direita]])
            esquerda += 1
            direita -= 1
        elif soma < alvo:
            esquerda += 1
        else:
            direita -= 1

    if not pares:
        return None
    return pares


def encontrar_par(lista, alvo):
    lista = sorted(lista)

    esquerda = 0
    direita = len(lista) - 1

    while esquerda < direita:
        soma = lista[esquerda] + lista[direita]

        if soma == alvo:
            return [lista[esquerda], lista[direita]]
        elif soma < alvo:
            esquerda += 1
        else:
            direita -= 1

    return None


lista = [1, 2, 3, 4, 6, 8, 10, 12]
alvo = 10

print(encontrar_par(lista, alvo))
print(encontrar_pares(lista, alvo))
print()
print(encontrar_par([1, 2, 3, 4, 6, 8, 10], 9))
print(encontrar_pares([1, 2, 3, 4, 6, 8, 10], 9))
print()
print(encontrar_par([1, 3, 5, 7], 20))
print(encontrar_pares([1, 3, 5, 7], 20))
print()
print(encontrar_par([-10, -5, 0, 3, 8, 15], 5))
print(encontrar_pares([-10, -5, 0, 3, 8, 15], 5))
