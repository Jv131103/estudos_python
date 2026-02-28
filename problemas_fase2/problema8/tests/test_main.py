import pytest
from src.main import (inserir1, inserir2, inserir3, inserir4, inserir5,
                      inserir6, inserir7)


@pytest.mark.parametrize(
    "lista,inserir,esperado",
    [
        ([1, 4, 6, 10], 5, [1, 4, 5, 6, 10]),
        ([1, 2, 3, 4, 5, 6], 5, [1, 2, 3, 4, 5, 5, 6]),
        ([5, 5, 5, 5, 5], 5, [5, 5, 5, 5, 5, 5]),
        ([1, 2], 5, [1, 2, 5]),
        ([6, 7, 8], 5, [5, 6, 7, 8]),
        ([], 5, [5]),
    ]
)
class TestInsercaoListaOrdenada:
    def test_inserir1(self, lista, inserir, esperado):
        assert inserir1(lista.copy(), inserir) == esperado

    def test_inserir2(self, lista, inserir, esperado):
        assert inserir2(lista.copy(), inserir) == esperado

    def test_inserir3(self, lista, inserir, esperado):
        assert inserir3(lista.copy(), inserir) == esperado

    def test_inserir4(self, lista, inserir, esperado):
        assert inserir4(lista.copy(), inserir) == esperado

    def test_inserir5(self, lista, inserir, esperado):
        assert inserir5(lista.copy(), inserir) == esperado

    def test_inserir6(self, lista, inserir, esperado):
        assert inserir6(lista.copy(), inserir) == esperado

    def test_inserir7(self, lista, inserir, esperado):
        assert inserir7(lista.copy(), inserir) == esperado
