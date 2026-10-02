def diferenca(lista1, lista2):
    presentes_lista2 = {}
    ja_adicionados = {}
    resultado = []

    for valor in lista2:
        presentes_lista2[valor] = True

    for valor in lista1:
        if valor not in presentes_lista2 and valor not in ja_adicionados:
            resultado.append(valor)
            ja_adicionados[valor] = True

    return resultado


lista1 = [2, 5, 7, 10, 5, 20]
lista2 = [1, 5, 8, 10, 30]

print(diferenca(lista1, lista2))
