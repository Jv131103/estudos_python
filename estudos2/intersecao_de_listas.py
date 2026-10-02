def intersecao(lista1, lista2):
    novo = []

    for valor1 in lista1:
        if valor1 in lista2 and valor1 not in novo:
            novo.append(valor1)

    return novo


lista1 = [2, 5, 7, 10, 5, 20]
lista2 = [1, 5, 8, 10, 5, 30]
print(intersecao(lista1, lista2))

retorno = intersecao(
    [2, 5, 7, 10],
    [5, 8, 10]
)
print(retorno)

print(intersecao(
    [1, 2, 3],
    [7, 8, 9]
))
