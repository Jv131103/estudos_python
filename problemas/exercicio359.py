def filtrar(numeros, limite):
    return [numero for numero in numeros if numero > limite]


print(filtrar(list(range(1, 20)), 10))
