"""
Faça um programa que:

    . Leia um valor inicial

    . Leia um valor de desconto

    . Subtraia o desconto usando -=

    . Mostre o valor final
"""
valor = float(input("Valor inicial: "))
desconto = float(input("Valor de desconto: "))

valor -= desconto
print(f"Resultado: {valor}")
