import pytest
from src.atualizar_bias_quadratico import atualizar_bias_quadratico

# Dados do exemplo: temperatura = 30 + 0.2 * cpu (peso ideal = 0.2, bias ideal = 30, a ideal = 0)
DADOS = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50),
]


def test_exemplo_do_enunciado():
    novo_bias = atualizar_bias_quadratico(
        DADOS, a=0.001, peso=0.2, bias=30, learning_rate=0.000001
    )
    assert novo_bias == pytest.approx(29.9999925, abs=1e-10)


def test_parametros_ideais_nao_mudam_o_bias():
    # Previsões perfeitas -> gradiente zero
    novo_bias = atualizar_bias_quadratico(DADOS, a=0, peso=0.2, bias=30, learning_rate=0.01)
    assert novo_bias == pytest.approx(30)


def test_com_a_zero_equivale_ao_modelo_linear():
    # Mesmo resultado do exemplo de atualizar_bias (modelo linear)
    novo_bias = atualizar_bias_quadratico(DADOS, a=0, peso=0.1, bias=30, learning_rate=0.0001)
    assert novo_bias == pytest.approx(30.001, abs=1e-10)


def test_bias_acima_do_ideal_diminui():
    novo_bias = atualizar_bias_quadratico(DADOS, a=0, peso=0.2, bias=35, learning_rate=0.01)
    assert novo_bias == pytest.approx(34.9)


def test_bias_abaixo_do_ideal_aumenta():
    novo_bias = atualizar_bias_quadratico(DADOS, a=0, peso=0.2, bias=25, learning_rate=0.01)
    assert novo_bias == pytest.approx(25.1)


def test_learning_rate_zero_nao_altera_bias():
    assert atualizar_bias_quadratico(DADOS, 0.001, 0.2, 30, 0) == 30


def test_um_unico_dado_calculo_manual():
    # previsão = 0 * 10² + 1 * 10 + 0 = 10; contribuição = 2 * (10 - 20) = -20
    # gradiente = -20; novo_bias = 0 - 0.01 * (-20) = 0.2
    novo_bias = atualizar_bias_quadratico([(10, 20)], a=0, peso=1, bias=0, learning_rate=0.01)
    assert novo_bias == pytest.approx(0.2)


def test_cpu_zero_tambem_contribui_para_o_gradiente():
    # previsão = bias = 30; contribuição = 2 * (30 - 40) = -20
    # gradiente = -20; novo_bias = 30 - 0.1 * (-20) = 32
    novo_bias = atualizar_bias_quadratico([(0, 40)], a=0.5, peso=0.2, bias=30, learning_rate=0.1)
    assert novo_bias == pytest.approx(32)


def test_nao_modifica_a_lista_de_dados():
    copia = list(DADOS)
    atualizar_bias_quadratico(DADOS, 0.001, 0.2, 30, 0.000001)
    assert DADOS == copia


def test_lista_vazia_levanta_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        atualizar_bias_quadratico([], a=0.001, peso=0.2, bias=30, learning_rate=0.000001)
