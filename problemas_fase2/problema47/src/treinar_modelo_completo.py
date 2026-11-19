try:
    from atualizar_bias import atualizar_bias
    from atualizar_peso import atualizar_peso
    from mse import calcular_mse
except (ImportError, ImportWarning):
    from src.atualizar_bias import atualizar_bias
    from src.atualizar_peso import atualizar_peso
    from src.mse import calcular_mse


def treinar_modelo_completo(
    dados,
    peso_inicial,
    bias_inicial,
    learning_rate,
    epocas
):
    historico = [calcular_mse(dados, peso_inicial, bias_inicial)]
    peso = peso_inicial
    bias = bias_inicial
    for _ in range(epocas):
        novo_peso = atualizar_peso(
            dados, peso, bias, learning_rate
        )

        novo_bias = atualizar_bias(
            dados, peso, bias, learning_rate
        )

        peso = novo_peso
        bias = novo_bias

        historico.append(
            calcular_mse(dados, peso, bias)
        )

    return peso, bias, historico


if __name__ == "__main__":
    dados = [
        (0, 30),
        (25, 35),
        (50, 40),
        (75, 45),
        (100, 50)
    ]

    peso, bias, historico = treinar_modelo_completo(
        dados,
        peso_inicial=0.1,
        bias_inicial=30,
        learning_rate=0.0001,
        epocas=1
    )

    assert abs(peso - 0.175) < 1e-10
    assert abs(bias - 30.001) < 1e-10

    assert len(historico) == 2
    assert historico[1] < historico[0]
