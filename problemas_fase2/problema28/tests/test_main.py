import pytest
from src.main import FilaCircular


def test_enqueue_adiciona_elemento():
    fila = FilaCircular(3)

    fila.enqueue(10)

    assert fila.size() == 1
    assert fila.peek() == 10


def test_dequeue_remove_elemento():
    fila = FilaCircular(3)

    fila.enqueue(10)
    fila.enqueue(20)

    valor = fila.dequeue()

    assert valor == 10
    assert fila.size() == 1


def test_peek_nao_remove():
    fila = FilaCircular(3)

    fila.enqueue(10)

    assert fila.peek() == 10
    assert fila.size() == 1


def test_fila_cheia():
    fila = FilaCircular(2)

    fila.enqueue(1)
    fila.enqueue(2)

    with pytest.raises(Exception, match="Fila cheia"):
        fila.enqueue(3)


def test_fila_vazia():
    fila = FilaCircular(2)

    with pytest.raises(Exception, match="Fila vazia"):
        fila.dequeue()


def test_fila_circular():
    fila = FilaCircular(3)

    fila.enqueue(1)
    fila.enqueue(2)
    fila.enqueue(3)

    fila.dequeue()

    fila.enqueue(4)

    assert str(fila) == "2 3 4"


def test_is_empty():
    fila = FilaCircular(2)

    assert fila.is_empty()

    fila.enqueue(10)

    assert not fila.is_empty()


def test_size():
    fila = FilaCircular(5)

    fila.enqueue(1)
    fila.enqueue(2)

    assert fila.size() == 2

    fila.dequeue()

    assert fila.size() == 1


@pytest.mark.parametrize("valores", [
    [1],
    [1, 2],
    [1, 2, 3]
])
def test_enqueue_varios(valores):

    fila = FilaCircular(5)

    for v in valores:
        fila.enqueue(v)

    assert fila.size() == len(valores)
