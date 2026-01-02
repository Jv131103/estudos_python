def contar_maiores(valores, limite):
    return len([v for v in valores if v > limite])


print(contar_maiores([1, 2, 3, 4, 5, 6], 4))
