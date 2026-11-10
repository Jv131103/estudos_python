def calcular_compras(precos):
    result = {
        "total_original": 0,
        "total_final": 0,
        "descontos_aplicados": 0,
        "economia": 0
    }

    for preco in precos:
        result["total_original"] += preco

        if preco >= 100:
            preco = preco - 10
            result["descontos_aplicados"] += 1

        result["total_final"] += preco

    result["economia"] = result["total_original"] - result["total_final"]

    return result


print(calcular_compras([50, 120, 80, 200]))
print(calcular_compras([10, 20, 30]))
print(calcular_compras([100, 150, 300]))
print(calcular_compras([99, 100, 101]))
print(calcular_compras([]))
print(calcular_compras([0, 1000]))
