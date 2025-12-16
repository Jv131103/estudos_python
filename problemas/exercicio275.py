def retornar_pares_e_impares(lista):
    pares = []
    impares = []

    for itens in lista:
        if itens % 2 == 0:
            pares.append(itens)
        else:
            impares.append(itens)

    return {
        "pares": pares,
        "impares": impares
    }


numeros = [1, 2, 3, 4, 5, 6]
dados = retornar_pares_e_impares(numeros)
print(dados["pares"])
print(dados["impares"])
