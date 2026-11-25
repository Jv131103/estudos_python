try:
    from atualizar_a import atualizar_a
    from atualizar_bias_quadratico import atualizar_bias_quadratico
    from atualizar_peso_quadratico import atualizar_peso_quadratico
    from mse import calcular_mse_quadratico
except (ImportError, ImportWarning):
    from src.atualizar_a import atualizar_a
    from src.atualizar_bias_quadratico import atualizar_bias_quadratico
    from src.atualizar_peso_quadratico import atualizar_peso_quadratico
    from src.mse import calcular_mse_quadratico


def treinar_modelo_quadratico(dados, a_inicial, peso_inicial, bias_inicial, learning_rate, epocas):
    a = a_inicial
    peso = peso_inicial
    bias = bias_inicial

    historico = [calcular_mse_quadratico(dados, a, peso, bias)]

    for i in range(epocas):
        novo_a = atualizar_a(dados, a, peso, bias, learning_rate)
        novo_peso = atualizar_peso_quadratico(dados, a, peso, bias, learning_rate)
        novo_bias = atualizar_bias_quadratico(dados, a, peso, bias, learning_rate)
        a = novo_a
        peso = novo_peso
        bias = novo_bias
        historico.append(calcular_mse_quadratico(dados, a, peso, bias))

    return a, peso, bias, historico


if __name__ == "__main__":
    dados = [
        (0, 30),
        (25, 35),
        (50, 40),
        (75, 45),
        (100, 50)
    ]

    a, peso, bias, historico = treinar_modelo_quadratico(
        dados,
        a_inicial=0.001,
        peso_inicial=0.2,
        bias_inicial=30,
        learning_rate=0.00000001,
        epocas=1
    )

    assert abs(a - 0.000446875) < 1e-12
    assert abs(peso - 0.19999375) < 1e-12
    assert abs(bias - 29.999999925) < 1e-10

    assert len(historico) == 2
    assert abs(historico[0] - 27.65625) < 1e-10
    assert historico[1] < historico[0]
