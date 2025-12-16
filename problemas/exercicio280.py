def numeros_quadrados(n):
    lista = []
    for i in range(1, n + 1):
        lista.append(i**2)

    return lista


lista = numeros_quadrados(4)
print(lista)
