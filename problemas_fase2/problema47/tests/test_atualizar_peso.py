import pytest
import src.atualizar_peso
from src.atualizar_peso import atualizar_peso

# Dados do exemplo: temperatura = 30 + 0.2 * cpu (peso ideal = 0.2, bias = 30)
DADOS = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50),
]


# ---------- Testes com a prever_temperatura real (assume peso * cpu + bias) ----------

def test_exemplo_do_enunciado():
    novo_peso = atualizar_peso(DADOS, peso=0.1, bias=30, learning_rate=0.0001)
    assert novo_peso == pytest.approx(0.175, abs=1e-10)


def test_peso_ideal_nao_muda():
    # Previsões perfeitas -> gradiente zero -> peso permanece igual
    novo_peso = atualizar_peso(DADOS, peso=0.2, bias=30, learning_rate=0.01)
    assert novo_peso == pytest.approx(0.2)


def test_peso_abaixo_do_ideal_aumenta():
    novo_peso = atualizar_peso(DADOS, peso=0.1, bias=30, learning_rate=0.0001)
    assert novo_peso > 0.1


def test_peso_acima_do_ideal_diminui():
    novo_peso = atualizar_peso(DADOS, peso=0.3, bias=30, learning_rate=0.0001)
    assert novo_peso < 0.3


def test_learning_rate_zero_nao_altera_peso():
    novo_peso = atualizar_peso(DADOS, peso=0.1, bias=30, learning_rate=0)
    assert novo_peso == 0.1


def test_learning_rate_maior_gera_passo_proporcionalmente_maior():
    passo_pequeno = atualizar_peso(DADOS, 0.1, 30, 0.0001) - 0.1
    passo_grande = atualizar_peso(DADOS, 0.1, 30, 0.0002) - 0.1
    assert passo_grande == pytest.approx(2 * passo_pequeno)


def test_um_unico_dado_calculo_manual():
    # previsão = 1 * 10 + 0 = 10; contribuição = 2 * 10 * (10 - 20) = -200
    # gradiente = -200; novo_peso = 1 - 0.01 * (-200) = 3
    novo_peso = atualizar_peso([(10, 20)], peso=1, bias=0, learning_rate=0.01)
    assert novo_peso == pytest.approx(3.0)


def test_cpu_zero_nao_contribui_para_o_gradiente():
    # Com cpu = 0 a contribuição é sempre 0, mesmo com erro grande
    novo_peso = atualizar_peso([(0, 100)], peso=0.5, bias=30, learning_rate=0.1)
    assert novo_peso == pytest.approx(0.5)


def test_duplicar_os_dados_nao_muda_o_resultado():
    # O gradiente é uma média, então repetir os dados não deve alterá-lo
    uma_vez = atualizar_peso(DADOS, 0.1, 30, 0.0001)
    duas_vezes = atualizar_peso(DADOS * 2, 0.1, 30, 0.0001)
    assert duas_vezes == pytest.approx(uma_vez)


def test_ordem_dos_dados_nao_importa():
    normal = atualizar_peso(DADOS, 0.1, 30, 0.0001)
    invertido = atualizar_peso(list(reversed(DADOS)), 0.1, 30, 0.0001)
    assert invertido == pytest.approx(normal)


def test_nao_modifica_a_lista_de_dados():
    copia = list(DADOS)
    atualizar_peso(DADOS, 0.1, 30, 0.0001)
    assert DADOS == copia


def test_lista_vazia_levanta_zero_division_error():
    # Comportamento atual: divisão por len(dados) == 0
    with pytest.raises(ZeroDivisionError):
        atualizar_peso([], peso=0.1, bias=30, learning_rate=0.0001)


# ---------- Teste isolado (unitário puro), com prever_temperatura simulada ----------

def test_usa_prever_temperatura_com_os_argumentos_corretos(monkeypatch):
    chamadas = []

    def previsao_falsa(cpu, peso, bias):
        chamadas.append((cpu, peso, bias))
        return 10

    monkeypatch.setattr(src.atualizar_peso, "prever_temperatura", previsao_falsa)

    novo_peso = atualizar_peso([(2, 4)], peso=1, bias=5, learning_rate=0.5)

    # contribuição = 2 * 2 * (10 - 4) = 24; gradiente = 24
    # novo_peso = 1 - 0.5 * 24 = -11
    assert chamadas == [(2, 1, 5)]
    assert novo_peso == pytest.approx(-11)
