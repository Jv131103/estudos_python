"""
Faça um programa que leia 5 números e informe o maior número
"""

contador = 0
maior = float("-inf")  # - infinito. Uma propriedade específica do Python

while contador < 5:
    try:
        numero = float(input("Digite um número: "))
        if numero > maior:
            maior = numero
    except ValueError:
        print("Digite apenas números")
        continue
    contador += 1


print(f"Maior: {maior}")
