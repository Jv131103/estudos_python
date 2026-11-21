import pytest
# Ajuste o import se o seu módulo tiver outro nome ou estiver em src/.
from src.prever_temperatura_quadratica import prever_temperatura_quadratica


@pytest.mark.parametrize(
    "cpu, a, peso, bias, esperado",
    [
        (50, 0, 0.2, 30, 40),
        (50, 0.001, 0.2, 30, 42.5),
        (100, 0.001, 0.2, 30, 60),
    ],
)
def test_exemplos_do_enunciado(cpu, a, peso, bias, esperado):
    assert prever_temperatura_quadratica(cpu, a, peso, bias) == pytest.approx(esperado)


# ---------- Valores calculados à mão ----------

@pytest.mark.parametrize(
    "cpu, a, peso, bias, esperado",
    [
        (0, 0.001, 0.2, 30, 30),
        (25, 0.001, 0.2, 30, 35.625),
        (75, 0.001, 0.2, 30, 50.625),
        (0.5, 2, 3, 1, 3.0),
        (-2, 1, 2, 3, 3),
        (10, -0.01, 0.5, 20, 24),
        (3, 1, 1, 1, 13),
    ],
)
def test_valores_calculados_a_mao(cpu, a, peso, bias, esperado):
    assert prever_temperatura_quadratica(cpu, a, peso, bias) == pytest.approx(esperado)
