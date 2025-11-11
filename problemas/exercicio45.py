"""
Determine se uma letra inserida pelo usuário é uma vogal ou consoante. Armazene
as vogais em uma lista e implemente sua solução. Desconsidere a possibilidade
de o usuário inserir números ou caracteres especiais.
"""


def letter_is(letter):
    # garante que é apenas uma letra e ignora maiúsculas
    letter = letter.lower().strip()

    if letter.isalpha():
        return "Vogal" if letter in "aeiou" else "Consoante"
    return "Não é uma letra"


print(letter_is('a'))
print(letter_is('b'))
print(letter_is('1'))
