"""
Considere a lista abaixo e escreva um programa que multiplique todos os seus
elementos.

    lista = [5,4,3,2,1]
"""
mult = 1
lista = [5, 4, 3, 2, 1]

for valor in lista:
    mult *= valor

print(f"Resultado: {mult}")
