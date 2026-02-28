import pytest
from src.main import busca_binaria, busca_binaria_recursivo


@pytest.mark.parametrize(
    "lista,busca,saida",
    [
        ([1, 2, 3, 4, 5, 6, 7], 4, 3),
        ([1, 2, 3, 4, 5, 6, 7], 1, 0),
        ([1, 2, 3, 4, 5, 6, 7], 7, 6),
        ([1, 2, 3, 4, 5, 6, 7], 2, 1),
        ([1, 2, 3, 4, 5, 6, 7], 5, 4),
        ([1, 2, 3, 4], 2, 1),
        ([1, 2, 3, 4], 2, 1),
        ([1, 2, 3, 4], 3, 2),
        ([1, 2, 3, 4], 1, 0),
        ([1, 2, 3, 4], 4, 3),
    ]
)
class TestBuscaBinaria:
    def test_busca_binaria(self, lista, busca, saida):
        assert busca_binaria(lista, busca) == saida

    def test_busca_binaria_recursiva(self, lista, busca, saida):
        assert busca_binaria_recursivo(lista, busca) == saida
