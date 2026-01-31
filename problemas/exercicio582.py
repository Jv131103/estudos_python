"""
Faça um programa que:

    Leia um valor do usuário

    Tente converter esse valor para inteiro

Se a conversão falhar:

    use o valor 0 como fallback

    Mostre o valor final usado no programa

Exemplo conceitual:

    Entrada: "10"   → Resultado: 10
    Entrada: "abc"  → Resultado: 0
"""

try:
    entrada = int(input("Digite um número: "))
except ValueError:
    entrada = 0

print(f"Resultado: {entrada}")
