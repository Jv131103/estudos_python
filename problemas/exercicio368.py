def soma_quadrados(numeros):
    soma_quadrados = 0
    for numero in numeros:
        soma_quadrados += numero**2
    return soma_quadrados


print(soma_quadrados([2, 4, 6]))
