import pytest
from src.main import (eh_matriz_valida, transposta, transposta2, transposta3,
                      transposta4, transposta5, transposta6)

ALGORITMOS = [
    transposta,
    transposta2,
    transposta3,
    transposta4,
    transposta5,
    transposta6,
]


@pytest.mark.parametrize(
    "matriz, esperado",
    [
        ([[1]], True),
        ([[1, 2], [3, 4]], True),
        ([[1, 2, 3], [4, 5, 6]], True),
        ([[1, 2], [3]], False),
        ([[1], [2, 3]], False),
    ],
)
def test_eh_matriz_valida(matriz, esperado):
    assert eh_matriz_valida(matriz) == esperado


@pytest.mark.parametrize(
    "matriz, esperado",
    [
        (
            [[1]],
            [[1]],
        ),
        (
            [[1, 2]],
            [[1], [2]],
        ),
        (
            [[1], [2], [3]],
            [[1, 2, 3]],
        ),
        (
            [[1, 2], [3, 4]],
            [[1, 3], [2, 4]],
        ),
        (
            [[1, 2, 3], [4, 5, 6]],
            [[1, 4], [2, 5], [3, 6]],
        ),
        (
            [[1, 2], [3, 4], [5, 6]],
            [[1, 3, 5], [2, 4, 6]],
        ),
    ],
)
def test_transposta_casos_basicos(matriz, esperado):
    for algoritmo in ALGORITMOS:
        assert algoritmo(matriz) == esperado
