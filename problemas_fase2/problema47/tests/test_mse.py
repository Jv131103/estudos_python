import pytest
from src.mse import calcular_mse


@pytest.mark.parametrize(
    "peso, bias, esperado",
    [
        (0.1, 30, 37.5),
        (0.2, 30, 0)
    ]
)
def test_calcular_mse(peso, bias, esperado):
    dados = [
        (0, 30),
        (25, 35),
        (50, 40),
        (75, 45),
        (100, 50)
    ]

    assert calcular_mse(dados, peso, bias) == esperado
