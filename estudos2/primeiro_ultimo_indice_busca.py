def maior_menor_indice(lista, alvo):
    menor = -1
    maior = -1

    for idx, valor in enumerate(lista):
        if valor == alvo:
            if menor == -1:
                menor = idx
            maior = idx

    return menor, maior


def busca_binaria_left(lista, alvo):
    e = 0
    d = len(lista) - 1
    resultado = -1

    while e <= d:
        m = (e + d) // 2

        if lista[m] == alvo:
            resultado = m
            d = m - 1
        elif lista[m] < alvo:
            e = m + 1
        else:
            d = m - 1

    return resultado


def busca_binaria_right(lista, alvo):
    e = 0
    d = len(lista) - 1
    resultado = -1

    while e <= d:
        m = (e + d) // 2

        if lista[m] == alvo:
            resultado = m
            e = m + 1
        elif lista[m] < alvo:
            e = m + 1
        else:
            d = m - 1

    return resultado


def maior_menor_indice2(lista, alvo):
    esquerda = busca_binaria_left(lista, alvo)
    direita = busca_binaria_right(lista, alvo)
    return esquerda, direita


lista = [1, 2, 2, 2, 3, 4, 4, 5]
alvo = 2
print(maior_menor_indice(lista, alvo))
print(maior_menor_indice2(lista, alvo))
