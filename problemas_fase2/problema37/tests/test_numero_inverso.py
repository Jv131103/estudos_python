import pytest
from src.numero_inverso import inverter


@pytest.mark.parametrize(
    "valor,inverso",
    [
        (12345, 54321),
        (123, 321),
        (121, 121),
        (9001, 1009),
        (-505, -505),
        (-9876, -6789),
        (0, 0),
        (-87, -78)
    ]
)
def test_deve_retornar_inverso(valor, inverso):
    assert inverter(valor) == inverso


def test_deve_retornar_ValueError_para_caso_string1():
    with pytest.raises(ValueError):
        assert inverter("1")


def test_deve_retornar_ValueError_para_caso_string2():
    with pytest.raises(ValueError):
        assert inverter("a")


def test_deve_retornar_ValueError_para_caso_string3():
    with pytest.raises(ValueError):
        assert inverter("None")


def test_deve_retornar_ValueError_para_caso_float():
    with pytest.raises(ValueError):
        assert inverter(1.0)


def test_deve_retornar_ValueError_para_caso_bool():
    with pytest.raises(ValueError):
        assert inverter(True)
