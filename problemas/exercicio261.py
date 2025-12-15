def soma_positivos(lista):
    soma = 0
    for n in lista:
        if n > 0:
            soma += n
    return soma


print(soma_positivos([-2, 5, -1, 3, 7]))
