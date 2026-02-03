"""
Peça um número decimal ao usuário e mostre:

    arredondado para cima (ceil)

    arredondado para baixo (floor)

    valor absoluto (fabs)

Exemplo:

    Digite um número: -3.7
    Ceil: -3
    Floor: -4
    Absoluto: 3.7
"""

import math

while True:
    try:
        num = float(input("Número: [0 sai do programa] "))
        if num == 0:
            break

        ceil = math.ceil(num)
        floor = math.floor(num)
        absoluto = math.fabs(num)

        print(f"Ceil: {ceil}")
        print(f"Floor: {floor}")
        print(f"Absoluto: {absoluto}")
    except ValueError:
        print("Número precisa ser do tipo numérico")
