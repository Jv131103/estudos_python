import pytest
from src.main import FilaComPilha


def test_fila_comeca_vazia():
    f = FilaComPilha()
    assert f.is_empty() is True
    assert f.size() == 0


def test_enqueue_adiciona_elementos():
    f = FilaComPilha()

    f.enqueue(10)
    f.enqueue(20)

    assert f.is_empty() is False
    assert f.size() == 2


def test_dequeue_respeita_fifo():
    f = FilaComPilha()

    f.enqueue(10)
    f.enqueue(20)
    f.enqueue(30)

    assert f.dequeue() == 10
    assert f.dequeue() == 20
    assert f.dequeue() == 30


def test_peek_retorna_primeiro_sem_remover():
    f = FilaComPilha()

    f.enqueue(10)
    f.enqueue(20)

    assert f.peek() == 10
    assert f.peek() == 10
    assert f.size() == 2


def test_size_funciona_apos_enqueue_e_dequeue():
    f = FilaComPilha()

    f.enqueue(1)
    f.enqueue(2)
    f.enqueue(3)
    assert f.size() == 3

    f.dequeue()
    assert f.size() == 2

    f.dequeue()
    assert f.size() == 1


def test_is_empty_depois_de_remover_tudo():
    f = FilaComPilha()

    f.enqueue("A")
    f.enqueue("B")

    f.dequeue()
    f.dequeue()

    assert f.is_empty() is True
    assert f.size() == 0


def test_dequeue_em_fila_vazia_levanta_erro():
    f = FilaComPilha()

    with pytest.raises(IndexError, match="fila vazia"):
        f.dequeue()


def test_peek_em_fila_vazia_levanta_erro():
    f = FilaComPilha()

    with pytest.raises(IndexError, match="fila vazia"):
        f.peek()


def test_funciona_com_transferencia_entre_pilhas():
    f = FilaComPilha()

    f.enqueue(1)
    f.enqueue(2)
    f.enqueue(3)

    assert f.dequeue() == 1

    f.enqueue(4)
    f.enqueue(5)

    assert f.dequeue() == 2
    assert f.dequeue() == 3
    assert f.dequeue() == 4
    assert f.dequeue() == 5


def test_peek_apos_transferencia():
    f = FilaComPilha()

    f.enqueue(100)
    f.enqueue(200)
    f.enqueue(300)

    assert f.peek() == 100
    assert f.size() == 3

    assert f.dequeue() == 100
    assert f.peek() == 200


@pytest.mark.parametrize(
    "valores",
    [
        [1],
        [1, 2],
        [10, 20, 30, 40],
        ["a", "b", "c"],
    ],
)
def test_fifo_com_varios_dados(valores):
    f = FilaComPilha()

    for v in valores:
        f.enqueue(v)

    saida = []
    while not f.is_empty():
        saida.append(f.dequeue())

    assert saida == valores
