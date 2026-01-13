"""
Crie:

    Uma constante de taxa de imposto

    Uma variável de preço

    Calcule o valor do imposto usando a constante

Não use números soltos no cálculo.
"""

TAXA_IMPOSTO = 10

preco = float(input("Valor bruto do produto: "))

preco_final = preco + (preco * TAXA_IMPOSTO / 100)

print(f"O preço final líquido do produto é R$ {preco_final:.2f}")
