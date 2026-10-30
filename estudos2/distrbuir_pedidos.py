def distribuir_pedidos(pedidos):
    caixas = [[], [], []]
    totais = [0, 0, 0]
    quantidades = [0, 0, 0]

    for i in range(0, len(pedidos)):
        d = i % 3
        pedido = pedidos[i]
        caixas[d].append(pedido)
        totais[d] += pedido
        quantidades[d] += 1

    return {
        "caixas": caixas,
        "totais": totais,
        "quantidades": quantidades
    }


pedidos = [20, 35, 10, 50, 5, 15, 30]
print(distribuir_pedidos(pedidos))
