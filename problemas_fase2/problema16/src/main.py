def busca1(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i

    return -1


def busca2(lista, alvo):
    i = 0
    for valor in lista:
        if valor == alvo:
            return i

        i += 1

    return -1


def busca3(lista, alvo):
    for idx, valor in enumerate(lista):
        if valor == alvo:
            return idx

    return -1


def busca4(lista, alvo):
    i = 0

    while i < len(lista):
        if lista[i] == alvo:
            return i
        i += 1

    return -1


def busca5(lista, alvo):

    n = len(lista)

    lista.append(alvo)

    i = 0
    while lista[i] != alvo:
        i += 1

    lista.pop()

    if i < n:
        return i

    return -1


def busca6(lista, alvo):
    try:
        return lista.index(alvo)
    except ValueError:
        return -1


def busca7(lista, alvo):

    indices = [i for i, v in enumerate(lista) if v == alvo]

    return indices[0] if indices else -1


def busca8(lista, alvo, i=0):
    if i == len(lista):
        return -1

    if lista[i] == alvo:
        return i

    return busca8(lista, alvo, i + 1)


if __name__ == "__main__":
    lista = [7, 3, 9, 1, 3]
    alvo = 3

    print(busca1(lista, alvo))
    print(busca2(lista, alvo))
    print(busca3(lista, alvo))
    print(busca4(lista, alvo))
    print(busca5(lista, alvo))
    print(busca6(lista, alvo))
    print(busca7(lista, alvo))
    print(busca8(lista, alvo))
