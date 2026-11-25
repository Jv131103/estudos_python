import pytest
# Ajuste os imports se o seu módulo estiver em outro lugar (ex.: src.treinar_modelo_quadratico).
import src.treinar_modelo_quadratico as modulo_treino
from src.treinar_modelo_quadratico import treinar_modelo_quadratico

# Dados do exemplo: temperatura = 30 + 0.2 * cpu (linear; a ideal = 0, peso ideal = 0.2, bias ideal = 30)
DADOS = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50),
]
LR = 0.00000001


# ---------- Referência independente (forma fechada para os DADOS acima) ----------
# Com A = a, B = peso - 0.2 e C = bias - 30, o erro de cada ponto é A*cpu² + B*cpu + C.
# Momentos de cpu: m1 = 50, m2 = 3750, m3 = 312500, m4 = 27656250.

M1, M2, M3, M4 = 50, 3750, 312_500, 27_656_250


def mse_ref(a, peso, bias):
    A, B, C = a, peso - 0.2, bias - 30
    return A**2 * M4 + B**2 * M2 + C**2 + 2 * A * B * M3 + 2 * A * C * M2 + 2 * B * C * M1


def referencia(a, peso, bias, learning_rate, epocas):
    historico = [mse_ref(a, peso, bias)]
    for _ in range(epocas):
        A, B, C = a, peso - 0.2, bias - 30
        grad_a = 2 * (A * M4 + B * M3 + C * M2)
        grad_peso = 2 * (A * M3 + B * M2 + C * M1)
        grad_bias = 2 * (A * M2 + B * M1 + C)
        a, peso, bias = (
            a - learning_rate * grad_a,
            peso - learning_rate * grad_peso,
            bias - learning_rate * grad_bias,
        )
        historico.append(mse_ref(a, peso, bias))
    return a, peso, bias, historico


# ---------- Testes com as funções reais ----------

def test_exemplo_do_enunciado_uma_epoca():
    a, peso, bias, historico = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 1)
    assert a == pytest.approx(0.000446875, abs=1e-12)
    assert peso == pytest.approx(0.19999375, abs=1e-12)
    assert bias == pytest.approx(29.999999925, abs=1e-10)
    assert len(historico) == 2
    assert historico[0] == pytest.approx(27.65625, abs=1e-10)
    assert historico[1] < historico[0]


def test_valor_exato_do_mse_apos_uma_epoca():
    _, _, _, historico = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 1)
    assert historico[1] == pytest.approx(5.521131792, abs=1e-8)


def test_retorna_tupla_com_a_peso_bias_e_historico():
    resultado = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 3)
    assert isinstance(resultado, tuple)
    assert len(resultado) == 4
    a, peso, bias, historico = resultado
    assert isinstance(a, float)
    assert isinstance(peso, float)
    assert isinstance(bias, float)
    assert isinstance(historico, list)


@pytest.mark.parametrize("epocas", [0, 1, 2, 5, 10])
def test_historico_tem_epocas_mais_um_elementos(epocas):
    *_, historico = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, epocas)
    assert len(historico) == epocas + 1


def test_zero_epocas_retorna_valores_iniciais_e_apenas_o_mse_inicial():
    a, peso, bias, historico = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 0)
    assert (a, peso, bias) == (0.001, 0.2, 30)
    assert historico == pytest.approx([27.65625])


@pytest.mark.parametrize("epocas", [1, 2, 3, 5, 10])
@pytest.mark.parametrize(
    "a_inicial, peso_inicial, bias_inicial",
    [
        (0.001, 0.2, 30),
        (-0.001, 0.2, 30),
        (0.0005, 0.25, 29),
        (0.0, 0.1, 30),
        (0.001, 0.2, 31),
    ],
)
def test_bate_com_a_referencia_independente(a_inicial, peso_inicial, bias_inicial, epocas):
    a, peso, bias, historico = treinar_modelo_quadratico(
        DADOS, a_inicial, peso_inicial, bias_inicial, LR, epocas
    )
    a_ref, peso_ref, bias_ref, historico_ref = referencia(
        a_inicial, peso_inicial, bias_inicial, LR, epocas
    )
    assert a == pytest.approx(a_ref, rel=1e-6, abs=1e-12)
    assert peso == pytest.approx(peso_ref, rel=1e-6, abs=1e-12)
    assert bias == pytest.approx(bias_ref, rel=1e-6, abs=1e-12)
    assert historico == pytest.approx(historico_ref, rel=1e-6, abs=1e-9)


def test_primeiro_elemento_e_o_mse_dos_valores_iniciais():
    *_, historico = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 4)
    assert historico[0] == pytest.approx(modulo_treino.calcular_mse_quadratico(DADOS, 0.001, 0.2, 30))


def test_ultimo_elemento_e_o_mse_dos_valores_finais():
    a, peso, bias, historico = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 4)
    assert historico[-1] == pytest.approx(modulo_treino.calcular_mse_quadratico(DADOS, a, peso, bias))


def test_mse_diminui_a_cada_epoca_com_learning_rate_pequeno():
    *_, historico = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 10)
    assert all(proximo < atual for atual, proximo in zip(historico, historico[1:]))


def test_mse_nunca_e_negativo():
    *_, historico = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 10)
    assert all(valor >= 0 for valor in historico)


def test_treino_reduz_o_mse_drasticamente_e_a_se_aproxima_de_zero():
    a, _, _, historico = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 10)
    assert historico[-1] < historico[0] / 1e4
    assert abs(a) < 1e-6   # dados são lineares: o termo quadrático ideal é 0


def test_parametros_ideais_permanecem_e_mse_fica_zero():
    a, peso, bias, historico = treinar_modelo_quadratico(DADOS, 0, 0.2, 30, LR, 5)
    assert a == pytest.approx(0, abs=1e-12)
    assert peso == pytest.approx(0.2)
    assert bias == pytest.approx(30)
    assert historico == pytest.approx([0.0] * 6, abs=1e-9)


def test_learning_rate_zero_mantem_tudo_constante():
    a, peso, bias, historico = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, 0, 4)
    assert (a, peso, bias) == (0.001, 0.2, 30)
    assert historico == pytest.approx([27.65625] * 5)


def test_learning_rate_muito_alto_faz_o_mse_crescer():
    *_, historico = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, 0.0000001, 3)
    assert all(proximo > atual for atual, proximo in zip(historico, historico[1:]))


def test_atualizacao_e_simultanea_peso_e_bias_usam_o_a_antigo():
    # Se o peso fosse atualizado com o `a` já atualizado (0.000446875),
    # o resultado seria ~0.19999721 em vez de 0.19999375.
    _, peso, bias, _ = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 1)
    assert peso == pytest.approx(0.19999375, abs=1e-12)
    assert peso != pytest.approx(0.19999721, abs=1e-9)
    assert bias == pytest.approx(29.999999925, abs=1e-10)


def test_treinar_em_etapas_equivale_a_treinar_de_uma_vez():
    de_uma_vez = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 5)
    a, peso, bias, _ = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 2)
    a, peso, bias, _ = treinar_modelo_quadratico(DADOS, a, peso, bias, LR, 3)
    assert (a, peso, bias) == pytest.approx(de_uma_vez[:3])


def test_epocas_negativas_retornam_valores_iniciais():
    a, peso, bias, historico = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, -2)
    assert (a, peso, bias) == (0.001, 0.2, 30)
    assert len(historico) == 1


def test_nao_modifica_a_lista_de_dados():
    copia = list(DADOS)
    treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 5)
    assert DADOS == copia


def test_cada_chamada_retorna_um_historico_independente():
    *_, historico_1 = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 2)
    *_, historico_2 = treinar_modelo_quadratico(DADOS, 0.001, 0.2, 30, LR, 2)
    assert historico_1 == historico_2
    assert historico_1 is not historico_2


@pytest.mark.parametrize("epocas", [0, 3])
def test_dados_vazios_levantam_value_error(epocas):
    # O MSE inicial já é calculado antes do laço, então falha mesmo com 0 épocas
    with pytest.raises(ValueError):
        treinar_modelo_quadratico([], 0.001, 0.2, 30, LR, epocas)


# ---------- Testes isolados, com as dependências simuladas ----------

@pytest.fixture
def chamadas(monkeypatch):
    registro = {"a": [], "peso": [], "bias": [], "mse": []}

    def a_falso(dados, a, peso, bias, learning_rate):
        registro["a"].append((dados, a, peso, bias, learning_rate))
        return a + 1

    def peso_falso(dados, a, peso, bias, learning_rate):
        registro["peso"].append((dados, a, peso, bias, learning_rate))
        return peso + 10

    def bias_falso(dados, a, peso, bias, learning_rate):
        registro["bias"].append((dados, a, peso, bias, learning_rate))
        return bias + 100

    def mse_falso(dados, a, peso, bias):
        registro["mse"].append((dados, a, peso, bias))
        return a * 1_000_000 + peso * 1_000 + bias

    monkeypatch.setattr(modulo_treino, "atualizar_a", a_falso)
    monkeypatch.setattr(modulo_treino, "atualizar_peso_quadratico", peso_falso)
    monkeypatch.setattr(modulo_treino, "atualizar_bias_quadratico", bias_falso)
    monkeypatch.setattr(modulo_treino, "calcular_mse_quadratico", mse_falso)
    return registro


def test_encadeia_valores_e_usa_o_trio_antigo_nas_tres_atualizacoes(chamadas):
    a, peso, bias, historico = treinar_modelo_quadratico(
        DADOS, a_inicial=0, peso_inicial=0, bias_inicial=0, learning_rate=0.5, epocas=2
    )

    assert (a, peso, bias) == (2, 20, 200)
    assert historico == [0, 1_010_100, 2_020_200]

    # Em cada época, as três funções recebem o MESMO trio (a, peso, bias) antigo
    esperado = [(DADOS, 0, 0, 0, 0.5), (DADOS, 1, 10, 100, 0.5)]
    assert chamadas["a"] == esperado
    assert chamadas["peso"] == esperado
    assert chamadas["bias"] == esperado


def test_calcula_o_mse_com_o_trio_inicial_e_depois_de_cada_epoca(chamadas):
    treinar_modelo_quadratico(DADOS, 0, 0, 0, 0.5, 2)
    assert chamadas["mse"] == [
        (DADOS, 0, 0, 0),
        (DADOS, 1, 10, 100),
        (DADOS, 2, 20, 200),
    ]


def test_zero_epocas_nao_chama_as_atualizacoes(chamadas):
    a, peso, bias, historico = treinar_modelo_quadratico(DADOS, 1, 2, 3, 0.5, 0)

    assert (a, peso, bias) == (1, 2, 3)
    assert historico == [1_000_000 + 2_000 + 3]
    assert chamadas["a"] == []
    assert chamadas["peso"] == []
    assert chamadas["bias"] == []
    assert chamadas["mse"] == [(DADOS, 1, 2, 3)]
