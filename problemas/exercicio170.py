def lista_pares(lista):
    lista_pares = []

    for i in range(len(lista)):
        if lista[i] & 1 == 0:
            lista_pares.append(lista[i])
    return lista_pares


lista = [1, 2, 3, 10, 17, 20]
print(lista_pares(lista))
