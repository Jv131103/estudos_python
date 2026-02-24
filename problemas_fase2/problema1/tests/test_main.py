import pytest
from src.main import (reversao_manual_eficiente, reversao_slicing_manual,
                      reversao_slicing_manual_pythonico,
                      reversao_tecnica_dois_ponteiros,
                      reversao_tecnica_dois_ponteiros_lista,
                      reversao_tecnica_slicing_pythonico,
                      reversao_tecnica_slicing_reverse,
                      reverse_divide_conquer_join)


@pytest.mark.parametrize(
    "nao_invertido,invertido",
    [
        ("banana", "ananab"),
        ("teste", "etset"),
        ("arara", "arara"),
        ("ovo", "ovo"),
        ("python", "nohtyp"),
        ("paralelogramo", "omargolelarap")
    ],
)
class TestReversoes:
    def test_reversao_manual_eficiente(self, nao_invertido, invertido):
        assert reversao_manual_eficiente(nao_invertido) == invertido

    def test_reversao_slicing_manual(self, nao_invertido, invertido):
        assert reversao_slicing_manual(nao_invertido) == invertido

    def test_reversao_slicing_manual_pythonico(self, nao_invertido, invertido):
        assert reversao_slicing_manual_pythonico(nao_invertido) == invertido

    def test_reversao_tecnica_dois_ponteiros(self, nao_invertido, invertido):
        assert reversao_tecnica_dois_ponteiros(nao_invertido) == invertido

    def test_reversao_tecnica_dois_ponteiros_lista(self, nao_invertido, invertido):
        assert reversao_tecnica_dois_ponteiros_lista(nao_invertido) == invertido

    def test_reversao_tecnica_slicing_pythonico(self, nao_invertido, invertido):
        assert reversao_tecnica_slicing_pythonico(nao_invertido) == invertido

    def test_reversao_tecnica_slicing_reverse(self, nao_invertido, invertido):
        assert reversao_tecnica_slicing_reverse(nao_invertido) == invertido

    def test_reverse_divide_conquer_join(self, nao_invertido, invertido):
        assert reverse_divide_conquer_join(nao_invertido) == invertido
