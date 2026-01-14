"""
Faça um programa que:

    Some um inteiro com um float

Mostre o resultado e o tipo do resultado
"""

tipo_int = int(input("Inteiro: "))
tipo_float = float(input("Decimal: ").replace(",", "."))

soma = tipo_int + tipo_float

print(f"{tipo_int} + {tipo_float} = {soma}")
print(f"Tipo do resultado: {type(soma)}")
