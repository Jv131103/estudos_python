# Ajuste os imports se o seu módulo estiver em outro lugar (ex.: src.atualizar_bias).
import pytest
import src.atualizar_bias as modulo_bias
from src.atualizar_bias import atualizar_bias

# Dados do exemplo: temperatura = 30 + 0.2 * cpu (peso ideal = 0.2, bias ideal = 30)
DADOS = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50),
]


# ---------- Testes com a prever_temperatura real (assume peso * cpu + bias) ----------

def test_exemplo_do_enunciado():
    novo_bias = atualizar_bias(DADOS, peso=0.1, bias=30, learning_rate=0.0001)
    assert novo_bias == pytest.approx(30.001, abs=1e-10)


def test_peso_e_bias_ideais_nao_mudam_o_bias():
    # Previsões perfeitas -> gradiente zero
    novo_bias = atualizar_bias(DADOS, peso=0.2, bias=30, learning_rate=0.01)
    assert novo_bias == pytest.approx(30)


def test_bias_abaixo_do_ideal_aumenta():
    # peso ideal; erro médio = -5, gradiente = -10; novo = 25 + 0.01 * 10
    novo_bias = atualizar_bias(DADOS, peso=0.2, bias=25, learning_rate=0.01)
    assert novo_bias == pytest.approx(25.1)


def test_bias_acima_do_ideal_diminui():
    # peso ideal; erro médio = +5, gradiente = +10; novo = 35 - 0.01 * 10
    novo_bias = atualizar_bias(DADOS, peso=0.2, bias=35, learning_rate=0.01)
    assert novo_bias == pytest.approx(34.9)


@pytest.mark.parametrize(
    "peso, bias, learning_rate",
    [
        (0.1, 30, 0.0001),
        (0.2, 25, 0.01),
        (0.5, 10, 0.001),
        (0.0, 0, 0.1),
        (-0.3, 40, 0.0005),
    ],
)
def test_formula_fechada(peso, bias, learning_rate):
    # erro_i = (peso - 0.2) * cpu_i + (bias - 30); média de cpu = 50
    # gradiente = 2 * erro_médio = 2 * (50 * (peso - 0.2) + (bias - 30))
    gradiente = 2 * (50 * (peso - 0.2) + (bias - 30))
    esperado = bias - learning_rate * gradiente
    assert atualizar_bias(DADOS, peso, bias, learning_rate) == pytest.approx(esperado)


def test_learning_rate_zero_nao_altera_bias():
    assert atualizar_bias(DADOS, 0.1, 30, 0) == 30


def test_learning_rate_maior_gera_passo_proporcionalmente_maior():
    passo_pequeno = atualizar_bias(DADOS, 0.1, 30, 0.0001) - 30
    passo_grande = atualizar_bias(DADOS, 0.1, 30, 0.0002) - 30
    assert passo_grande == pytest.approx(2 * passo_pequeno)


def test_um_unico_dado_calculo_manual():
    # previsão = 1 * 10 + 0 = 10; contribuição = 2 * (10 - 20) = -20
    # gradiente = -20; novo_bias = 0 - 0.01 * (-20) = 0.2
    novo_bias = atualizar_bias([(10, 20)], peso=1, bias=0, learning_rate=0.01)
    assert novo_bias == pytest.approx(0.2)


def test_com_peso_zero_o_valor_de_cpu_e_irrelevante():
    # previsão = bias para qualquer cpu: contribuição = 2 * (30 - 40) = -20
    # gradiente = -20; novo_bias = 30 + 0.1 * 20 = 32
    dados = [(5, 40), (500, 40)]
    novo_bias = atualizar_bias(dados, peso=0, bias=30, learning_rate=0.1)
    assert novo_bias == pytest.approx(32)


def test_erros_positivos_e_negativos_se_cancelam():
    # previsões = 40; erros +5 e -5 somam zero
    dados = [(0, 35), (0, 45)]
    novo_bias = atualizar_bias(dados, peso=0, bias=40, learning_rate=0.1)
    assert novo_bias == pytest.approx(40)


@pytest.mark.parametrize("learning_rate", [0.01, 0.1, 0.25])
def test_distancia_ate_o_bias_ideal_e_multiplicada_por_1_menos_2_lr(learning_rate):
    # Com peso ideal: gradiente = 2 * (bias - 30), logo
    # (novo_bias - 30) = (bias - 30) * (1 - 2 * lr)
    bias = 20
    novo_bias = atualizar_bias(DADOS, peso=0.2, bias=bias, learning_rate=learning_rate)
    assert novo_bias - 30 == pytest.approx((bias - 30) * (1 - 2 * learning_rate))


def test_duplicar_os_dados_nao_muda_o_resultado():
    # O gradiente é uma média, então repetir os dados não deve alterá-lo
    uma_vez = atualizar_bias(DADOS, 0.1, 30, 0.0001)
    duas_vezes = atualizar_bias(DADOS * 2, 0.1, 30, 0.0001)
    assert duas_vezes == pytest.approx(uma_vez)


def test_ordem_dos_dados_nao_importa():
    normal = atualizar_bias(DADOS, 0.1, 30, 0.0001)
    invertido = atualizar_bias(list(reversed(DADOS)), 0.1, 30, 0.0001)
    assert invertido == pytest.approx(normal)


def test_nao_modifica_a_lista_de_dados():
    copia = list(DADOS)
    atualizar_bias(DADOS, 0.1, 30, 0.0001)
    assert DADOS == copia


def test_lista_vazia_levanta_zero_division_error():
    # Comportamento atual: divisão por len(dados) == 0
    with pytest.raises(ZeroDivisionError):
        atualizar_bias([], peso=0.1, bias=30, learning_rate=0.0001)


# ---------- Teste isolado (unitário puro), com prever_temperatura simulada ----------

def test_usa_prever_temperatura_com_os_argumentos_corretos(monkeypatch):
    chamadas = []

    def previsao_falsa(cpu, peso, bias):
        chamadas.append((cpu, peso, bias))
        return 10

    monkeypatch.setattr(modulo_bias, "prever_temperatura", previsao_falsa)

    novo_bias = atualizar_bias([(2, 4), (3, 8)], peso=7, bias=1, learning_rate=0.5)

    # contribuições: 2 * (10 - 4) = 12 e 2 * (10 - 8) = 4; soma = 16
    # gradiente = 16 / 2 = 8; novo_bias = 1 - 0.5 * 8 = -3
    assert chamadas == [(2, 7, 1), (3, 7, 1)]
    assert novo_bias == pytest.approx(-3)
