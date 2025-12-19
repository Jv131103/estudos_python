def diferenca(a, b):
    diferentes = set(a) - set(b)
    return list(diferentes)


def diferenca2(a, b):
    tamA, tamB = len(a), len(b)

    lista_a_percorrer, lista_a_verificar = (a, b) if tamA > tamB else (b, a)

    novo = []
    for valor in lista_a_percorrer:
        if valor not in lista_a_verificar:
            novo.append(valor)

    return novo


a = [1, 2, 3, 4]
b = [2, 4]
print(diferenca(a, b))
print(diferenca2(a, b))
