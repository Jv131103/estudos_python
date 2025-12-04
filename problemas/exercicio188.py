def eh_par(x):
    return x % 2 == 0


def filtrar(funcao, iteravel):
    return [item for item in iteravel if funcao(item)]


print(filtrar(eh_par, [1, 2, 3, 4, 5, 6]))
