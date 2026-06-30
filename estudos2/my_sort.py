lista = [99, 5, 66, 25, 2]

for i in range(len(lista)):
    for j in range(i + 1):
        if lista[i] <= lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

print(lista)


lista = [0, 99, 5, 66, 25, 2, 90]

for i in range(len(lista)):
    for j in range(i + 1):
        if lista[i] >= lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

print(lista)
