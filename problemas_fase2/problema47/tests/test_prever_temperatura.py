import pytest
from src.prever_temperatura import prever_temperatura


@pytest.mark.parametrize(
    "cpu, peso, bias, esperado",
    [
        (50, 0.1, 30, 35),
        (100, 0.1, 30, 40),
        (0, 0.1, 30, 30)
    ]
)
def test_deve_prever_temperatura(cpu, peso, bias, esperado):
    assert prever_temperatura(cpu, peso, bias) == esperado
