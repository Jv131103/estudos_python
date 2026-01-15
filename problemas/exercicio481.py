"""
Faça um programa que:

    Use while True

    Mostre um menu:

        1 → somar dois números

        2 → subtrair dois números

        0 → sair

    O programa só termina quando o usuário escolher 0

Use break.
"""

from random import randint

while True:
    print("==" * 30)
    print("1. somar dois números")
    print("2. subtrair dois números")
    print("0. sair")
    print("==" * 30)
    menu = input("Escolha a opção conforme acima: ")
    print("--" * 30)

    n1 = randint(0, 1000)
    n2 = randint(0, 1000)

    match menu:
        case '1':
            print("Gerando números aleatórios...")
            print(f"{n1} + {n2} = {n1 + n2}")
        case '2':
            print("Gerando números aleatórios...")
            print(f"{n1} - {n2} = {n1 - n2}")
        case '0':
            print("Encerrando a execução!")
            break
        case _:
            print("Escolha as opções acima...")
