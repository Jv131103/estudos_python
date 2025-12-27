def soma_pares(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    return soma


print(soma_pares([1, 2, 3, 4, 5, 6]))
