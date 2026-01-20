"""
Faça um programa que:

    Receba uma lista de números

    Use apenas slicing para:

        obter os 3 primeiros elementos

        obter os 3 últimos elementos

        obter a lista sem o primeiro e o último elemento

    Mostre os resultados

Não use loops nem índices individuais (lista[i]).
"""

lista = ["João", "Maria", "Santana", "Luzia", "Núbia", "Lais", "Duque"]

primeiros3 = lista[0:3]
print(primeiros3)

ultimos3 = lista[-3:]
print(ultimos3)

sem_primeiro_e_ultimo = lista[1:-1]
print(sem_primeiro_e_ultimo)
