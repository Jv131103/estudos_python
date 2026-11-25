import pytest
from src.atualizar_a import atualizar_a

# Dados do exemplo: temperatura = 30 + 0.2 * cpu (peso ideal = 0.2, bias ideal = 30, a ideal = 0)
DADOS = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50),
]


def test_exemplo_do_enunciado():
    novo_a = atualizar_a(DADOS, a=0.001, peso=0.2, bias=30, learning_rate=0.00000001)
    assert novo_a == pytest.approx(0.000446875, abs=1e-12)


def test_a_ideal_nao_muda():
    # Previsões perfeitas -> gradiente zero
    novo_a = atualizar_a(DADOS, a=0, peso=0.2, bias=30, learning_rate=0.00000001)
    assert novo_a == pytest.approx(0, abs=1e-12)


def test_a_acima_do_ideal_diminui():
    novo_a = atualizar_a(DADOS, a=0.001, peso=0.2, bias=30, learning_rate=0.00000001)
    assert novo_a < 0.001


def test_a_abaixo_do_ideal_aumenta():
    novo_a = atualizar_a(DADOS, a=-0.001, peso=0.2, bias=30, learning_rate=0.00000001)
    assert novo_a > -0.001


def test_learning_rate_zero_nao_altera_a():
    assert atualizar_a(DADOS, 0.001, 0.2, 30, 0) == 0.001


def test_um_unico_dado_calculo_manual():
    # previsão = 0 * 10² + 1 * 10 + 0 = 10; contribuição = 2 * 10² * (10 - 20) = -2000
    # gradiente = -2000; novo_a = 0 - 0.001 * (-2000) = 2
    novo_a = atualizar_a([(10, 20)], a=0, peso=1, bias=0, learning_rate=0.001)
    assert novo_a == pytest.approx(2.0)


def test_cpu_zero_nao_contribui_para_o_gradiente():
    novo_a = atualizar_a([(0, 100)], a=0.5, peso=0.2, bias=30, learning_rate=0.1)
    assert novo_a == pytest.approx(0.5)


def test_nao_modifica_a_lista_de_dados():
    copia = list(DADOS)
    atualizar_a(DADOS, 0.001, 0.2, 30, 0.00000001)
    assert DADOS == copia


def test_lista_vazia_levanta_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        atualizar_a([], a=0.001, peso=0.2, bias=30, learning_rate=0.00000001)
