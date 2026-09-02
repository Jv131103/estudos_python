import pytest
from src.divisao import dividir


def test_divisao_normal():
    assert dividir(10, 2) == 5


def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)


def test_divisao_retorno_decimal():
    assert dividir(7, 2) == 3.5


def test_divisao_decimal():
    assert dividir(4.2, 4) == 1.05


def test_divisao_negativo1():
    assert dividir(-10, 2) == -5


def test_divisao_negativo2():
    assert dividir(10, -2) == -5
