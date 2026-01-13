"""
Faça um programa que:

    Leia três números

Mostre:

    o maior

    o menor

    a soma deles

Use max(), min() e sum().
"""
n1, n2, n3 = input().split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
soma = sum([n1, n2, n3])

print(f"Min: {menor}")
print(f"Max: {maior}")
print(f"Sum: {soma}")
