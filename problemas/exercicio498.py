"""
Crie uma função ordenar_por_tamanho(lista) que receba uma lista de strings e
retorne a lista ordenada pelo tamanho das palavras, usando lambda.
"""


def ordenar_por_tamanho(lista, reverse=True):
    return sorted(lista, key=lambda x: len(x), reverse=reverse)


print(ordenar_por_tamanho(["arroz", "feijão", "Batata"]))
print(ordenar_por_tamanho(["arroz", "feijão", "Batata"], False))
