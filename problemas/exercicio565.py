"""
Faça um programa que:

    Receba uma string com letras e números misturados

    Use regex para encontrar todos os números inteiros presentes no texto

    Mostre a lista de números encontrados

Exemplo conceitual:

    "abc123def45x9" → ["123", "45", "9"]
"""

import re


def find_numbers(string):
    return re.findall(r"-?\d+", string)


print(find_numbers("abc123def45x9"))
