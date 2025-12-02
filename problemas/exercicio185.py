def agrupar(lista):
    dicionario = {}

    for valor in lista:
        if valor not in dicionario:
            dicionario[valor] = [valor]
        else:
            dicionario[valor].append(valor)

    return dicionario


print(agrupar([1, 2, 1, 3, 2, 1, 4, 2]))
