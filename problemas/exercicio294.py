def len_multiples(lista, number):
    return len([valor for valor in lista if valor % number == 0])


lista = [4, 5, 8, 10, 16]
print(len_multiples(lista, 4))
print(len_multiples(lista, 2))
