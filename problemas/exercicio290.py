def frequencia(lista):
    valores = {}

    for i in lista:
        valores[i] = valores.get(i, 0) + 1

    return valores


valores = [1, 1, 2, 3, 3, 3, 4]
print(frequencia(valores))
