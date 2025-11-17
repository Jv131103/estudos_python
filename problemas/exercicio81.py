"""
Considere a lista abaixo e faça um programa que some todos os seus elementos.
Tente implementar ao menos duas soluções.


    lista = [10, 2, 40, 50, -2, 3, 100, 21, 33, 29, 123, 234, 32, 88, 90, 23]

"""
# Versão 1
lista = [10, 2, 40, 50, -2, 3, 100, 21, 33, 29, 123, 234, 32, 88, 90, 23]
print(sum(lista))

print()

# Versão 2
soma = 0
for valor in lista:
    soma += valor
print(soma)
