try:
    from prever_temperatura import prever_temperatura
except (ImportError, ImportWarning):
    from src.prever_temperatura import prever_temperatura


def atualizar_bias(dados, peso, bias, learning_rate):
    soma = 0
    for cpu, temperatura_real in dados:
        previsao = prever_temperatura(cpu, peso, bias)
        contribuicao = 2 * (previsao - temperatura_real)
        soma += contribuicao

    gradiente = soma / len(dados)
    novo_bias = bias - learning_rate * gradiente
    return novo_bias


if __name__ == "__main__":
    dados = [
        (0, 30),
        (25, 35),
        (50, 40),
        (75, 45),
        (100, 50)
    ]

    novo_bias = atualizar_bias(
        dados,
        peso=0.1,
        bias=30,
        learning_rate=0.0001
    )

    assert abs(novo_bias - 30.001) < 1e-10
