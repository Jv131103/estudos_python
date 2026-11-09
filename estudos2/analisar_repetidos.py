def analisar_repetidos(numeros):
    contador = {}

    for numero in numeros:
        contador[numero] = contador.get(numero, 0) + 1

    final = {
        "unicos": [],
        "repetidos": [],
        "frequencias": contador
    }

    for valor, total in contador.items():
        if total > 1:
            final["repetidos"].append(valor)
        else:
            final["unicos"].append(valor)

    return final


print(analisar_repetidos([4, 2, 4, 7, 2, 9, 4]))
print(analisar_repetidos([1, 2, 3]))
print(analisar_repetidos([5, 5, 5]))
print(analisar_repetidos([0, -1, 0, -1, 2]))
print(analisar_repetidos([]))
