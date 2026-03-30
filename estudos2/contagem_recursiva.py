def contar(inicio, fim, intervalo=1):
    if not intervalo:
        intervalo = 1

    print(inicio)
    if inicio == fim:
        return inicio
    elif inicio > fim:
        return contar(abs(inicio - intervalo), fim, intervalo)
    else:
        return contar(abs(inicio + intervalo), fim, intervalo)


'''contar(1, 10)
print()
contar(10, 1)
print()'''
contar(0, 30, 3)
print()
contar(10, 0, 2)
