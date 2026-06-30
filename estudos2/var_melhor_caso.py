precos_acoes = [24.50, 22.10, 28.90, 19.80, 21.00]

# Iniciamos assumindo que o primeiro preço é o menor de todos
preco_mais_barato = precos_acoes[0]  # <-- VARIÁVEL DE MELHOR CASO

for preco in precos_acoes:
    if preco < preco_mais_barato:
        preco_mais_barato = preco  # Atualiza o recorde absoluto de menor preço

print(f"O melhor momento de compra é quando a ação atingir: R$ {preco_mais_barato}")
# Saída: R$ 19.80
