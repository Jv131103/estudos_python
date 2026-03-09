import pytest
from src.main import espiral, espiral_direcoes, espiral_pop

ALGORITMOS = [
    espiral,
    espiral_direcoes,
    espiral_pop,
]


def copiar_matriz(matriz):
    return [linha[:] for linha in matriz]


@pytest.mark.parametrize(
    "matriz, esperado",
    [
        (
            [[1]],
            [1],
        ),
        (
            [[1, 2, 3]],
            [1, 2, 3],
        ),
        (
            [[1], [2], [3]],
            [1, 2, 3],
        ),
        (
            [
                [1, 2],
                [3, 4],
            ],
            [1, 2, 4, 3],
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
            ],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
            ],
            [1, 2, 3, 6, 5, 4],
        ),
    ],
)
def test_espiral_casos_basicos(matriz, esperado):
    for algoritmo in ALGORITMOS:
        resultado = algoritmo(copiar_matriz(matriz))
        assert resultado == esperado
