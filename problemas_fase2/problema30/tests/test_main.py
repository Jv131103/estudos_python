from src.main import Deque


def test_adicionar_um_esquerda_e_direita():
    d = Deque()
    d.append_right(1)
    d.append_left(2)
    assert d.dados == [2, 1]


def test_adicionar_um_direita():
    d = Deque()
    d.append_right(1)
    assert d.dados == [1]


def test_adicionar_um_esquerda():
    d = Deque()
    d.append_left(1)
    assert d.dados == [1]


def test_adicionar_varios_esquerda_e_direita():
    d = Deque()

    d.append_right(10)
    d.append_right(20)
    d.append_left(5)
    d.append_left(6)

    assert d.dados == [6, 5, 10, 20]


def test_adicionar_varios_direita():
    d = Deque()

    d.append_right(10)
    d.append_right(20)
    d.append_right(30)
    d.append_right(40)

    assert d.dados == [10, 20, 30, 40]


def test_adicionar_varios_esquerda():
    d = Deque()

    d.append_left(10)
    d.append_left(20)
    d.append_left(30)
    d.append_left(40)

    assert d.dados == [40, 30, 20, 10]


def test_is_empty_false_quando_tem_dados():
    d = Deque()
    d.append_right(10)
    d.append_right(20)
    d.append_left(5)
    d.append_left(6)

    assert d.is_empty() is False


def test_is_empty_true_quando_nao_tem_dados():
    d = Deque()

    assert d.is_empty() is True


def test_peek_front_nao_e_menos1():
    d = Deque()

    d.append_right(10)

    assert d.peek_front() == 10


def test_peek_back_nao_e_menos1():
    d = Deque()

    d.append_right(10)

    assert d.peek_back() == 10


def test_size_e_diferente_de0():
    d = Deque()

    d.append_right(10)
    d.append_right(20)
    d.append_left(5)
    d.append_left(6)

    assert d.size() != 0


def test_size_e_igual_a0():
    d = Deque()

    assert d.size() == 0
