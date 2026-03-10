from src.main import (avaliar_postfix, avaliar_prefix, divisao_real,
                      multiplicacao, resto_divisao, soma, subtracao)

# =========================
# Testes das operações
# =========================


def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0


def test_subtracao():
    assert subtracao(10, 5) == 5
    assert subtracao(5, 10) == -5


def test_multiplicacao():
    assert multiplicacao(3, 4) == 12
    assert multiplicacao(-2, 3) == -6


def test_divisao():
    assert divisao_real(6, 3) == 2
    assert divisao_real(5, 2) == 2.5


def test_divisao_por_zero():
    assert divisao_real(10, 0) == "Erro de divisão por 0"


def test_resto():
    assert resto_divisao(10, 3) == 1


def test_resto_zero():
    assert resto_divisao(10, 0) == "Erro de divisão por 0"


# =========================
# Testes postfix
# =========================

def test_postfix_soma():
    assert avaliar_postfix("2 3 +") == 5


def test_postfix_expressao_complexa():
    # exemplo clássico
    assert avaliar_postfix("5 1 2 + 4 * + 3 -") == 14


def test_postfix_divisao():
    assert avaliar_postfix("6 3 /") == 2


def test_postfix_resto():
    assert avaliar_postfix("7 3 %") == 1


# =========================
# Testes prefix
# =========================

def test_prefix_soma():
    assert avaliar_prefix("+ 2 3") == 5


def test_prefix_multiplicacao():
    assert avaliar_prefix("* 4 3") == 12


def test_prefix_expressao():
    # equivalente a (2 + (3 * 4))
    assert avaliar_prefix("+ 2 * 3 4") == 14
