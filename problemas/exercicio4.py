"""
Faça um programa que peça 2 números inteiros e um número float. Calcule e
mostre:

    . O produto do dobro do primeiro com a metade do segundo.
    . A soma do triplo do primeiro com o terceiro.
    . O terceiro elevado ao cubo.
"""

inteiro1 = int(input("Digite um número inteiro: "))
inteiro2 = int(input("Digite um outro número inteiro: "))
decimal = float(input("Digite um número decimal agora: "))

resultado = (inteiro1 * 2) * (inteiro2 / 2)
resultado2 = inteiro1 * 3 + decimal
resultado3 = decimal**2

print(f"O produto do dobro do primeiro com a metade do segundo: {resultado}")
print(f"A soma do triplo do primeiro com o terceiro: {resultado2}")
print(f"O terceiro elevado ao cubo: {resultado3}")
