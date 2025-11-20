lista = []
cont = 0
for i in list(range(5, 15)):
    lista.append((i, cont))
    cont += 1
print(lista)

lista = [(indice, valor) for indice, valor in enumerate(range(10), start=5)]
print(lista)

print()

lista1 = []
for i in list(range(0, 10)):
    lista1.append((i, i * i))
print(lista1)

lista1 = [(x, x**2) for x in range(10)]
print(lista1)
