def rotacionar(lista, k):
    n = len(lista)
    k = k % n

    return lista[-k:] + lista[:-k]


def rotacionar2(lista, k):
    n = len(lista)

    k = k % n

    for _ in range(k):
        ultimo = lista[-1]

        for i in range(n - 1, 0, -1):
            lista[i] = lista[i - 1]

        lista[0] = ultimo

    return lista


def rotacionar3(lista, k):
    n = len(lista)
    if n == 0:
        return lista

    k %= n
    nova = [0] * n

    for i in range(n):
        novo_indice = (i + k) % n
        nova[novo_indice] = lista[i]

    return nova


def inverter(lista, ini, fim):
    while ini < fim:
        lista[ini], lista[fim] = lista[fim], lista[ini]
        ini += 1
        fim -= 1


def rotacionar4(lista, k):
    n = len(lista)
    if n == 0:
        return lista

    k %= n
    if k == 0:
        return lista

    inverter(lista, 0, n - 1)
    inverter(lista, 0, k - 1)
    inverter(lista, k, n - 1)

    return lista


def rotacionar5(lista, k):
    n = len(lista)
    if n == 0:
        return lista

    k %= n
    return [lista[(i - k) % n] for i in range(n)]


def rotacionar6(lista, k):
    n = len(lista)
    if n == 0:
        return lista

    k %= n

    for _ in range(k):
        ultimo = lista.pop()
        lista.insert(0, ultimo)

    return lista


def rotacionar7(lista, k):
    n = len(lista)
    if n == 0:
        return lista

    k %= n
    dupla = lista + lista
    inicio = n - k
    fim = inicio + n

    resultado = []
    for i in range(inicio, fim):
        resultado.append(dupla[i])

    return resultado


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(rotacionar(lista.copy(), 2))
    print(rotacionar2(lista.copy(), 2))
    print(rotacionar3(lista.copy(), 2))
    print(rotacionar4(lista.copy(), 2))
    print(rotacionar5(lista.copy(), 2))
    print(rotacionar6(lista.copy(), 2))
    print(rotacionar7(lista.copy(), 2))
