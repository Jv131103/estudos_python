def normalizar_cpu(dados):
    lista = []

    for cpu, temperatura_real in dados:
        cpu_normalizada = cpu / 100
        tupla = (cpu_normalizada, temperatura_real)
        lista.append(tupla)

    return lista


if __name__ == "__main__":
    from mse import calcular_mse_quadratico
    from treinar_modelo_quadratico import treinar_modelo_quadratico

    dados = [
        (0, 30),
        (25, 35),
        (50, 40),
        (75, 45),
        (100, 50)
    ]

    resultado = normalizar_cpu(dados)

    assert resultado == [
        (0.0, 30),
        (0.25, 35),
        (0.5, 40),
        (0.75, 45),
        (1.0, 50)
    ]

    a, peso, bias, historico = treinar_modelo_quadratico(
        resultado,
        a_inicial=0,
        peso_inicial=0,
        bias_inicial=30,
        learning_rate=0.1,
        epocas=100
    )
    for epoca, mse in enumerate(historico):
        print(f"Época {epoca}: MSE = {mse}")

    dados_teste = [
        (10, 33),
        (40, 37),
        (80, 47)
    ]
    resultado = normalizar_cpu(dados_teste)
    mse_teste = calcular_mse_quadratico(resultado, a, peso, bias)
    print(f"MSE de teste: {mse_teste}")
