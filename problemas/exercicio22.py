"""
Faça um programa que solicite três números inteiros do usuário e imprima a
soma destes.
"""

# modelo 1
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
n1 += n2 + n3  # usando propriedade associativa
print(n1)

# modelo 2
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
soma = n1 + n2 + n3
print(soma)

# modelo 3
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
while True:
    soma = n1 ^ n2 ^ n3                          # XOR = soma sem carry
    carry = ((n1 & n2) | (n2 & n3) | (n3 & n1)) << 1  # AND/OR + shift = carry
    n1, n2, n3 = soma, carry, 0                  # novo ciclo: soma + carry
    if n2 == 0:                                  # quando não houver mais carry
        print(n1)
        break

# modelo 4
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
print(sum((n1, n2, n3)))

# modelo 5
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

soma = n1
while n2 > 0:
    soma += 1
    n2 -= 1
while n3 > 0:
    soma += 1
    n3 -= 1
print(soma)
