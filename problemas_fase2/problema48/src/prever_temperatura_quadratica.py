def prever_temperatura_quadratica(cpu, a, peso, bias):
    return a * cpu**2 + peso * cpu + bias


if __name__ == "__main__":
    assert prever_temperatura_quadratica(
        50, 0, 0.2, 30
    ) == 40

    assert prever_temperatura_quadratica(
        50, 0.001, 0.2, 30
    ) == 42.5

    assert prever_temperatura_quadratica(
        100, 0.001, 0.2, 30
    ) == 60
