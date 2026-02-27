import pytest
from src.main import (segundo_maior, segundo_maior_ordenado,
                      segundo_maior_ordenado2)


@pytest.mark.parametrize(
    "lista_desordenada,segundo_maior_valor",
    [
        ([2, 3, 0, -1, 9, 7, 10, 11], 10),
        ([-1, 10, 9, 2, 3, -1, 0], 9),
        ([5, 4, 3, 2, 1], 4),
        ([1, 2, 3, 4, 5], 4),
        ([5, 5, 5, 5, 5, 5], None),
        ([5, 5, 4, 4, 3, 2], None),
    ]
)
class TesteSegundoMaior:
    def test_segundo_maior(self, lista_desordenada, segundo_maior_valor):
        assert segundo_maior(lista_desordenada) == segundo_maior_valor

    def test_segundo_maior_ordenado(self, lista_desordenada, segundo_maior_valor):
        assert segundo_maior_ordenado(lista_desordenada) == segundo_maior_valor

    def test_segundo_maior_ordenado2(self, lista_desordenada, segundo_maior_valor):
        assert segundo_maior_ordenado2(lista_desordenada.copy()) == segundo_maior_valor
