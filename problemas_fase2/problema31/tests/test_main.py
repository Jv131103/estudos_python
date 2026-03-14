import pytest
from src.classes import Deque, Pilha
from src.funcoes import (dois_ponteiros, manual, recursicion, reverse_py,
                         slicing_py, slicing_py2, tecnica_pilha)
from src.main import (is_palinder_class_pilha, is_palinder_deque,
                      is_palinder_dois_ponteiros, is_palinder_list_pilha,
                      is_palinder_manual, is_palinder_recursicion,
                      is_palinder_reverse, is_palinder_slicing1,
                      is_palinder_slicing2)

# =========================
# Testes das classes
# =========================


def test_deque_append_left():
    d = Deque()
    d.append_left("B")
    d.append_left("A")

    assert d.dados == ["A", "B"]


def test_deque_append_right():
    d = Deque()
    d.append_right("A")
    d.append_right("B")

    assert d.dados == ["A", "B"]


def test_deque_pop_left():
    d = Deque()
    d.append_right("A")
    d.append_right("B")

    assert d.pop_left() == "A"
    assert d.dados == ["B"]


def test_deque_pop_right():
    d = Deque()
    d.append_right("A")
    d.append_right("B")

    assert d.pop_right() == "B"
    assert d.dados == ["A"]


def test_deque_pop_left_vazio():
    d = Deque()

    with pytest.raises(ValueError, match="Fila Vazia"):
        d.pop_left()


def test_deque_pop_right_vazio():
    d = Deque()

    with pytest.raises(ValueError, match="Fila Vazia"):
        d.pop_right()


def test_deque_peek_front():
    d = Deque()
    d.append_right("A")
    d.append_right("B")

    assert d.peek_front() == "A"


def test_deque_peek_back():
    d = Deque()
    d.append_right("A")
    d.append_right("B")

    assert d.peek_back() == "B"


def test_deque_peek_em_vazio():
    d = Deque()

    assert d.peek_front() == -1
    assert d.peek_back() == -1


def test_deque_is_empty():
    d = Deque()
    assert d.is_empty() is True

    d.append_right(10)
    assert d.is_empty() is False


def test_deque_size():
    d = Deque()
    assert d.size() == 0

    d.append_right(10)
    d.append_left(5)

    assert d.size() == 2


def test_pilha_push_pop():
    p = Pilha()
    p.push("A")
    p.push("B")

    assert p.pop() == "B"
    assert p.pop() == "A"


def test_pilha_peek():
    p = Pilha()
    p.push("A")
    p.push("B")

    assert p.peek() == "B"


def test_pilha_is_empty():
    p = Pilha()
    assert p.is_empty() is True

    p.push("A")
    assert p.is_empty() is False


# =========================
# Testes das funções de inverter
# =========================

@pytest.mark.parametrize(
    "func, entrada, esperado",
    [
        (slicing_py, "abc", "cba"),
        (slicing_py2, "abc", "cba"),
        (manual, "abc", "cba"),
        (dois_ponteiros, "abc", "cba"),
        (reverse_py, "abc", "cba"),
        (tecnica_pilha, "abc", "cba"),
        (recursicion, "abc", "cba"),
    ],
)
def test_funcoes_invertem_string(func, entrada, esperado):
    assert func(entrada) == esperado


@pytest.mark.parametrize(
    "func",
    [slicing_py, slicing_py2, manual, dois_ponteiros, reverse_py, tecnica_pilha, recursicion],
)
def test_funcoes_string_vazia(func):
    assert func("") == ""


@pytest.mark.parametrize(
    "func",
    [slicing_py, slicing_py2, manual, dois_ponteiros, reverse_py, tecnica_pilha, recursicion],
)
def test_funcoes_um_caractere(func):
    assert func("a") == "a"


# =========================
# Testes das funções de palíndromo
# =========================

funcoes_palindromo = [
    is_palinder_deque,
    is_palinder_class_pilha,
    is_palinder_list_pilha,
    is_palinder_slicing1,
    is_palinder_slicing2,
    is_palinder_dois_ponteiros,
    is_palinder_manual,
    is_palinder_reverse,
    is_palinder_recursicion,
]


@pytest.mark.parametrize("func", funcoes_palindromo)
def test_palindromo_com_ovo(func):
    assert func("ovo") is True


@pytest.mark.parametrize("func", funcoes_palindromo)
def test_palindromo_com_ana(func):
    assert func("ana") is True


@pytest.mark.parametrize("func", funcoes_palindromo)
def test_nao_palindromo_com_banana(func):
    assert func("banana") is False


@pytest.mark.parametrize("func", funcoes_palindromo)
def test_string_vazia_e_palindromo(func):
    assert func("") is True


@pytest.mark.parametrize("func", funcoes_palindromo)
def test_um_caractere_e_palindromo(func):
    assert func("a") is True


@pytest.mark.parametrize(
    "func",
    [
        is_palinder_deque,
        is_palinder_class_pilha,
        is_palinder_list_pilha,
        is_palinder_slicing1,
        is_palinder_slicing2,
        is_palinder_dois_ponteiros,
        is_palinder_manual,
        is_palinder_reverse,
    ],
)
def test_palindromo_maior(func):
    assert func("arara") is True


@pytest.mark.parametrize(
    "func",
    [
        is_palinder_deque,
        is_palinder_class_pilha,
        is_palinder_list_pilha,
        is_palinder_slicing1,
        is_palinder_slicing2,
        is_palinder_dois_ponteiros,
        is_palinder_manual,
        is_palinder_reverse,
    ],
)
def test_nao_palindromo_maior(func):
    assert func("computador") is False
