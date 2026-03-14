import pytest
from src.main import ArrayDinamico


def test_append_basico():

    a = ArrayDinamico()

    a.append(1)
    a.append(2)
    a.append(3)

    assert a.size() == 3
    assert a.get(0) == 1
    assert a.get(1) == 2
    assert a.get(2) == 3


def test_capacity_crescimento():

    a = ArrayDinamico()

    capacidade_inicial = a.capacity()

    a.append(1)
    a.append(2)

    assert a.capacity() >= capacidade_inicial


def test_resize_funciona():

    a = ArrayDinamico()

    for i in range(10):
        a.append(i)

    for i in range(10):
        assert a.get(i) == i


def test_size():

    a = ArrayDinamico()

    assert a.size() == 0

    a.append(1)
    a.append(2)

    assert a.size() == 2


def test_capacity_dobra():

    a = ArrayDinamico()

    cap1 = a.capacity()

    a.append(1)
    a.append(2)

    cap2 = a.capacity()

    assert cap2 >= cap1


def test_get_indice_invalido():

    a = ArrayDinamico()

    a.append(10)

    with pytest.raises(IndexError):
        a.get(5)


def test_get_indice_negativo():

    a = ArrayDinamico()

    a.append(10)

    with pytest.raises(IndexError):
        a.get(-1)


def test_grande_volume():

    a = ArrayDinamico()

    for i in range(10000):
        a.append(i)

    assert a.size() == 10000

    assert a.get(0) == 0
    assert a.get(9999) == 9999


def test_consistencia_pos_resize():

    a = ArrayDinamico()

    for i in range(50):
        a.append(i)

    for i in range(50):
        assert a.get(i) == i
