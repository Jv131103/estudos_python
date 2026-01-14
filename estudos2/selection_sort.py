lista = [3, 2, 4, 5, 9, 9, 0]

n = len(lista)

for i in range(n):
    menor = i
    for j in range(i + 1, n):
        if lista[j] < lista[menor]:
            menor = j

    lista[i], lista[menor] = lista[menor], lista[i]

print(lista)
