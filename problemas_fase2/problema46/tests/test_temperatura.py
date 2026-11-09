import math

import pytest
from src.temperatura import controlar_temperatura


@pytest.mark.parametrize(
    "temp, esperado",
    [
        (20, "Temperatura normal"),
        (25, "Ligar ventilação"),
        (34, "Ligar ventilação"),
        (35, "ALERTA: temperatura crítica!"),
        (24.5, "Temperatura normal"),
        (25.5, "Ligar ventilação"),
        (34.9, "Ligar ventilação"),
        (35.1, "ALERTA: temperatura crítica!")
    ]
)
def test_controle_temperatura(temp, esperado):
    assert controlar_temperatura(temp) == esperado


@pytest.mark.parametrize(
    'tipo',
    [
        ("21"),
        (True),
        (False),
        (complex(90)),
    ]
)
def test_raises_controle_temperatura(tipo):
    with pytest.raises(ValueError, match="Tipo inválido para temperatura. Só é aceito INT ou FLOAT"):
        controlar_temperatura(tipo)


@pytest.mark.parametrize(
    'tipo',
    [
        float("nan"),
        float("inf"),
        float("-inf"),
        math.nan,
    ]
)
def test_raises_controle_temperatura2(tipo):
    with pytest.raises(ValueError, match="Temperatura deve ser um número finito"):
        controlar_temperatura(tipo)
