def contar_frequencias(numeros):
    frequencias = [0] * 10

    for numero in numeros:
        frequencias[numero] += 1

    return frequencias


numeros = [3, 1, 3, 0, 9, 1, 3]

print(contar_frequencias(numeros))
