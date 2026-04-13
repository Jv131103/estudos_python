def forma_ruim():
    numeros = [1, 2, 3, 4]

    for i in numeros:
        if i % 2 == 0:
            numeros.remove(i)

    print(numeros)


def forma_boa():
    numeros = [1, 2, 3, 4]

    for i in numeros[:]:
        if i % 2 == 0:
            numeros.remove(i)

    print(numeros)


forma_ruim()
forma_boa()
