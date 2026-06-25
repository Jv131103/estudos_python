def soma_pares(lista, num):
    i = 0
    j = len(lista) - 1

    while i < j:
        soma = lista[i] + lista[j]
        if soma == num:
            return lista[i], lista[j]
        elif soma < num:
            i += 1
        else:
            j -= 1


print(soma_pares([1, 2, 3, 4, 6, 8, 11], 10))
print(soma_pares([1, 3, 5, 7, 9], 20))
print(soma_pares([1, 2, 3, 4, 6, 8, 11], 12))
print(soma_pares([2, 4, 6, 8], 5))
print(soma_pares([5], 5))
print(soma_pares([], 10))
