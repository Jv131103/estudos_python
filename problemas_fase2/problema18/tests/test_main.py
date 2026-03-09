import pytest
from src.main import maior_menor_indice, maior_menor_indice2

ALGORITMOS = [
    maior_menor_indice,
    maior_menor_indice2
]


@pytest.mark.parametrize(
    "lista,alvo,maior_menor",
    [
        ([1, 2, 2, 2, 3, 4, 4, 5], 2, (1, 3)),
        ([1, 2, 2, 2, 3, 4, 4, 5], 4, (5, 6)),
        ([1, 2, 3, 4, 4, 4, 4, 5], 4, (3, 6)),
        ([4, 4, 4, 4, 4, 4, 4], 4, (0, 6)),
        ([1, 2, 2, 2, 3, 4, 4, 5], 7, (-1, -1)),
        ([4, 4, 4, 4, 4, 4, 4], 5, (-1, -1)),
        ([], 5, (-1, -1)),
    ]
)
def test_buscas_maior_menor(lista, alvo, maior_menor):
    for algoritmo in ALGORITMOS:
        assert algoritmo(lista, alvo) == maior_menor
