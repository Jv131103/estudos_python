"""
Faça um programa que pergunte o preço de 3 produtos e informe qual o produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato
"""

preco1 = float(input("Preco do produto 1: "))
preco2 = float(input("Preco do produto 2: "))
preco3 = float(input("Preco do produto 3: "))

if preco1 < preco2 and preco1 < preco3:
    print("A melhor opção é o produto 1")
elif preco2 < preco1 and preco2 < preco3:
    print("A melhor opção é o produto 2")
else:
    print("A melhor opção é o produto 3")
