def agrupar_por_criterio(lista):
    dados = {
        "menores_que_10": [],
        "maiores_ou_iguais_10": []
    }

    for numero in lista:
        if numero < 10:
            dados["menores_que_10"].append(numero)
        else:
            dados["maiores_ou_iguais_10"].append(numero)

    return dados


numeros = [3, 8, 12, 5, 7, 10]
saida = agrupar_por_criterio(numeros)
print(saida)
