def quadrado(x):
    return x * x


def aplicar(funcao, iteravel):
    lista = []
    for valor in iteravel:
        lista.append(funcao(valor))

    return lista


print(aplicar(quadrado, [1, 2, 3, 4]))
