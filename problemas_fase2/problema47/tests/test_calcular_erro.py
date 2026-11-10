import pytest
from src.calcular_erro import calcular_erro


@pytest.mark.parametrize(
    "real, previsao, diferenca_esperada, erro_quadratico_esperado",
    [
        (40, 35, 5, 25),
        (50, 45, 5, 25),
        (95, 85, 10, 100),
        (35, 40, -5, 25),
        (40, 40, 0, 0)
    ]
)
def test_deve_passar_erros_quadraticos(real, previsao, diferenca_esperada, erro_quadratico_esperado):
    assert calcular_erro(real, previsao) == (diferenca_esperada, erro_quadratico_esperado)
