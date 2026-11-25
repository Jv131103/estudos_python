import pytest
from src.atualizar_peso_quadratico import atualizar_peso_quadratico

# Dados do exemplo: temperatura = 30 + 0.2 * cpu (peso ideal = 0.2, bias ideal = 30, a ideal = 0)
DADOS = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50),
]


def test_exemplo_do_enunciado():
    novo_peso = atualizar_peso_quadratico(
        DADOS, a=0.001, peso=0.2, bias=30, learning_rate=0.000001
    )
    assert novo_peso == pytest.approx(0.199375, abs=1e-10)


def test_parametros_ideais_nao_mudam_o_peso():
    # Previsões perfeitas -> gradiente zero
    novo_peso = atualizar_peso_quadratico(DADOS, a=0, peso=0.2, bias=30, learning_rate=0.01)
    assert novo_peso == pytest.approx(0.2)


def test_com_a_zero_equivale_ao_modelo_linear():
    # Mesmo resultado do exemplo de atualizar_peso (modelo linear)
    novo_peso = atualizar_peso_quadratico(DADOS, a=0, peso=0.1, bias=30, learning_rate=0.0001)
    assert novo_peso == pytest.approx(0.175, abs=1e-10)


def test_peso_acima_do_ideal_diminui():
    novo_peso = atualizar_peso_quadratico(DADOS, a=0, peso=0.3, bias=30, learning_rate=0.0001)
    assert novo_peso < 0.3


def test_peso_abaixo_do_ideal_aumenta():
    novo_peso = atualizar_peso_quadratico(DADOS, a=0, peso=0.1, bias=30, learning_rate=0.0001)
    assert novo_peso > 0.1


def test_learning_rate_zero_nao_altera_peso():
    assert atualizar_peso_quadratico(DADOS, 0.001, 0.2, 30, 0) == 0.2


def test_um_unico_dado_calculo_manual():
    # previsão = 0 * 10² + 1 * 10 + 0 = 10; contribuição = 2 * 10 * (10 - 20) = -200
    # gradiente = -200; novo_peso = 1 - 0.001 * (-200) = 1.2
    novo_peso = atualizar_peso_quadratico([(10, 20)], a=0, peso=1, bias=0, learning_rate=0.001)
    assert novo_peso == pytest.approx(1.2)


def test_cpu_zero_nao_contribui_para_o_gradiente():
    novo_peso = atualizar_peso_quadratico([(0, 100)], a=0.001, peso=0.5, bias=30, learning_rate=0.1)
    assert novo_peso == pytest.approx(0.5)


def test_nao_modifica_a_lista_de_dados():
    copia = list(DADOS)
    atualizar_peso_quadratico(DADOS, 0.001, 0.2, 30, 0.000001)
    assert DADOS == copia


def test_lista_vazia_levanta_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        atualizar_peso_quadratico([], a=0.001, peso=0.2, bias=30, learning_rate=0.000001)
