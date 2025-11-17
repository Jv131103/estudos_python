serie = list(range(1900, 2021))


def primeiros_20(lista):
    lista_20 = []

    cont = 0
    primeiro = 0

    while cont < len(lista) and primeiro < 20:
        lista_20.append(lista[cont])
        cont += 1
        primeiro += 1

    return lista_20


def lista_1937_a_1969(lista):
    lista_1937_a_1969 = []

    for valores in lista:
        if 1937 <= valores <= 1969:
            lista_1937_a_1969.append(valores)

    return lista_1937_a_1969


def de_2010_ate_2020(lista):
    lista_2010_a_2020 = []

    for valores in lista:
        if 2010 <= valores <= 2020:
            lista_2010_a_2020.append(valores)

    return lista_2010_a_2020


def lista_ultimo(lista):
    return [lista[-1]]


def lista_10_em_10(lista):
    lista_10_em_10 = []

    for valores in range(0, len(lista), 10):
        lista_10_em_10.append(lista[valores])

    return lista_10_em_10


print(primeiros_20(serie))
print(lista_1937_a_1969(serie))
print(de_2010_ate_2020(serie))
print(lista_ultimo(serie))
print(lista_10_em_10(serie))
