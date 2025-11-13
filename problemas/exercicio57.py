"""
Escreva um programa que peça ao usuário 20 números reais e ao final mostre a
soma e a média dos números digitados.
"""

# VERSÃO 1
soma = 0
qtd_digitados = 0

while qtd_digitados < 20:
    try:
        numero = float(input("Digite um valor: "))
    except ValueError:
        print("DIGITE APENAS NÚMEROS...")
        continue

    soma += numero
    qtd_digitados += 1


media = soma / qtd_digitados
print(f"SOMA FINAL: {soma} | MÉDIA FINAL: {media}")

# VERSÃO 2
soma = 0

for i in range(20):
    try:
        numero = float(input("Digite um valor: "))
    except ValueError:
        print("DIGITE APENAS NÚMEROS...")
        continue

    soma += numero

media = soma / i
print(f"SOMA FINAL: {soma} | MÉDIA FINAL: {media}")
