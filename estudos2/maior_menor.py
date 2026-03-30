def maior_de3(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        maior = n1
    elif n2 > n1 and n2 > n3:
        maior = n2
    else:
        maior = n3
    return maior


def menor_de3(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        menor = n1
    elif n2 < n1 and n2 < n3:
        menor = n2
    else:
        menor = n3
    return menor


print(maior_de3(1, 2, 3))
print(maior_de3(1, 3, 2))
print(maior_de3(2, 1, 3))
print(maior_de3(2, 3, 1))
print(maior_de3(3, 2, 1))
print(maior_de3(3, 1, 2))
print()
print(menor_de3(1, 2, 3))
print(menor_de3(1, 3, 2))
print(menor_de3(2, 1, 3))
print(menor_de3(2, 3, 1))
print(menor_de3(3, 2, 1))
print(menor_de3(3, 1, 2))
