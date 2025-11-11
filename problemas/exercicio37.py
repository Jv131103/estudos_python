"""
Escreva um programa que verifique se um determinado número digitado pelo
usuário é nulo, positivo ou negativo.
"""

n = int(input("Número: "))

if n == 0:
    print("Nulo")
elif n > 0:
    print("Positivo")
else:
    print("Negativo")
