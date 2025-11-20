lista = [valor**2 if valor % 2 == 0 else round(valor**(1 / 2), 1) for valor in range(1, 51)]
print(lista)
