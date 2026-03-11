from src.main import Fila


def test_fila_vazia():
    f = Fila()
    assert f.is_empty()


def test_enqueue():
    f = Fila()
    f.enqueue(10)

    assert f.size() == 1
    assert f.peek() == 10


def test_dequeue():
    f = Fila()
    f.enqueue(10)
    f.enqueue(20)

    valor = f.dequeue()

    assert valor == 10
    assert f.size() == 1


def test_peek():
    f = Fila()
    f.enqueue(5)
    f.enqueue(7)

    assert f.peek() == 5


def test_dequeue_fila_vazia():
    f = Fila()

    valor = f.dequeue()

    assert valor is None
