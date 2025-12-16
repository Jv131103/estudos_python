def contar_unicos(lista):
    d = {}

    for valor in lista:
        d[valor] = d.get(valor, 0) + 1

    lista_unicos = []
    for chave in d:
        if d[chave] <= 1:
            lista_unicos.append(chave)

    return lista_unicos


valores = [1, 2, 3, 1, 4, 2, 1]
lista = contar_unicos(valores)
print(lista)
