# 1
lista_mutiplos_5 = [valor * 5 for valor in range(0, 21)]
print(lista_mutiplos_5)

# 2
lista_mutiplos_5 = [valor for valor in range(0, 101, 5)]
print(lista_mutiplos_5)

# 3
lista_mutiplos_5 = [valor for valor in range(101) if valor % 5 == 0]
print(lista_mutiplos_5)

print()

# 1
lista_multiplos_7 = [valor * 7 for valor in range(0, 143)]
print(lista_multiplos_7)

# 2
lista_multiplos_7 = [valor for valor in range(0, 995, 7)]
print(lista_multiplos_7)

# 3
lista_multiplos_7 = [numero for numero in range(1001) if numero % 7 == 0]
print(lista_multiplos_7)
