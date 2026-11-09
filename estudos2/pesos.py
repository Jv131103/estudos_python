def empacotar_produtos(pesos, capacidade):
    caixas = []
    pesos_totais = []

    caixa_atual = []
    peso_atual = 0

    for peso in pesos:
        if peso_atual + peso <= capacidade:
            caixa_atual.append(peso)
            peso_atual += peso
        else:
            pesos_totais.append(peso_atual)
            caixas.append(caixa_atual)
            peso_atual = peso
            caixa_atual = [peso]

    if caixa_atual:
        pesos_totais.append(peso_atual)
        caixas.append(caixa_atual)

    return {
        "caixas": caixas,
        "pesos_totais": pesos_totais,
        "quantidade_caixas": len(caixas)
    }


print(empacotar_produtos([4, 3, 6, 2, 8, 1, 5], 10))
print(empacotar_produtos([5, 5, 5, 5], 10))
print(empacotar_produtos([10, 2, 8], 10))
print(empacotar_produtos([], 10))
