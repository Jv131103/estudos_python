def fatiar(lista, inicio=0, fim=0, passo=1):
    if not inicio and not fim:
        fim = len(lista)

    novo = []

    for i in range(inicio, fim, passo):
        novo.append(lista[i])

    return novo


lista = [1, 2, 3, 4, 5]
print(fatiar(lista))
print(fatiar(lista, fim=3))
print(fatiar(lista, inicio=3))
print(fatiar(lista, passo=2))
print(fatiar(lista, inicio=len(lista) - 1, fim=-1, passo=-1))
