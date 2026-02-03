"""
Peça um ângulo em graus e mostre:

    seno

    cosseno

    tangente

Dica: use math.radians() antes de calcular.
"""

import math

while True:
    try:
        angulo = float(input("Ângulo em graus (0 sai): "))

        if angulo == 0:
            break

        rad = math.radians(angulo)

        seno = math.sin(rad)
        cosseno = math.cos(rad)

        print(f"Seno: {seno}")
        print(f"Cosseno: {cosseno}")

        if abs(cosseno) < 1e-10:
            print("Tangente indefinida para esse ângulo.")
        else:
            tangente = math.tan(rad)
            print(f"Tangente: {tangente}")

    except ValueError:
        print("Digite um número válido.")
