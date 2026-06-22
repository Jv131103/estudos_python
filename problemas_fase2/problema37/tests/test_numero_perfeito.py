import pytest
from src.numero_perfeito import is_perfect, is_perfect2


@pytest.mark.parametrize(
    "valor,resultado",
    [
        (6, True),
        (28, True),
        (12, False),
        (1, False),
        (0, False)
    ]
)
def test_deve_validar_se_eh_perfeito_ou_nao(valor, resultado):
    assert is_perfect(valor) == resultado
    assert is_perfect2(valor) == resultado


def test_deve_retornar_ValueError_para_caso_string1_perfect1():
    with pytest.raises(ValueError):
        assert is_perfect("1")


def test_deve_retornar_ValueError_para_caso_string1_perfect2():
    with pytest.raises(ValueError):
        assert is_perfect2("1")


def test_deve_retornar_ValueError_para_caso_string2_perfect1():
    with pytest.raises(ValueError):
        assert is_perfect("a")


def test_deve_retornar_ValueError_para_caso_string2_perfect2():
    with pytest.raises(ValueError):
        assert is_perfect2("a")


def test_deve_retornar_ValueError_para_caso_string3_perfect1():
    with pytest.raises(ValueError):
        assert is_perfect("None")


def test_deve_retornar_ValueError_para_caso_string3_perfect2():
    with pytest.raises(ValueError):
        assert is_perfect2("None")


def test_deve_retornar_ValueError_para_caso_float_perfect1():
    with pytest.raises(ValueError):
        assert is_perfect(1.0)


def test_deve_retornar_ValueError_para_caso_float_perfect2():
    with pytest.raises(ValueError):
        assert is_perfect2(1.0)


def test_deve_retornar_ValueError_para_caso_bool_perfect1():
    with pytest.raises(ValueError):
        assert is_perfect(True)


def test_deve_retornar_ValueError_para_caso_bool_perfect2():
    with pytest.raises(ValueError):
        assert is_perfect2(True)
