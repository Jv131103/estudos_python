"""
Faça um programa que peça 5 números de ponto flutuante do usuário e apresente no
final a média dos números digitados.
"""

# Modelo 1
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
n5 = float(input("Nota 5: "))
media = (n1 + n2 + n3 + n4 + n5) / 5
print(f"Média: {media:.1f}")

# modelo 2
soma = 0
qtd = 0
while True:
    opcao = input("Digite um número [ENTER PARA SAIR]: ").replace(",", ".").strip()
    if opcao == "":
        break
    numero = float(opcao)
    soma += numero
    qtd += 1

media = soma / qtd
print(f"Média: {media:.1f}")
