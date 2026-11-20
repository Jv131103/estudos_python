def calcular_acuracia(dados, memoria, percent=False):
    acertos = 0

    for numero, resposta_real in dados:
        previsao = memoria.get(numero, 0)

        if previsao == resposta_real:
            acertos += 1

    acuracia = acertos / len(dados) if not percent else acertos / len(dados) * 100

    return acuracia


dados_treino = [
    (1, 1),
    (2, 0),
    (3, 1),
    (4, 0)
]

dados_teste = [
    (5, 1),
    (6, 0),
    (7, 1),
    (8, 0)
]

memoria = dict(dados_treino)
assert calcular_acuracia(dados_treino, memoria) == 1.0

assert calcular_acuracia(dados_teste, memoria) == 0.5
