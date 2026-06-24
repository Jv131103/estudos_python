def mover_zeros(lista):
    if not lista:
        raise ValueError("Lista vazia!")

    nao_zeros = []
    zeros = []

    for valor in lista:
        if valor == 0:
            zeros.append(valor)
        else:
            nao_zeros.append(valor)

    nao_zeros.extend(zeros)

    return nao_zeros


def mover_zeros2(lista):
    if not lista:
        raise ValueError("Lista vazia!")

    pos = 0

    for i in range(len(lista)):
        if lista[i] != 0:
            lista[pos], lista[i] = lista[i], lista[pos]
            pos += 1

    return lista


print(mover_zeros([0, 1, 0, 3, 12]))
print(mover_zeros2([0, 1, 0, 3, 12]))
