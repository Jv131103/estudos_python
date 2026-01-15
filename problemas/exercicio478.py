"""
Faça um programa que:

    Leia números inteiros

    Some os valores

    Pare quando o usuário digitar 0

    Mostre a soma final

Use while com condição dinâmica.
"""

soma = 0

while True:

    try:
        num = int(input())

        if num == 0:
            break

        soma += num
    except ValueError:
        print("Digite apenas números inteiros")

print(f"A soma final é {soma}")
