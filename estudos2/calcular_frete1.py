def calcular_frete(valor_compra, distancia_km):
    frete = 8

    if distancia_km > 5:
        frete += 4

    if valor_compra >= 80:
        frete = 0

    return frete


print(calcular_frete(50, 3))
print(calcular_frete(50, 5))
print(calcular_frete(50, 6))
print(calcular_frete(80, 3))
print(calcular_frete(80, 10))
print(calcular_frete(100, 15))
print(calcular_frete(79, 5))
print(calcular_frete(79, 6))
