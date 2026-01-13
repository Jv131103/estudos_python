"""
Faça um programa que:

    Peça o nome do produto

    Peça o preço

    Peça a quantidade

    Calcule o total

Mostre uma saída organizada, por exemplo:

    Produto: Camisa
    Preço unitário: R$ 49.90
    Quantidade: 3
    Total a pagar: R$ 149.70

Use f-string e formatação numérica.
"""
nome = input("Nome: ")
preco = float(input("Preço: "))
qtd = int(input("Quantidade: "))

total = preco * qtd

print(f"Produto: {nome}")
print(f"Preço: {preco:.2f}")
print(f"Quantidade: {qtd}")
print(f"Total: {total}")
