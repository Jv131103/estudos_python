def encontrar_ponto_rotacao(lista):
    if not lista:
        raise ValueError("lista não pode ser vazia")

    esquerda = 0
    direita = len(lista) - 1

    while esquerda < direita:
        meio = (esquerda + direita) // 2

        if lista[meio] > lista[direita]:
            esquerda = meio + 1
        else:
            direita = meio

    return esquerda


def encontrar_ponto_rotacao_linear(lista):
    if not lista:
        raise ValueError("lista não pode ser vazia")

    for i in range(1, len(lista)):
        if lista[i] < lista[i - 1]:
            return i

    return 0


def encontrar_ponto_rotacao_min_manual(lista):
    if not lista:
        raise ValueError("lista não pode ser vazia")

    menor = lista[0]
    indice = 0

    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice = i

    return indice


def encontrar_ponto_rotacao_vizinhos(lista):
    if not lista:
        raise ValueError("lista não pode ser vazia")

    n = len(lista)
    e = 0
    d = n - 1

    while e <= d:
        if lista[e] <= lista[d]:
            return e

        m = (e + d) // 2
        prox = (m + 1) % n
        ant = (m - 1 + n) % n

        if lista[m] <= lista[prox] and lista[m] <= lista[ant]:
            return m

        if lista[m] >= lista[e]:
            e = m + 1
        else:
            d = m - 1


def encontrar_ponto_rotacao_binaria(lista):
    if not lista:
        raise ValueError("lista não pode ser vazia")

    e = 0
    d = len(lista) - 1

    while e < d:
        m = (e + d) // 2

        if lista[m] > lista[d]:
            e = m + 1
        else:
            d = m

    return e


if __name__ == "__main__":

    lista = [15, 18, 2, 3, 6, 12]
    indice = encontrar_ponto_rotacao(lista)
    print(indice)
    print(lista[indice])
