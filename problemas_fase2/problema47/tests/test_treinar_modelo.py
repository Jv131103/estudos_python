import pytest
# Ajuste os imports se o seu módulo estiver em outro lugar (ex.: src.treinar_modelo).
import src.treinar_modelo as modulo_treino
from src.treinar_modelo import treinar_modelo

# Dados do exemplo: temperatura = 30 + 0.2 * cpu (peso ideal = 0.2, bias = 30)
DADOS = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50),
]


# ---------- Testes com atualizar_peso e prever_temperatura reais ----------

@pytest.mark.parametrize(
    "epocas, esperado",
    [
        (1, 0.175),
        (2, 0.19375),
        (3, 0.1984375),
    ],
)
def test_exemplos_do_enunciado(epocas, esperado):
    resultado = treinar_modelo(DADOS, 0.1, 30, 0.0001, epocas)
    assert resultado == pytest.approx(esperado, abs=1e-10)


def test_zero_epocas_retorna_peso_inicial():
    assert treinar_modelo(DADOS, 0.1, 30, 0.0001, 0) == 0.1


@pytest.mark.parametrize("epocas", [1, 2, 3, 5, 10, 20])
def test_formula_fechada_do_exemplo(epocas):
    # Com esses dados e learning_rate, a distância até o peso ideal (0.2)
    # é multiplicada por 0.25 a cada época: peso_n = 0.2 - 0.1 * 0.25**n
    esperado = 0.2 - 0.1 * 0.25 ** epocas
    resultado = treinar_modelo(DADOS, 0.1, 30, 0.0001, epocas)
    assert resultado == pytest.approx(esperado, abs=1e-10)


def test_converge_para_o_peso_ideal():
    resultado = treinar_modelo(DADOS, 0.1, 30, 0.0001, 50)
    assert resultado == pytest.approx(0.2, abs=1e-9)


def test_converge_por_cima_quando_peso_inicial_e_maior_que_o_ideal():
    resultado = treinar_modelo(DADOS, 0.3, 30, 0.0001, 3)
    assert resultado == pytest.approx(0.2 + 0.1 * 0.25 ** 3, abs=1e-10)
    assert resultado > 0.2


def test_erro_diminui_a_cada_epoca():
    erros = [abs(treinar_modelo(DADOS, 0.1, 30, 0.0001, n) - 0.2) for n in range(6)]
    assert all(proximo < atual for atual, proximo in zip(erros, erros[1:]))


def test_peso_ideal_permanece_inalterado():
    assert treinar_modelo(DADOS, 0.2, 30, 0.0001, 10) == pytest.approx(0.2)


def test_learning_rate_zero_nao_altera_peso():
    assert treinar_modelo(DADOS, 0.1, 30, 0, 10) == 0.1


def test_learning_rate_muito_alto_diverge():
    # Com lr = 0.001 o fator por época é 1 - 0.001 * 2 * 3750 = -6.5,
    # então o erro cresce em vez de diminuir.
    resultado = treinar_modelo(DADOS, 0.1, 30, 0.001, 3)
    assert abs(resultado - 0.2) > abs(0.1 - 0.2)


def test_treinar_em_etapas_equivale_a_treinar_de_uma_vez():
    de_uma_vez = treinar_modelo(DADOS, 0.1, 30, 0.0001, 5)
    etapa_1 = treinar_modelo(DADOS, 0.1, 30, 0.0001, 2)
    etapa_2 = treinar_modelo(DADOS, etapa_1, 30, 0.0001, 3)
    assert etapa_2 == pytest.approx(de_uma_vez)


def test_nao_modifica_a_lista_de_dados():
    copia = list(DADOS)
    treinar_modelo(DADOS, 0.1, 30, 0.0001, 5)
    assert DADOS == copia


def test_epocas_negativas_retorna_peso_inicial():
    # range(negativo) é vazio: nenhuma atualização acontece
    assert treinar_modelo(DADOS, 0.1, 30, 0.0001, -3) == 0.1


def test_dados_vazios_com_epocas_levanta_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        treinar_modelo([], 0.1, 30, 0.0001, 1)


def test_dados_vazios_sem_epocas_nao_levanta_erro():
    assert treinar_modelo([], 0.1, 30, 0.0001, 0) == 0.1


# ---------- Testes isolados, com atualizar_peso simulada ----------

def test_chama_atualizar_peso_uma_vez_por_epoca_encadeando_o_peso(monkeypatch):
    chamadas = []

    def atualizar_falsa(dados, peso, bias, learning_rate):
        chamadas.append((dados, peso, bias, learning_rate))
        return peso + 1

    monkeypatch.setattr(modulo_treino, "atualizar_peso", atualizar_falsa)

    resultado = treinar_modelo(DADOS, peso_inicial=0, bias=30, learning_rate=0.5, epocas=3)

    assert resultado == 3
    assert chamadas == [
        (DADOS, 0, 30, 0.5),
        (DADOS, 1, 30, 0.5),
        (DADOS, 2, 30, 0.5),
    ]


def test_zero_epocas_nao_chama_atualizar_peso(monkeypatch):
    def nao_deve_ser_chamada(*args, **kwargs):
        raise AssertionError("atualizar_peso não deveria ser chamada")

    monkeypatch.setattr(modulo_treino, "atualizar_peso", nao_deve_ser_chamada)

    assert treinar_modelo(DADOS, 0.1, 30, 0.0001, 0) == 0.1
