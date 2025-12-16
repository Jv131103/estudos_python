def fibonacci(n):
    cont = 1

    n1 = 0
    n2 = 1

    lista = []

    while cont <= n:
        n1, n2 = n1 + n2, n1

        lista.append(n2)
        cont += 1

    return lista


fibon = fibonacci(5)
print(fibon)
