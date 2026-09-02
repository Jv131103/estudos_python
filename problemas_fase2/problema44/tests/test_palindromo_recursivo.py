import pytest
from src.palindromo_recursivo import eh_palindromo


@pytest.mark.parametrize("entrada, esperado", [
    ("arara", True),
    ("python", False),
    ("Ana", True),
    ("A base do teto", False),
    ("radar", True),
    ("Socorram-me, subi no ônibus em Marrocos", True),
    ("Batata", False)
])
def test_palindromo(entrada, esperado):
    assert eh_palindromo(entrada) == esperado
