"""
Faça um programa que:

    Leia uma lista de strings

    Use enumerate

    Mostre índice e valor formatados

Exemplo:

    0 - Ana
    1 - João

Objetivo: enumerate.
"""

nomes = ["João", "Ana", "Maria", "Junipher", "Isaias", "Lucas", "Renato"]
for idx, nome in enumerate(nomes):
    print(f"{idx} - {nome}")
