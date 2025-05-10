"""
Faça um programa que: Dada uma lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e um número
inteiro, imoprima a tabuada desse numero
"""

numero = int(input("Digite um numero: "))

numeros_tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("x===============x")
print(f"| TABUADA -> {numero:02d} |")
print("x===============x")
for i in numeros_tabuada:
    print(f"| {numero:02d} x {i:02d} = {numero * i:03d} |")
    print("x---------------x")
