def separar_pares_impares(lista):
    i = 0
    for j in range(len(lista)):
        if lista[j] % 2 == 0:
            lista[i], lista[j] = lista[j], lista[i]

            i += 1

    print(lista)


separar_pares_impares([7, 2, 5, 8, 3, 6])
