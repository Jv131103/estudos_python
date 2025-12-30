def gerar_lista_alternada1(limite):
    resultado = []
    for valor in range(1, limite):
        resultado.append(-valor if valor % 2 == 0 else valor)
    return resultado


def gerar_lista_alternada2(limite):
    return [(-v if v % 2 == 0 else v) for v in range(1, limite)]


def gerar_lista_alternada3(limite):
    return [v * (-1) ** (v % 2 == 0) for v in range(1, limite)]


print(gerar_lista_alternada1(10))
print(gerar_lista_alternada2(10))
print(gerar_lista_alternada3(10))
