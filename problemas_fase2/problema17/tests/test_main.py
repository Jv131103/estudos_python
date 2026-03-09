import pytest
from src.main import busca_binaria, busca_binaria_recursiva

FUNCOES = [
    busca_binaria,
    busca_binaria_recursiva
]


@pytest.mark.parametrize(
    "lista,alvo,posicao_encontrada",
    [
        ([1, 3, 5, 7, 9, 11, 13], 9, 4),
        ([1, 3, 5, 7, 9, 11, 13], 13, 6),
        ([1, 3, 5, 7, 9, 11, 13], 1, 0),
        ([1, 3, 5, 7, 9, 11, 13], 7, 3),
        ([1, 3, 5, 7, 9, 11, 13], 0, -1),
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 10, -1)
    ]
)
def test_busca_binaria(lista, alvo, posicao_encontrada):
    for algoritmo in FUNCOES:
        assert algoritmo(lista, alvo) == posicao_encontrada
