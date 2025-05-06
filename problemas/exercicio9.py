"""
Faça um programa que peça uma nota, entre 0 e 10. Mostre uma mensagem
caso o valor sejá inválido e continue pedindo até que o usuário informe
um valor válido.
"""

while True:
    try:
        nota = int(input("Digite uma nota de 0 até 10: "))
        if 0 <= nota <= 10:
            print(f"NOTA: {nota}")
            break
        else:
            print("Nota inválida, digite de 0 até 10!")
    except ValueError:
        print("Inválido, digite apenas números")
