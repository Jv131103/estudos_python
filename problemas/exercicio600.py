"""
Faça um programa que:

    Peça um número ao usuário

    Mostre:

        a raiz quadrada

        o valor elevado ao cubo
        (use math.sqrt() e math.pow())
"""

import math

while True:
    try:
        num = float(input("Número (0 sai do programa): "))

        if num == 0:
            break

        if num < 0:
            print("Não é possível calcular raiz quadrada de número negativo.")
            continue

        raiz = math.sqrt(num)
        potencia = math.pow(num, 3)

        print(f"Raiz quadrada: {raiz}")
        print(f"Valor ao cubo: {potencia}")

    except ValueError:
        print("Digite um número válido.")
