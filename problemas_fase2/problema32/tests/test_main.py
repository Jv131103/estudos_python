import pytest
from src.main import Pilha


def test_push_top():
    p = Pilha()

    p.push(10)
    p.push(20)

    assert p.top() == 20


def test_pop():
    p = Pilha()

    p.push(1)
    p.push(2)

    assert p.pop() == 2
    assert p.top() == 1


def test_get_min_basico():
    p = Pilha()

    p.push(5)
    p.push(3)
    p.push(7)

    assert p.get_min() == 3


def test_get_min_apos_pop():
    p = Pilha()

    p.push(5)
    p.push(3)
    p.push(7)

    p.pop()

    assert p.get_min() == 3


def test_get_min_atualiza():
    p = Pilha()

    p.push(5)
    p.push(3)
    p.push(2)
    p.push(7)

    assert p.get_min() == 2

    p.pop()

    assert p.get_min() == 2

    p.pop()

    assert p.get_min() == 3


def test_pilha_vazia_pop():
    p = Pilha()

    with pytest.raises(ValueError):
        p.pop()


def test_pilha_vazia_top():
    p = Pilha()

    with pytest.raises(ValueError):
        p.top()


def test_pilha_vazia_get_min():
    p = Pilha()

    with pytest.raises(ValueError):
        p.get_min()


def test_varias_operacoes():
    p = Pilha()

    p.push(10)
    p.push(4)
    p.push(8)
    p.push(1)

    assert p.get_min() == 1

    p.pop()
    assert p.get_min() == 4

    p.pop()
    assert p.get_min() == 4

    p.pop()
    assert p.get_min() == 10
