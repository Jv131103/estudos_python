"""
Leia uma string e:

    Use if texto: para verificar se está vazia

Mostre "Vazia" ou "Não vazia"
"""


def esta_vazio(texto):
    if texto:
        return "Não vazia"
    return "Vazia"


print(esta_vazio(""))
print(esta_vazio("SALVE"))
