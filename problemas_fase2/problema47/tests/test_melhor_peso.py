import pytest
from src.encontrar_melhor_peso import encontrar_melhor_peso


@pytest.mark.parametrize(
    "candidatos, bias, esperado",
    [
        ([0.0, 0.1, 0.2, 0.3, 0.4], 30, (0.2, 0.0)),
        ([0.0, 0.1], 30, (0.1, 37.5)),
        ([0.1], 30, (0.1, 37.5))
    ]
)
def test_melhor_peso(candidatos, bias, esperado):
    dados = [
        (0, 30),
        (25, 35),
        (50, 40),
        (75, 45),
        (100, 50)
    ]

    assert encontrar_melhor_peso(dados, candidatos, bias) == esperado
