import pytest
from src.look_say import look_and_say1, look_and_say2


@pytest.mark.parametrize(
    "look,say",
    [
        ('1', '11'),
        ('11', '21'),
        ('21', '1211'),
        ('221', '2211'),
        ('301', '131011'),
        ('9886', '192816'),
        ('0', '10'),
    ]
)
def test_deve_gerar_look_and_say(look, say):
    assert look_and_say1(look) == say
    assert look_and_say2(look) == say


def test_deve_retornar_ValueError_para_caso_string1():
    with pytest.raises(ValueError):
        assert look_and_say1(" 1 ")


def test_deve_retornar_ValueError_para_caso_string2():
    with pytest.raises(ValueError):
        assert look_and_say1("a")


def test_deve_retornar_ValueError_para_caso_string3():
    with pytest.raises(ValueError):
        assert look_and_say1("None")


def test_deve_retornar_TypeError_para_caso_float():
    with pytest.raises(TypeError):
        assert look_and_say1(1.0)


def test_deve_retornar_TypeError_para_caso_bool():
    with pytest.raises(TypeError):
        assert look_and_say1(True)


def test_deve_retornar_TypeError_para_caso_int():
    with pytest.raises(TypeError):
        assert look_and_say1(12)
