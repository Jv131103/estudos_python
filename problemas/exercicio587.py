"""
Faça um programa que:

    Tente converter um valor de texto para inteiro

    Capture o erro técnico

    Lance uma exceção de domínio usando raise ... from ...

    Mostre o traceback completo
"""

try:
    num = int(input("Número inteiro: "))
except ValueError as ve:
    raise TypeError("Tipo inválido para num") from ve
else:
    print(num)
