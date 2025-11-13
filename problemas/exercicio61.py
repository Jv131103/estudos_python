"""
Escreva um programa que peça números inteiros positivos indefinidamente e
armazene-os em uma lista. O programa deverá ser encerrado caso o número
digitado seja negativo ou nulo. Ao final mostre na tela a quantidade números
pares e ímpares.
"""

lista_numeros = []

while True:
    n = int(input("N: "))
    if n <= 0:
        break
    lista_numeros.append(n)


qtd_pares = 0
qtd_impares = 0

for i in lista_numeros:
    if i % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1

print(f"Quantidade Pares: {qtd_pares}")
print(f"Quantidade Ímpares: {qtd_impares}")
