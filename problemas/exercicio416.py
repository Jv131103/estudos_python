"""
Faça um programa que:

    Peça o preço de um produto

    Peça a quantidade comprada

    Calcule o total

    Mostre o valor final formatado

Dica: use conversão de tipo corretamente.
"""

preco = float(input("Preço: "))
qtd = int(input("Quantidade: "))

total = preco * qtd
print(f"Total: R$ {total:.2f}")
