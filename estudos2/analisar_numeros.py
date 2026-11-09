def analisar_numeros(numeros):
    resultado = {
        "positivos": 0,
        "negativos": 0,
        "zeros": 0,
        "soma_positivos": 0
    }

    for numero in numeros:
        if numero > 0:
            resultado["positivos"] += 1
            resultado["soma_positivos"] += numero
        elif numero < 0:
            resultado["negativos"] += 1
        else:
            resultado["zeros"] += 1

    return resultado


print(analisar_numeros([5, -3, 0, 8, -2, 0, 4]))
print(analisar_numeros([1, 2, 3, 4]))
print(analisar_numeros([-5, -10, -2]))
print(analisar_numeros([0, 0, 0]))
print(analisar_numeros([]))
print(analisar_numeros([1000000, -999999, 0, 1]))
