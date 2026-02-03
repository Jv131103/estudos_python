"""
Faça um programa que:

    Leia entradas do usuário

    Continue lendo enquanto a entrada não for vazia

    Use walrus para:

        ler a entrada

        testar a condição no while

    Imprima cada entrada lida

Exemplo conceitual:

    Digite algo: abc
    Digite algo: 123
    Digite algo:
    (loop termina)
"""


while (valor := input("Digite algo: ")) != "":
    print(valor)
