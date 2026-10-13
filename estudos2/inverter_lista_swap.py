def inverter_lista(lista):
    i = 0
    j = len(lista) - 1

    while i < j:
        lista[i], lista[j] = lista[j], lista[i]
        i += 1
        j -= 1


lista = [10, 20, 30, 40, 50]
inverter_lista(lista)
print(lista)
