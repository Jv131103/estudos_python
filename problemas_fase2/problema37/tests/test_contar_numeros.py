import pytest
from src.contar_numero import contar_numero


@pytest.mark.parametrize(
    "valor,contagem",
    [
        (12345, 5),
        (123, 3),
        (121, 3),
        (9001, 4),
        (-505, 3),
        (-9876, 4),
        (0, 1),
        (-87, 2),
        (9, 1),
        (1000000, 7)
    ]
)
def test_deve_retornar_contagem(valor, contagem):
    assert contar_numero(valor) == contagem


def test_deve_retornar_ValueError_para_caso_string1():
    with pytest.raises(ValueError):
        assert contar_numero("1")


def test_deve_retornar_ValueError_para_caso_string2():
    with pytest.raises(ValueError):
        assert contar_numero("a")


def test_deve_retornar_ValueError_para_caso_string3():
    with pytest.raises(ValueError):
        assert contar_numero("None")


def test_deve_retornar_ValueError_para_caso_float():
    with pytest.raises(ValueError):
        assert contar_numero(1.0)


def test_deve_retornar_ValueError_para_caso_bool():
    with pytest.raises(ValueError):
        assert contar_numero(True)
