"""
Faça um programa que receba uma string, com um número de ponto flutuante,
e imprima qual a parte dele que não é inteira
"""

# Versão melhor
from decimal import Decimal

numero = Decimal(input("Digite um número: ").replace(",", "."))
resposta = numero - int(numero)
print(f"Casa decimal: {resposta}")

# versão com string:
numero = input("Digite um número: ").replace(",", ".").split(".")
print(numero[1])
