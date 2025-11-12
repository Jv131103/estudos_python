"""
Faça um programa que imprima na tela de 1 até um número digitado pelo usuário.
"""

limite = int(input("Limite: "))
cont = 1
while cont <= limite:
    print(cont)
    cont += 1

print()

for i in range(1, limite + 1):
    print(i)
