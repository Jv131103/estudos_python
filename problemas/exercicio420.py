"""
Faça um programa que:

    Leia um número inteiro

Mostre:

    o quadrado (n²)

    o cubo (n³)

Depois diga se o número é par ou ímpar

Dica: use % 2.
"""

n = int(input())

quadrado = n**2
cubo = n**3

print(f"Quadrado de {n}: {quadrado}")
print(f"Cubo de {n}: {cubo}")

# Sem if por enquanto
is_par = n % 2 == 0
print(f"É PAR? {is_par}")
print(f"É ÍMPAR? {not is_par}")
