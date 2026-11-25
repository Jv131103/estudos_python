try:
    from src.prever_temperatura_quadratica import prever_temperatura_quadratica
except (ImportError, ImportWarning):
    from prever_temperatura_quadratica import prever_temperatura_quadratica


def atualizar_peso_quadratico(
    dados, a, peso, bias, learning_rate
):
    soma = 0

    for cpu, temperatura_real in dados:
        previsao = prever_temperatura_quadratica(
            cpu, a, peso, bias
        )

        contribuicao = 2 * cpu * (previsao - temperatura_real)

        soma += contribuicao

    gradiente = soma / len(dados)

    novo_peso = peso - learning_rate * gradiente

    return novo_peso


if __name__ == "__main__":
    dados = [
        (0, 30),
        (25, 35),
        (50, 40),
        (75, 45),
        (100, 50)
    ]

    novo_peso = atualizar_peso_quadratico(
        dados,
        a=0.001,
        peso=0.2,
        bias=30,
        learning_rate=0.000001
    )

    assert abs(novo_peso - 0.199375) < 1e-10
