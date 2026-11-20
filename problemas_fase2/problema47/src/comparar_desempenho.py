try:
    from mse import calcular_mse
except (ImportError, ImportWarning):
    from src.mse import calcular_mse


def comparar_desempenho(
    dados_treino,
    dados_teste,
    peso,
    bias
):
    mse_teste = calcular_mse(dados_teste, peso, bias)
    mse_treino = calcular_mse(dados_treino, peso, bias)

    return mse_treino, mse_teste


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

    mse_treino, mse_teste = comparar_desempenho(
        dados_treino,
        dados_teste,
        peso=0.2,
        bias=30
    )

    # Modelo 1
    mse_treino, mse_teste = comparar_desempenho(
        dados_treino, dados_teste, 0.2, 30
    )

    assert abs(mse_treino - 0) < 1e-10
    assert abs(mse_teste - 0) < 1e-10

    # Modelo 2
    mse_treino, mse_teste = comparar_desempenho(
        dados_treino, dados_teste, 0.1, 30
    )

    assert abs(mse_treino - 37.5) < 1e-10
    assert abs(mse_teste - 27) < 1e-10
