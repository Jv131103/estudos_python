"""
Faça um programa que:

    Leia um nome

Remova espaços das pontas (strip)

    Compare ignorando maiúsculas/minúsculas (lower)

Se for "renato", imprima "OK", senão "NÃO".
"""

nome = input("Nome: ").strip().lower()

if nome == "renato":
    print("OK")
else:
    print("NÃO")
