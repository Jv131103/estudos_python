import pytest
from src.main import (maior_menor_manual, maior_menor_ordenado_inplace,
                      maior_menor_ordenado_nao_inplace,
                      maior_menor_ordenado_pythonico, maior_menor_pythonico,
                      maior_menor_recursivo)


@pytest.mark.parametrize(
    "lista_desordenada,min_max",
    [
        ([9, 2, 1, 0, 5, 6, 10, 11, 12], (0, 12)),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (1, 10)),
        ([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], (5, 5)),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2], (2, 10))
    ]
)
class TestMinMax:
    def test_maior_menor_manual(self, lista_desordenada, min_max):
        assert maior_menor_manual(lista_desordenada) == min_max

    def test_maior_menor_ordenado_inplace(self, lista_desordenada, min_max):
        assert maior_menor_ordenado_inplace(lista_desordenada.copy()) == min_max

    def test_maior_menor_ordenado_nao_inplace(self, lista_desordenada, min_max):
        assert maior_menor_ordenado_nao_inplace(lista_desordenada) == min_max

    def test_maior_menor_ordenado_pythonico(self, lista_desordenada, min_max):
        assert maior_menor_ordenado_pythonico(lista_desordenada) == min_max

    def test_maior_menor_pythonico(self, lista_desordenada, min_max):
        assert maior_menor_pythonico(lista_desordenada) == min_max

    def test_maior_menor_recursivo(self, lista_desordenada, min_max):
        assert maior_menor_recursivo(lista_desordenada) == min_max
