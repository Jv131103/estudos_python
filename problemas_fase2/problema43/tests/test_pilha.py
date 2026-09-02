import pytest
from src.pilha import Pilha, PilhaVaziaError


@pytest.fixture
def pilha_vazia():
    return Pilha()


def test_pilha_comeca_vazia(pilha_vazia):
    assert pilha_vazia.is_empty() is True


def test_empilhar_um_item(pilha_vazia):
    pilha_vazia.push(10)
    assert pilha_vazia.is_empty() is False
    assert pilha_vazia.peek() == 10


def test_desempilhar_um_item(pilha_vazia):
    pilha_vazia.push(10)
    pilha_vazia.push(20)
    assert pilha_vazia.peek() == 20
    assert pilha_vazia.pop() == 20
    assert pilha_vazia.peek() == 10


def test_erro_desempilhar(pilha_vazia):
    with pytest.raises(PilhaVaziaError):
        assert pilha_vazia.pop()
