"""
Elementos em comum (interseção)

Faça um programa que:

    Leia duas listas de números

Descubra:

    quais elementos aparecem nas duas listas

    quais aparecem somente na primeira

Mostre os resultados
"""

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

interseccao = list(set(l1) & set(l2))
print(f"Está nas duas listas: {interseccao}")

somente_na_primeira = list(set(l1) - set(l2))
print(f"Está apenas na primeira: {somente_na_primeira}")
