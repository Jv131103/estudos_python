import pytest
from src.main import (rotacionar, rotacionar2, rotacionar3, rotacionar4,
                      rotacionar5, rotacionar6, rotacionar7)

FUNCOES = [
    rotacionar,
    rotacionar2,
    rotacionar3,
    rotacionar4,
    rotacionar5,
    rotacionar6,
    rotacionar7,
]


@pytest.mark.parametrize(
    "lista,k,esperado",
    [
        ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1, 2, 3, 4, 5], 3, [3, 4, 5, 1, 2]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ]
)
def test_rotacao(lista, k, esperado):

    for func in FUNCOES:
        resultado = func(lista.copy(), k)
        assert resultado == esperado
