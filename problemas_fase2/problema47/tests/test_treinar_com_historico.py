import pytest
import src.treinar_com_historico as modulo_treino
from src.mse import calcular_mse
from src.treinar_com_historico import treinar_com_historico

# Dados do exemplo: temperatura = 30 + 0.2 * cpu (peso ideal = 0.2, bias = 30)
DADOS = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50),
]


# ---------- Testes com atualizar_peso e calcular_mse reais ----------

def test_exemplo_do_enunciado():
    peso_final, historico = treinar_com_historico(
        DADOS, peso_inicial=0.1, bias=30, learning_rate=0.0001, epocas=3
    )
    assert peso_final == pytest.approx(0.1984375, abs=1e-10)
    assert historico == pytest.approx(
        [37.5, 2.34375, 0.146484375, 0.0091552734375], abs=1e-10
    )


def test_retorna_tupla_com_peso_e_lista():
    resultado = treinar_com_historico(DADOS, 0.1, 30, 0.0001, 3)
    assert isinstance(resultado, tuple)
    assert len(resultado) == 2
    peso, historico = resultado
    assert isinstance(peso, float)
    assert isinstance(historico, list)


@pytest.mark.parametrize("epocas", [0, 1, 2, 5, 10])
def test_historico_tem_epocas_mais_um_elementos(epocas):
    _, historico = treinar_com_historico(DADOS, 0.1, 30, 0.0001, epocas)
    assert len(historico) == epocas + 1


def test_zero_epocas_retorna_peso_inicial_e_apenas_o_mse_inicial():
    peso_final, historico = treinar_com_historico(DADOS, 0.1, 30, 0.0001, 0)
    assert peso_final == 0.1
    assert historico == pytest.approx([37.5])


def test_primeiro_elemento_e_o_mse_do_peso_inicial():
    _, historico = treinar_com_historico(DADOS, 0.1, 30, 0.0001, 4)
    assert historico[0] == pytest.approx(calcular_mse(DADOS, 0.1, 30))


def test_ultimo_elemento_e_o_mse_do_peso_final():
    peso_final, historico = treinar_com_historico(DADOS, 0.1, 30, 0.0001, 4)
    assert historico[-1] == pytest.approx(calcular_mse(DADOS, peso_final, 30))


@pytest.mark.parametrize("epocas", [1, 2, 3, 5, 8])
def test_formula_fechada_do_historico(epocas):
    # O erro (distância até 0.2) é multiplicado por 0.25 a cada época,
    # então o MSE (proporcional ao erro²) é dividido por 16: 37.5 / 16**i
    _, historico = treinar_com_historico(DADOS, 0.1, 30, 0.0001, epocas)
    esperado = [37.5 / 16 ** i for i in range(epocas + 1)]
    assert historico == pytest.approx(esperado, abs=1e-10)


def test_peso_final_segue_a_formula_fechada():
    peso_final, _ = treinar_com_historico(DADOS, 0.1, 30, 0.0001, 6)
    assert peso_final == pytest.approx(0.2 - 0.1 * 0.25 ** 6, abs=1e-10)


def test_mse_diminui_a_cada_epoca_quando_o_treino_converge():
    _, historico = treinar_com_historico(DADOS, 0.1, 30, 0.0001, 10)
    assert all(proximo < atual for atual, proximo in zip(historico, historico[1:]))


def test_mse_nunca_e_negativo():
    _, historico = treinar_com_historico(DADOS, 0.1, 30, 0.0001, 10)
    assert all(valor >= 0 for valor in historico)


def test_peso_ideal_mantem_mse_zero_em_todas_as_epocas():
    peso_final, historico = treinar_com_historico(DADOS, 0.2, 30, 0.0001, 5)
    assert peso_final == pytest.approx(0.2)
    assert historico == pytest.approx([0.0] * 6, abs=1e-12)


def test_learning_rate_zero_mantem_peso_e_historico_constante():
    peso_final, historico = treinar_com_historico(DADOS, 0.1, 30, 0, 4)
    assert peso_final == 0.1
    assert historico == pytest.approx([37.5] * 5)


def test_learning_rate_muito_alto_faz_o_mse_crescer():
    # Com lr = 0.001 o fator por época é -6.5: o treino diverge
    _, historico = treinar_com_historico(DADOS, 0.1, 30, 0.001, 3)
    assert all(proximo > atual for atual, proximo in zip(historico, historico[1:]))


def test_peso_inicial_acima_do_ideal_tambem_converge():
    peso_final, historico = treinar_com_historico(DADOS, 0.3, 30, 0.0001, 3)
    assert peso_final == pytest.approx(0.2 + 0.1 * 0.25 ** 3, abs=1e-10)
    assert historico == pytest.approx([37.5, 2.34375, 0.146484375, 0.0091552734375], abs=1e-10)


def test_epocas_negativas_retorna_peso_inicial_e_historico_unitario():
    peso_final, historico = treinar_com_historico(DADOS, 0.1, 30, 0.0001, -2)
    assert peso_final == 0.1
    assert len(historico) == 1


def test_nao_modifica_a_lista_de_dados():
    copia = list(DADOS)
    treinar_com_historico(DADOS, 0.1, 30, 0.0001, 5)
    assert DADOS == copia


def test_cada_chamada_retorna_um_historico_independente():
    _, historico_1 = treinar_com_historico(DADOS, 0.1, 30, 0.0001, 2)
    _, historico_2 = treinar_com_historico(DADOS, 0.1, 30, 0.0001, 2)
    assert historico_1 == historico_2
    assert historico_1 is not historico_2


# ---------- Testes isolados, com atualizar_peso e calcular_mse simuladas ----------

def test_ordem_e_argumentos_das_chamadas(monkeypatch):
    eventos = []

    def atualizar_falsa(dados, peso, bias, learning_rate):
        eventos.append(("atualizar", dados, peso, bias, learning_rate))
        return peso + 1

    def mse_falso(dados, peso, bias):
        eventos.append(("mse", dados, peso, bias))
        return peso * 10

    monkeypatch.setattr(modulo_treino, "atualizar_peso", atualizar_falsa)
    monkeypatch.setattr(modulo_treino, "calcular_mse", mse_falso)

    peso_final, historico = treinar_com_historico(
        DADOS, peso_inicial=0, bias=30, learning_rate=0.5, epocas=3
    )

    assert peso_final == 3
    assert historico == [0, 10, 20, 30]
    assert eventos == [
        ("mse", DADOS, 0, 30),             # MSE inicial, antes de treinar
        ("atualizar", DADOS, 0, 30, 0.5),
        ("mse", DADOS, 1, 30),
        ("atualizar", DADOS, 1, 30, 0.5),
        ("mse", DADOS, 2, 30),
        ("atualizar", DADOS, 2, 30, 0.5),
        ("mse", DADOS, 3, 30),
    ]


def test_zero_epocas_calcula_mse_uma_vez_e_nao_atualiza_peso(monkeypatch):
    chamadas_mse = []

    def nao_deve_ser_chamada(*args, **kwargs):
        raise AssertionError("atualizar_peso não deveria ser chamada")

    def mse_falso(dados, peso, bias):
        chamadas_mse.append((dados, peso, bias))
        return 99

    monkeypatch.setattr(modulo_treino, "atualizar_peso", nao_deve_ser_chamada)
    monkeypatch.setattr(modulo_treino, "calcular_mse", mse_falso)

    peso_final, historico = treinar_com_historico(DADOS, 0.1, 30, 0.0001, 0)

    assert peso_final == 0.1
    assert historico == [99]
    assert chamadas_mse == [(DADOS, 0.1, 30)]
