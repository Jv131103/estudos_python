"""
Escreva um programa que receba três números do usuário e mostre na tela o maior
número digitado.
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n1 > n3:
    print("n1 é maior")
elif n2 > n1 and n2 > n3:
    print("n2 é maior")
else:
    print("n3 é maior")
