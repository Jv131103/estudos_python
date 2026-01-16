"""
Faça um programa que:

    Use dois for

Imprima uma tabela de multiplicação de 1 a 5
"""


def multiplicar_de(inicio=0, fim=10):
    for valor in range(inicio, fim + 1):
        print("==" * 30)
        for item in range(11):
            print(f"{valor} * {item} = {valor * item}")


multiplicar_de(1, 5)
print()
multiplicar_de(5, 6)
print()
multiplicar_de(5, 5)
