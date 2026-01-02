def soma_indices_pares(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]
    return soma


print(soma_indices_pares([10, 20, 30, 40, 50]))
