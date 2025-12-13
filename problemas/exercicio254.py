def positivo_ou_negativo(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "zero"


valores = list(range(-10, 11))
for valor in valores:
    print(f"{valor}: {positivo_ou_negativo(valor)}")
