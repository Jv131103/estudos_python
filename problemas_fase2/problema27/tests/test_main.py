import pytest
from src.main import PriorityQueue


def test_push_adiciona_elemento():
    fila = PriorityQueue()

    fila.push("João", 3)

    assert fila.dados == [(3, "João")]


def test_pop_retorna_elemento_maior_prioridade():
    fila = PriorityQueue()

    fila.push("João", 3)
    fila.push("Maria", 1)
    fila.push("Pedro", 2)

    assert fila.pop() == "Maria"


def test_pop_remove_na_ordem_correta():
    fila = PriorityQueue()

    fila.push("João", 3)
    fila.push("Maria", 1)
    fila.push("Pedro", 2)

    assert fila.pop() == "Maria"
    assert fila.pop() == "Pedro"
    assert fila.pop() == "João"


def test_pop_fila_vazia_dispara_erro():
    fila = PriorityQueue()

    with pytest.raises(IndexError, match="pop from empty list"):
        fila.pop()


def test_push_varios_elementos():
    fila = PriorityQueue()

    fila.push("A", 3)
    fila.push("B", 2)
    fila.push("C", 1)

    assert len(fila.dados) == 3


def test_elementos_mesma_prioridade():
    fila = PriorityQueue()

    fila.push("Ana", 2)
    fila.push("Bruno", 2)
    fila.push("Carlos", 2)

    primeiro = fila.pop()
    segundo = fila.pop()
    terceiro = fila.pop()

    assert {primeiro, segundo, terceiro} == {"Ana", "Bruno", "Carlos"}


def test_apos_pop_elemento_e_removido():
    fila = PriorityQueue()

    fila.push("João", 3)
    fila.push("Maria", 1)

    fila.pop()

    assert len(fila.dados) == 1
    assert fila.dados == [(3, "João")]
