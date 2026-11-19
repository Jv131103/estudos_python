try:
    from mse import calcular_mse
except (ImportError, ImportWarning):
    from src.mse import calcular_mse


def avaliar_modelo(dados_teste, peso, bias):
    erro_mse = calcular_mse(dados_teste, peso, bias)
    return erro_mse


if __name__ == "__main__":
    dados_treino = [
        (0, 30),
        (25, 35),
        (50, 40),
        (75, 45),
        (100, 50)
    ]

    dados_teste = [
        (10, 32),
        (40, 38),
        (80, 46)
    ]
    assert avaliar_modelo(dados_teste, 0.2, 30) < 1e-10
