"""
Leia a, b, c e mostre o resultado de:

    a + b * c

    (a + b) * c

    a < b and b < c or a == c
    Depois refaça a última usando parênteses para ficar cristalino.
"""
a = int(input())
b = int(input())
c = int(input())

print(a + b * c)
print((a + b) * c)
print(a < b and b < c or a == c)
print((a < b and b < c) or a == c)
