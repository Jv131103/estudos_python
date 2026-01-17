"""
Faça um programa que:

    Leia uma lista de números

    Calcule a soma sem usar sum()

    Mostre o resultado

Objetivo: loop + acumulador.
"""
opc = "s"

lista = []
while opc.lower() == 's':
    try:
        num = int(input("Digite um valor inteiro: "))
    except ValueError:
        print("Digite apenas números")
        continue

    lista.append(num)

    opc = input("Continuar? [s/n] ")


soma = 0
for dados in lista:
    soma += dados

print(f"A soma é {soma}")
