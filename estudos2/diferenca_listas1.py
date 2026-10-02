def diferenca(lista1, lista2):
    resultado = []

    for valor in lista1:
        if valor not in lista2 and valor not in resultado:
            resultado.append(valor)

    return resultado


lista1 = [2, 5, 7, 10, 5, 20]
lista2 = [1, 5, 8, 10, 30]

print(diferenca(lista1, lista2))
