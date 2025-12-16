def media(lista):
    total = 0
    tam = len(lista)
    for i in range(tam):
        total += lista[i]
    return total / tam


lista = [1, 2, 3, 4, 5]
print(media(lista))
