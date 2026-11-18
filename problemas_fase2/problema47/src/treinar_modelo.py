try:
    from atualizar_peso import atualizar_peso
except (ImportError, ImportWarning):
    from src.atualizar_peso import atualizar_peso


def treinar_modelo(
    dados,
    peso_inicial,
    bias,
    learning_rate,
    epocas
):
    peso = peso_inicial
    for _ in range(epocas):
        peso = atualizar_peso(dados, peso, bias, learning_rate)

    return peso


dados = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50)
]

assert abs(
    treinar_modelo(dados, 0.1, 30, 0.0001, 1) - 0.175
) < 1e-10

assert abs(
    treinar_modelo(dados, 0.1, 30, 0.0001, 2) - 0.19375
) < 1e-10

assert abs(
    treinar_modelo(dados, 0.1, 30, 0.0001, 3) - 0.1984375
) < 1e-10
