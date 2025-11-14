"""
Escreva um programa que peça 5 números inteiros não-nulos ao usuário e
mostre na tela o quadrado de cada número digitado.
"""

lista = []

for i in range(1, 6):
    numero = int(input(f"Valor {i}: "))
    lista.append(numero)

for numero in lista:
    print(f"{numero}**2 = {numero**2}")
