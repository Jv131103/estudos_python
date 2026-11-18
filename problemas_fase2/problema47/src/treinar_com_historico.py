try:
    from atualizar_peso import atualizar_peso
    from mse import calcular_mse
except (ImportError, ImportWarning):
    from src.atualizar_peso import atualizar_peso
    from src.mse import calcular_mse


def treinar_com_historico(
    dados,
    peso_inicial,
    bias,
    learning_rate,
    epocas
):
    historico = [calcular_mse(dados, peso_inicial, bias)]
    peso = peso_inicial
    for _ in range(epocas):
        peso = atualizar_peso(dados, peso, bias, learning_rate)
        historico.append(calcular_mse(dados, peso, bias))

    return peso, historico


if __name__ == "__main__":
    dados = [
        (0, 30),
        (25, 35),
        (50, 40),
        (75, 45),
        (100, 50)
    ]

    peso_final, historico = treinar_com_historico(
        dados,
        peso_inicial=0.1,
        bias=30,
        learning_rate=0.0001,
        epocas=3
    )

    print(peso_final)
    # 0.1984375

    print(historico)
    # [37.5, 2.34375, 0.146484375, 0.0091552734375]
