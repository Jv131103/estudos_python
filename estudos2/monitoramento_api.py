
def analisar_status(status):
    tabela = [
        ["sucessos", 200, 299],
        ["erros_cliente", 400, 499],
        ["erros_servidor", 500, 599]
    ]

    resultado = {
        "sucessos": 0,
        "erros_cliente": 0,
        "erros_servidor": 0,
        "total": 0
    }

    tot = 0
    for valor in status:
        for sts, x1, x2 in tabela:
            if x1 <= valor <= x2:
                resultado[sts] = resultado.get(sts, 0) + 1

        tot += 1

    resultado["total"] = tot

    return resultado


def analisar_status2(status):
    resultado = {
        "sucessos": 0,
        "erros_cliente": 0,
        "erros_servidor": 0,
        "total": 0
    }

    for valor in status:
        if 200 <= valor <= 299:
            resultado["sucessos"] += 1
        elif 400 <= valor <= 499:
            resultado["erros_cliente"] += 1
        elif 500 <= valor <= 599:
            resultado["erros_servidor"] += 1

        resultado["total"] += 1

    return resultado


print(analisar_status([200, 404, 200, 500, 200, 404, 503, 200]))
print(analisar_status2([200, 404, 200, 500, 200, 404, 503, 200]))
print()
print(analisar_status([201, 204, 400, 502]))
print(analisar_status2([201, 204, 400, 502]))
print()
print(analisar_status([]))
print(analisar_status2([]))
print()
print(analisar_status([200]))
print(analisar_status2([200]))
