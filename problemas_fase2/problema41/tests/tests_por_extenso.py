import pytest
from src.por_extenso import por_extenso


@pytest.mark.parametrize("numero, esperado", [
    (0, "zero"),
    (15, "quinze"),
    (20, "vinte"),
    (47, "quarenta e sete"),
    (99, "noventa e nove"),
    (100, "Fora do intervalo"),
    (-100, "Fora do intervalo"),
])
def test_por_extenso(numero, esperado):
    assert por_extenso(numero) == esperado
