try:
    from calcular_erro import calcular_erro
    from prever_temperatura import prever_temperatura
except (ImportError, ImportWarning):
    from src.calcular_erro import calcular_erro
    from src.prever_temperatura import prever_temperatura


def calcular_mse(dados, peso, bias):
    if not dados:
        raise ValueError("Não existem dados para calcular o MSE")

    soma = 0
    for cpu, temperatura_real in dados:
        previsao = prever_temperatura(cpu, peso, bias)
        _, erro_quadratico = calcular_erro(temperatura_real, previsao)
        soma += erro_quadratico

    return soma / len(dados)


if __name__ == "__main__":
    dados = [
        (0, 30),
        (25, 35),
        (50, 40),
        (75, 45),
        (100, 50)
    ]

    testes = [
        (0.1, 30, 37.5),
        (0.2, 30, 0)
    ]

    for peso, bias, esperado in testes:
        retorno = calcular_mse(dados, peso, bias)
        print(retorno)
        assert retorno == esperado
