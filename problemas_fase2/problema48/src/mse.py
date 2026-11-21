try:
    from calcular_erro import calcular_erro
    from prever_temperatura_quadratica import prever_temperatura_quadratica
except (ImportError, ImportWarning):
    from src.calcular_erro import calcular_erro
    from src.prever_temperatura_quadratica import prever_temperatura_quadratica


def calcular_mse_quadratico(dados, a, peso, bias):
    if not dados:
        raise ValueError("Não existem dados para calcular o MSE")

    soma = 0
    for cpu, temperatura_real in dados:
        previsao = prever_temperatura_quadratica(cpu, a, peso, bias)
        _, erro = calcular_erro(temperatura_real, previsao)
        soma += erro

    return soma / len(dados)


if __name__ == "__main__":
    dados_treino = [
        (0, 30),
        (25, 35),
        (50, 40),
        (75, 45),
        (100, 50)
    ]

    assert abs(
        calcular_mse_quadratico(dados_treino, 0, 0.2, 30)
    ) < 1e-10

    assert abs(
        calcular_mse_quadratico(dados_treino, 0.001, 0.2, 30)
        - 27.65625
    ) < 1e-10
