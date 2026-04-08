import pytest
from src.pilha_min import PilhaMin


def test_pilha_vazia():
    p = PilhaMin()
    assert p.is_empty() is True
    assert len(p) == 0


def test_push_e_len():
    p = PilhaMin()
    p.push(10)
    p.push(20)

    assert len(p) == 2
    assert p.is_empty() is False


def test_pop():
    p = PilhaMin()
    p.push(1)
    p.push(2)

    assert p.pop() == 2
    assert p.pop() == 1


def test_top():
    p = PilhaMin()
    p.push(5)
    p.push(10)

    assert p.top() == 10
    assert len(p) == 2


def test_get_min_simples():
    p = PilhaMin()
    p.push(5)
    p.push(3)
    p.push(7)

    assert p.get_min() == 3


def test_get_min_apos_pop():
    p = PilhaMin()
    p.push(5)
    p.push(3)
    p.push(7)

    p.pop()  # remove 7
    assert p.get_min() == 3

    p.pop()  # remove 3
    assert p.get_min() == 5


def test_valores_negativos():
    p = PilhaMin()
    p.push(2)
    p.push(-1)
    p.push(-5)

    assert p.get_min() == -5


@pytest.mark.parametrize(
    "valores, esperado",
    [
        ([5, 4, 3, 2, 1], 1),
        ([1, 2, 3, 4, 5], 1),
        ([3, 3, 3], 3),
        ([10], 10),
    ],
)
def test_varios_casos(valores, esperado):
    p = PilhaMin()

    for v in valores:
        p.push(v)

    assert p.get_min() == esperado
