"""
Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir.

    [1, 3, 5, 7, 9]
"""

# 1
lista1 = [impares for impares in range(1, 10, 2)]
print(lista1)

# 2
lista2 = [impares for impares in range(1, 10) if impares % 2 != 0]
print(lista2)

# 3
lista3 = [2 * impares + 1 for impares in range(5)]
print(lista3)
