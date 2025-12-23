def mostrar_ponteiros(lista):
    i = 0
    j = len(lista) - 1

    while i < j:
        print(lista[i], lista[j])
        i += 1
        j -= 1


mostrar_ponteiros([1, 2, 3, 4, 5])
