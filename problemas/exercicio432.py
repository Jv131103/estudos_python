"""
Faça um programa que:

    . Leia dois números

Verifique:

    . se o primeiro é múltiplo do segundo

Dica: use o operador % junto com ==.
"""
n1 = int(input("N1: "))
n2 = int(input("N2: "))

primeiro_eh_multiplo_do_segundo = n1 % n2 == 0

print(f"O primeiro é múltiplo do segundo? {primeiro_eh_multiplo_do_segundo}")
