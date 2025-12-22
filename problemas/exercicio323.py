def repetidos(lista1, lista2):

    lista1.sort()
    lista2.sort()

    tam_lista1 = len(lista1)
    tam_lista2 = len(lista2)

    if tam_lista1 < tam_lista2:
        percorrer = lista1
        analisar = lista2
    else:
        percorrer = lista2
        analisar = lista1

    repetidos = []
    for valor in percorrer:
        if valor in analisar and valor not in repetidos:
            repetidos.append(valor)

    return repetidos


a = [1, 2, 2, 3, 5]
b = [2, 2, 4, 5, 6]
print(repetidos(a, b))
