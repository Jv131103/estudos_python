"""
Crie uma função aplicar_operacao(f, lista) que receba uma função e uma lista de
números, e retorne uma nova lista com a função aplicada a cada elemento.
"""


def dobrar(x):
    return x * 2


def aplicar_operacao(f, lista):
    nova = []
    for x in lista:
        nova.append(f(x))
    return nova


def aplicar_operacao_map(f, lista):
    return list(map(f, lista))


print(aplicar_operacao(dobrar, [1, 2, 3, 4]))
print(aplicar_operacao_map(dobrar, [1, 2, 3, 4]))
