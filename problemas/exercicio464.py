"""
Faça um programa que:

    Leia um número decimal

    Mostre sua fração exata usando as_integer_ratio()

Explique (comentário) por que 0.1 gera números grandes
"""

num = float(input())

fracao = num.as_integer_ratio()
print(fracao)
# 0.1 não pode ser representado exatamente em binário.
# O float armazena a aproximação binária mais próxima,
# que corresponde à fração:
# 3602879701896397 / 36028797018963968
# Por isso surgem números grandes.
