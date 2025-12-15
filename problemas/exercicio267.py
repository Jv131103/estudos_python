def apenas_pares(lista):
    return [n for n in lista if n % 2 == 0]


numeros = [1, 2, 3, 4, 5]
print(apenas_pares(numeros))
