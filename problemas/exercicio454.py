"""
Faça um programa que:

    Leia um valor qualquer (texto)

Mostre:

    o valor original

    o valor convertido para bool

Teste com: "0", "", "abc", " ".
"""

valor = input("Digite um valor qualquer: ")

valor_boolean = bool(valor)

print(f"Valor original: '{valor}' | Valor convertido em boolean: {valor_boolean}")
