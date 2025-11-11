"""
Faça um programa que peça uma string ao usuário e mostre na tela a quantidade
de caracteres.


Dica: use a função built-in len() e trate a string com o método strip().
"""


def tam(string):
    string_tratado = string.strip()

    cont = 0

    for _ in string_tratado:
        cont += 1

    return cont


string = input("Digite uma string: ").strip()
print(f"TAMANHO {string} >>> {len(string)}")
print(f"TAMANHO {string} >>> {tam(string)}")
