def encontrar_extremos(numeros):
    if not numeros:
        return {'maior': None, 'menor': None}

    d = {
        "maior": numeros[0],
        "menor": numeros[0]
    }

    for valor in numeros[1:]:
        if valor > d["maior"]:
            d["maior"] = valor

        if valor < d["menor"]:
            d["menor"] = valor

    return d


print(encontrar_extremos([8, 3, 15, 2, 10]))
# {'maior': 15, 'menor': 2}

print(encontrar_extremos([-8, -3, -15, -2]))
# {'maior': -2, 'menor': -15}

print(encontrar_extremos([7, 7, 7]))
# {'maior': 7, 'menor': 7}

print(encontrar_extremos([42]))
# {'maior': 42, 'menor': 42}

print(encontrar_extremos([]))
# {'maior': None, 'menor': None}

print(encontrar_extremos([100, -100, 0, 50]))
# {'maior': 100, 'menor': -100}
