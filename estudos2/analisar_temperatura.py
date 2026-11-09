def analisar_temperaturas(temperaturas):
    resultado = {
        "quentes": 0,
        "agradaveis": 0,
        "frios": 0
    }

    for temperatura in temperaturas:
        if temperatura > 30:
            r = "quentes"
        elif 20 <= temperatura <= 30:
            r = "agradaveis"
        else:
            r = "frios"

        resultado[r] += 1

    return resultado


print(analisar_temperaturas([18, 25, 32, 15, 30, 35, 22]))
print(analisar_temperaturas([31, 35, 40]))
print(analisar_temperaturas([10, 15, 19]))
print(analisar_temperaturas([20, 30]))
print(analisar_temperaturas([]))
