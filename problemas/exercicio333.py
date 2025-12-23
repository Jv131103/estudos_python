def pares(lista):
    n = len(lista)
    return [(lista[i], lista[n - 1 - i]) for i in range(n // 2)]


print(pares([1, 2, 3, 4, 5]))
