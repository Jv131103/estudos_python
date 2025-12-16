def primeiros_impares(numero):
    i = 1
    cont = 0
    lista = []

    while cont < numero:
        if i % 2 != 0:
            lista.append(i)
            i += 2
        cont += 1

    return lista


def primeiros_impares1(numero):
    return [i for i in range(0, numero + numero) if i % 2 != 0]


print(primeiros_impares(5))
print(primeiros_impares1(5))
print()
print(primeiros_impares(8))
print(primeiros_impares1(8))
