"""Escreva um programa que some todos os elementos de uma lista."""

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


soma = 0
for i in lista:
    soma += i

print(f"A soma é igual a: {soma}")
