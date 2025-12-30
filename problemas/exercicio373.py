def frequencia_numerica(numeros):
    d = {
        "positivos": 0,
        "zero": 0,
        "negativos": 0,
    }
    for numero in numeros:
        if numero > 0:
            d["positivos"] += 1
        elif numero < 0:
            d['negativos'] += 1
        else:
            d["zero"] += 1

    return d


print(frequencia_numerica(list(range(-10, 11))))
