def tranformar(lista):
    novo = []

    for i in lista:
        if i % 2 == 0:
            novo.append(i)
        else:
            novo.append(i * 2)

    return novo


numeros = [1, 2, 3, 4]
print(tranformar(numeros))
