"""
Faça um programa que:

    Leia uma string

    Verifique se ela representa um CPF no formato:

        NNN.NNN.NNN-NN

    . Mostre se o formato é válido ou não

    (não valide dígitos, apenas o formato)
"""


import re


def is_cpf(digit_cpf):
    pattern = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"

    if re.search(pattern, digit_cpf):
        return True
    return False


print(is_cpf("123.456.789-01"))
print(is_cpf("123x456y789-01"))
print(is_cpf("12345678901"))
