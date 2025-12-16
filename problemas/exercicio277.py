def calcular_desconto(preco, desconto):
    return preco - (preco * desconto)


preco_original = 100
desconto = 0.2  # 20%
print(calcular_desconto(preco_original, desconto))
