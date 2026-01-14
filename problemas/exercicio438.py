"""
Faça um programa que:

    Crie duas listas iguais

Compare:

    com ==

    com is

Mostre os dois resultados
"""

lista1 = list(range(10))
lista2 = list(range(10))

print(lista1 == lista2)  # compara valor / conteúdo
print(lista1 is lista2)  # compara identidade / memória
