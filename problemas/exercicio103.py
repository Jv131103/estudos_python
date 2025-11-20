lista = []
for i in range(1, 4):
    for j in range(1, 5):
        lista.append((i, j))
print(lista)


lista1 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            lista1.append((x, y))
print(lista1)
