lista = [1, 2, 3, 4]
i = 0
j = len(lista) - 1

while i < j:
    lista[i], lista[j] = lista[j], lista[i]
    i += 1
    j -= 1

print(lista)
