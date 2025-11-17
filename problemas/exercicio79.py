"""Escreva um programa que multiplique todos os elementos de uma lista."""

lista = []

while True:
    try:
        n = int(input("Digite um número: [0 - SAIR DO PROGRAMA] "))
        if n == 0:
            break
        lista.append(n)
    except ValueError:
        print("Digite apenas números")
        continue


multiplicar = 1
for i in lista:
    multiplicar *= i

print(f"A multiplicação é igual a: {multiplicar}")
