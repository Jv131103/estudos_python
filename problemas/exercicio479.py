"""
Faça um programa que:

    Leia um número

    Continue pedindo enquanto o número for negativo

    Ao final, imprima o número válido
"""

num = int(input())
ultimo = None
while num < 0:
    ultimo = num
    num = int(input())

print(f"Número válido: {num}")
print(f"último após execução: {ultimo}")
