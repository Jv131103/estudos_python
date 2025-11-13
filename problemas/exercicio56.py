"""
Escreva um programa que peça números reais (float) do usuário indefinidamente.
Caso os números digitados não estejam situados entre 0 e 10 o programa deverá
ser finalizado, mostrando a soma e a quantidade de números digitados.
"""

soma = 0
numeros_digitados = 0

while True:
    valor = float(input("Número de 0 a 10: "))
    if valor < 0 or valor > 10:
        print("Encerrando o programa...")
        break
    soma += valor
    numeros_digitados += 1

print(f"A soma final é {soma}")
print(f"Total de números digitados: {numeros_digitados}")
