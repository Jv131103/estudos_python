try:
    from mse import calcular_mse
except (ImportError, ImportWarning):
    from src.mse import calcular_mse


def encontrar_melhor_peso(dados, candidatos, bias):
    menor_mse = float("inf")  # Também poderia inicializar menor_mse usando o MSE do primeiro candidato.
    melhor_peso = None
    for peso in candidatos:
        mse_retornado = calcular_mse(dados, peso, bias)
        if mse_retornado <= menor_mse:
            menor_mse = mse_retornado
            melhor_peso = peso

    return melhor_peso, menor_mse


if __name__ == "__main__":
    dados = [
        (0, 30),
        (25, 35),
        (50, 40),
        (75, 45),
        (100, 50)
    ]

    candidatos = [0.0, 0.1, 0.2, 0.3, 0.4]

    resultado = encontrar_melhor_peso(dados, candidatos, 30)

    print(resultado)
    assert resultado == (0.2, 0.0)
