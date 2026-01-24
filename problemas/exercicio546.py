"""
Faça um programa que:

    . Crie uma lista de tuplas no formato:

        (nome, idade)

    . Ordene a lista:

        1. pelo nome

        2. pela idade

    . Mostre o resultado das duas ordenações

    Exemplo conceitual:

        [("Ana", 20), ("João", 18), ("Bia", 25)]

    DICAS

        Use sorted

        Para ordenar por idade, use key

        Lembre: sorted retorna lista, não tupla
"""


dados = [("Ana", 20), ("João", 18), ("Bia", 25)]

ordenar_por_nome = sorted(dados)
print(ordenar_por_nome)

ordenar_por_idade = sorted(dados, key=lambda i: i[1])
print(ordenar_por_idade)
