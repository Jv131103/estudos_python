import pytest
from src.main import verificar, verificar2, verificar3, verificar4

ALGORITMOS = [
    verificar,
    verificar2,
    verificar3,
    verificar4
]


@pytest.mark.parametrize(
    "expressao,resultado",
    [
        ("()", True),
        ("[]", True),
        ("{}", True),
        ("[()]", True),
        ("{[()]}", True),
        ("{[()]", False),
        ("[()]}", False),
        (")", False),
        ("(", False),
        (")(", False),
    ]
)
def test_validar_expressao(expressao, resultado):
    for algoritmo in ALGORITMOS:
        assert algoritmo(expressao) == resultado
