def gerar_ate(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()


padroes = list(range(1, 11))
for valor in padroes:
    gerar_ate(valor)
