"""
Faça um programa que solicite um número inteiro e mostre o seu valor absoluto.


Dica: use a função built-in abs().
"""

def absolute(n):
    if n < 0:
        return -(n)
    return n


num = int(input('Digite um número inteiro: '))
print(absolute(num))
print(abs(num))
