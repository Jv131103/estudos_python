def circularizar(lista, k):
    if k >= len(lista):
        return None

    indice = (k + 1) % len(lista)
    return lista[indice]


def circularizar2(lista, k):
    if k >= len(lista):
        return None

    indice = k + 1

    if indice == len(lista):
        indice = 0

    return lista[indice]


def circularizar3(lista, k):
    if k >= len(lista):
        return None

    indice = k + 1

    while indice >= len(lista):
        indice -= len(lista)

    return lista[indice]


if __name__ == "__main__":
    lista = [10, 20, 30, 40]

    print(circularizar(lista.copy(), -1))
    print(circularizar2(lista.copy(), -1))
    print(circularizar3(lista.copy(), -1))
    print(circularizar(lista.copy(), 0))
    print(circularizar2(lista.copy(), 0))
    print(circularizar3(lista.copy(), 0))
    print(circularizar(lista.copy(), 1))
    print(circularizar2(lista.copy(), 1))
    print(circularizar3(lista.copy(), 1))
    print(circularizar(lista.copy(), 2))
    print(circularizar2(lista.copy(), 2))
    print(circularizar3(lista.copy(), 2))
    print(circularizar(lista.copy(), 3))
    print(circularizar2(lista.copy(), 3))
    print(circularizar3(lista.copy(), 3))
    print(circularizar(lista.copy(), 4))
    print(circularizar2(lista.copy(), 4))
    print(circularizar3(lista.copy(), 4))
    print(circularizar(lista.copy(), 7))
    print(circularizar2(lista.copy(), 7))
    print(circularizar3(lista.copy(), 7))
