import pytest
# Ajuste os imports se o seu módulo estiver em outro lugar (ex.: src.treinar_modelo_completo).
import src.treinar_modelo_completo as modulo_treino
from src.mse import calcular_mse
from src.treinar_modelo_completo import treinar_modelo_completo

# Dados do exemplo: temperatura = 30 + 0.2 * cpu (peso ideal = 0.2, bias ideal = 30)
DADOS = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50),
]
LR = 0.0001


# ---------- Referência independente (forma fechada para os DADOS acima) ----------
# Com a = peso - 0.2 e b = bias - 30:
#   erro_i = a * cpu_i + b          (média de cpu = 50, média de cpu² = 3750)
#   MSE    = 3750 * a² + 100 * a * b + b²
#   grad_peso = 2 * (3750 * a + 50 * b)
#   grad_bias = 2 * (50 * a + b)

def referencia(peso, bias, learning_rate, epocas):
    def mse(p, b_):
        a, b = p - 0.2, b_ - 30
        return 3750 * a ** 2 + 100 * a * b + b ** 2

    historico = [mse(peso, bias)]
    for _ in range(epocas):
        a, b = peso - 0.2, bias - 30
        novo_peso = peso - learning_rate * 2 * (3750 * a + 50 * b)
        novo_bias = bias - learning_rate * 2 * (50 * a + b)
        peso, bias = novo_peso, novo_bias
        historico.append(mse(peso, bias))
    return peso, bias, historico


# ---------- Testes com as funções reais ----------

def test_exemplo_do_enunciado_uma_epoca():
    peso, bias, historico = treinar_modelo_completo(DADOS, 0.1, 30, LR, 1)
    assert peso == pytest.approx(0.175, abs=1e-10)
    assert bias == pytest.approx(30.001, abs=1e-10)
    assert len(historico) == 2
    assert historico[1] < historico[0]


def test_valores_exatos_uma_epoca():
    _, _, historico = treinar_modelo_completo(DADOS, 0.1, 30, LR, 1)
    # MSE final = 2.34375 - 0.0025 + 0.000001
    assert historico == pytest.approx([37.5, 2.341251], abs=1e-9)


def test_valores_exatos_duas_epocas():
    peso, bias, historico = treinar_modelo_completo(DADOS, 0.1, 30, LR, 2)
    assert peso == pytest.approx(0.19374, abs=1e-10)
    assert bias == pytest.approx(30.0012498, abs=1e-10)
    assert historico == pytest.approx([37.5, 2.341251, 0.1461726872], abs=1e-9)


def test_retorna_tupla_com_peso_bias_e_historico():
    resultado = treinar_modelo_completo(DADOS, 0.1, 30, LR, 3)
    assert isinstance(resultado, tuple)
    assert len(resultado) == 3
    peso, bias, historico = resultado
    assert isinstance(peso, float)
    assert isinstance(bias, float)
    assert isinstance(historico, list)


@pytest.mark.parametrize("epocas", [0, 1, 2, 5, 10])
def test_historico_tem_epocas_mais_um_elementos(epocas):
    _, _, historico = treinar_modelo_completo(DADOS, 0.1, 30, LR, epocas)
    assert len(historico) == epocas + 1


def test_zero_epocas_retorna_valores_iniciais_e_apenas_o_mse_inicial():
    peso, bias, historico = treinar_modelo_completo(DADOS, 0.1, 30, LR, 0)
    assert peso == 0.1
    assert bias == 30
    assert historico == pytest.approx([37.5])


@pytest.mark.parametrize("epocas", [1, 2, 3, 5, 10])
@pytest.mark.parametrize(
    "peso_inicial, bias_inicial",
    [(0.1, 30), (0.3, 30), (0.2, 25), (0.0, 0), (0.5, 40)],
)
def test_bate_com_a_referencia_independente(peso_inicial, bias_inicial, epocas):
    peso, bias, historico = treinar_modelo_completo(
        DADOS, peso_inicial, bias_inicial, LR, epocas
    )
    peso_ref, bias_ref, historico_ref = referencia(peso_inicial, bias_inicial, LR, epocas)
    assert peso == pytest.approx(peso_ref, rel=1e-9, abs=1e-9)
    assert bias == pytest.approx(bias_ref, rel=1e-9, abs=1e-9)
    assert historico == pytest.approx(historico_ref, rel=1e-9, abs=1e-9)


def test_primeiro_elemento_e_o_mse_dos_valores_iniciais():
    _, _, historico = treinar_modelo_completo(DADOS, 0.1, 30, LR, 4)
    assert historico[0] == pytest.approx(calcular_mse(DADOS, 0.1, 30))


def test_ultimo_elemento_e_o_mse_dos_valores_finais():
    peso, bias, historico = treinar_modelo_completo(DADOS, 0.1, 30, LR, 4)
    assert historico[-1] == pytest.approx(calcular_mse(DADOS, peso, bias))


def test_mse_diminui_a_cada_epoca_com_learning_rate_pequeno():
    _, _, historico = treinar_modelo_completo(DADOS, 0.1, 30, LR, 15)
    assert all(proximo < atual for atual, proximo in zip(historico, historico[1:]))


def test_mse_nunca_e_negativo():
    _, _, historico = treinar_modelo_completo(DADOS, 0.1, 30, LR, 15)
    assert all(valor >= 0 for valor in historico)


def test_treino_reduz_o_mse_drasticamente():
    peso, _, historico = treinar_modelo_completo(DADOS, 0.1, 30, LR, 20)
    assert historico[-1] < historico[0] / 1e5
    assert peso == pytest.approx(0.2, abs=1e-3)


def test_peso_e_bias_ideais_permanecem_e_mse_fica_zero():
    peso, bias, historico = treinar_modelo_completo(DADOS, 0.2, 30, LR, 5)
    assert peso == pytest.approx(0.2)
    assert bias == pytest.approx(30)
    assert historico == pytest.approx([0.0] * 6, abs=1e-12)


def test_learning_rate_zero_mantem_tudo_constante():
    peso, bias, historico = treinar_modelo_completo(DADOS, 0.1, 30, 0, 4)
    assert peso == 0.1
    assert bias == 30
    assert historico == pytest.approx([37.5] * 5)


def test_learning_rate_muito_alto_faz_o_mse_crescer():
    _, _, historico = treinar_modelo_completo(DADOS, 0.1, 30, 0.001, 3)
    assert all(proximo > atual for atual, proximo in zip(historico, historico[1:]))


def test_atualizacao_e_simultanea_bias_usa_o_peso_antigo():
    # Se o bias fosse atualizado com o peso JÁ atualizado (0.175), o resultado
    # seria 30.00025 em vez de 30.001.
    _, bias, _ = treinar_modelo_completo(DADOS, 0.1, 30, LR, 1)
    assert bias == pytest.approx(30.001, abs=1e-10)
    assert bias != pytest.approx(30.00025, abs=1e-6)


def test_epocas_negativas_retorna_valores_iniciais():
    peso, bias, historico = treinar_modelo_completo(DADOS, 0.1, 30, LR, -2)
    assert (peso, bias) == (0.1, 30)
    assert len(historico) == 1


def test_nao_modifica_a_lista_de_dados():
    copia = list(DADOS)
    treinar_modelo_completo(DADOS, 0.1, 30, LR, 5)
    assert DADOS == copia


def test_cada_chamada_retorna_um_historico_independente():
    _, _, historico_1 = treinar_modelo_completo(DADOS, 0.1, 30, LR, 2)
    _, _, historico_2 = treinar_modelo_completo(DADOS, 0.1, 30, LR, 2)
    assert historico_1 == historico_2
    assert historico_1 is not historico_2


# ---------- Testes isolados, com as dependências simuladas ----------

@pytest.fixture
def chamadas(monkeypatch):
    registro = {"peso": [], "bias": [], "mse": []}

    def peso_falso(dados, peso, bias, learning_rate):
        registro["peso"].append((dados, peso, bias, learning_rate))
        return peso + 1

    def bias_falso(dados, peso, bias, learning_rate):
        registro["bias"].append((dados, peso, bias, learning_rate))
        return bias + 10

    def mse_falso(dados, peso, bias):
        registro["mse"].append((dados, peso, bias))
        return peso * 100 + bias

    monkeypatch.setattr(modulo_treino, "atualizar_peso", peso_falso)
    monkeypatch.setattr(modulo_treino, "atualizar_bias", bias_falso)
    monkeypatch.setattr(modulo_treino, "calcular_mse", mse_falso)
    return registro


def test_encadeia_valores_e_usa_o_par_antigo_nas_duas_atualizacoes(chamadas):
    peso, bias, historico = treinar_modelo_completo(
        DADOS, peso_inicial=0, bias_inicial=0, learning_rate=0.5, epocas=2
    )

    assert (peso, bias) == (2, 20)
    assert historico == [0, 110, 220]

    # Em cada época, as duas funções recebem o MESMO par (peso, bias) antigo
    esperado = [(DADOS, 0, 0, 0.5), (DADOS, 1, 10, 0.5)]
    assert chamadas["peso"] == esperado
    assert chamadas["bias"] == esperado


def test_calcula_o_mse_com_o_par_inicial_e_depois_de_cada_epoca(chamadas):
    treinar_modelo_completo(DADOS, 0, 0, 0.5, 2)
    assert chamadas["mse"] == [(DADOS, 0, 0), (DADOS, 1, 10), (DADOS, 2, 20)]


def test_zero_epocas_nao_chama_as_atualizacoes(chamadas):
    peso, bias, historico = treinar_modelo_completo(DADOS, 0.1, 30, 0.5, 0)

    assert (peso, bias) == (0.1, 30)
    assert historico == [0.1 * 100 + 30]
    assert chamadas["peso"] == []
    assert chamadas["bias"] == []
    assert chamadas["mse"] == [(DADOS, 0.1, 30)]
