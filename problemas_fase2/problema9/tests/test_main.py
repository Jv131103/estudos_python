import pytest
from src.main import circularizar, circularizar2, circularizar3


@pytest.mark.parametrize(
    "lista,indice,esperado",
    [
        ([10, 20, 30, 40], -1, 10),
        ([10, 20, 30, 40], 0, 20),
        ([10, 20, 30, 40], 1, 30),
        ([10, 20, 30, 40], 2, 40),
        ([10, 20, 30, 40], 3, 10),
        ([10, 20, 30, 40], 4, None),
        ([10, 20, 30, 40], 5, None),
        ([10, 20, 30, 40], 6, None),
    ]
)
class TestCircularidade:
    def test_circularizar(self, lista, indice, esperado):
        assert circularizar(lista, indice) == esperado

    def test_circularizar2(self, lista, indice, esperado):
        assert circularizar2(lista, indice) == esperado

    def test_circularizar3(self, lista, indice, esperado):
        assert circularizar3(lista, indice) == esperado
