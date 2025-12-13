def contar_pares(numeros):
    total = 0
    for n in numeros:
        if n % 2 == 0:
            total += 1
    return total


print(contar_pares([1, 2, 3, 4, 5, 6]))
