def chamar_padrao(valor):
    cont = 0

    while cont < valor:
        print(valor, end="")
        cont += 1

    print()


padroes = list(range(21))
for valor in padroes:
    chamar_padrao(valor)
