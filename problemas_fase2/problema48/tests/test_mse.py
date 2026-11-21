# Ajuste os imports se o seu módulo estiver em outro lugar (ex.: src.calcular_mse_quadratico).
import pytest
import src.mse as modulo_mse
from src.mse import calcular_mse_quadratico

# Dados do exemplo: temperatura = 30 + 0.2 * cpu (linear; peso ideal = 0.2, bias ideal = 30)
DADOS = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50),
]

# Com peso e bias ideais, o erro de cada ponto é -a * cpu², então
# MSE = a² * média(cpu⁴) = a² * 27_656_250 para os DADOS acima.
MEDIA_CPU_4 = 27_656_250


# ---------- Exemplos do enunciado ----------

def test_modelo_perfeito_tem_mse_zero():
    assert calcular_mse_quadratico(DADOS, 0, 0.2, 30) == pytest.approx(0, abs=1e-10)


def test_termo_quadratico_gera_mse_esperado():
    resultado = calcular_mse_quadratico(DADOS, 0.001, 0.2, 30)
    assert resultado == pytest.approx(27.65625, abs=1e-10)


# ---------- Cálculos à mão ----------

def test_um_unico_ponto_modelo_linear():
    # previsão = 1 * 10 + 0 = 10; erro = (20 - 10)² = 100
    assert calcular_mse_quadratico([(10, 20)], 0, 1, 0) == pytest.approx(100)


def test_um_unico_ponto_com_termo_quadratico():
    # previsão = 1 * 10² = 100; erro = (60 - 100)² = 1600
    assert calcular_mse_quadratico([(10, 60)], 1, 0, 0) == pytest.approx(1600)


def test_media_de_dois_pontos():
    # previsões = 30 e 30; erros² = 0 e 100; média = 50
    dados = [(0, 30), (10, 40)]
    assert calcular_mse_quadratico(dados, 0, 0, 30) == pytest.approx(50)


def test_bias_errado_gera_erro_constante():
    # Peso ideal, bias 5 acima do ideal: erro = -5 em todos os pontos -> MSE = 25
    assert calcular_mse_quadratico(DADOS, 0, 0.2, 35) == pytest.approx(25)


@pytest.mark.parametrize("a", [0, 0.001, 0.002, -0.001, 0.01, -0.02])
def test_formula_fechada_com_peso_e_bias_ideais(a):
    esperado = a ** 2 * MEDIA_CPU_4
    assert calcular_mse_quadratico(DADOS, a, 0.2, 30) == pytest.approx(esperado, abs=1e-9)


# ---------- Propriedades ----------

def test_mse_nunca_e_negativo():
    for a, peso, bias in [(0, 0, 0), (0.001, 0.2, 30), (-1, 5, -20), (0.5, -3, 100)]:
        assert calcular_mse_quadratico(DADOS, a, peso, bias) >= 0


def test_sinal_de_a_nao_importa_com_peso_e_bias_ideais():
    positivo = calcular_mse_quadratico(DADOS, 0.001, 0.2, 30)
    negativo = calcular_mse_quadratico(DADOS, -0.001, 0.2, 30)
    assert positivo == pytest.approx(negativo)


def test_mse_cresce_com_o_modulo_de_a():
    mses = [calcular_mse_quadratico(DADOS, a, 0.2, 30) for a in (0, 0.001, 0.002, 0.003)]
    assert all(proximo > atual for atual, proximo in zip(mses, mses[1:]))


def test_dobrar_a_quadruplica_o_mse():
    mse_1 = calcular_mse_quadratico(DADOS, 0.001, 0.2, 30)
    mse_2 = calcular_mse_quadratico(DADOS, 0.002, 0.2, 30)
    assert mse_2 == pytest.approx(4 * mse_1)


def test_dados_quadraticos_sao_ajustados_perfeitamente_pelo_modelo_certo():
    # Dados gerados por temperatura = 0.001 * cpu² + 0.2 * cpu + 30
    dados = [(cpu, 0.001 * cpu ** 2 + 0.2 * cpu + 30) for cpu in (0, 25, 50, 75, 100)]

    mse_certo = calcular_mse_quadratico(dados, 0.001, 0.2, 30)
    mse_linear = calcular_mse_quadratico(dados, 0, 0.2, 30)

    assert mse_certo == pytest.approx(0, abs=1e-9)
    assert mse_linear == pytest.approx(27.65625)
    assert mse_linear > mse_certo


def test_duplicar_os_dados_nao_muda_o_mse():
    uma_vez = calcular_mse_quadratico(DADOS, 0.001, 0.2, 30)
    duas_vezes = calcular_mse_quadratico(DADOS * 2, 0.001, 0.2, 30)
    assert duas_vezes == pytest.approx(uma_vez)


def test_ordem_dos_dados_nao_importa():
    normal = calcular_mse_quadratico(DADOS, 0.001, 0.2, 30)
    invertido = calcular_mse_quadratico(list(reversed(DADOS)), 0.001, 0.2, 30)
    assert invertido == pytest.approx(normal)


def test_nao_modifica_a_lista_de_dados():
    copia = list(DADOS)
    calcular_mse_quadratico(DADOS, 0.001, 0.2, 30)
    assert DADOS == copia


def test_aceita_qualquer_iteravel_de_pares_com_len():
    dados_como_tuplas = tuple(DADOS)
    assert calcular_mse_quadratico(dados_como_tuplas, 0.001, 0.2, 30) == pytest.approx(27.65625)


def test_retorna_numero_float():
    assert isinstance(calcular_mse_quadratico(DADOS, 0.001, 0.2, 30), float)


# ---------- Validação de entrada ----------

@pytest.mark.parametrize("vazio", [[], (), None])
def test_dados_vazios_levantam_value_error(vazio):
    with pytest.raises(ValueError):
        calcular_mse_quadratico(vazio, 0.001, 0.2, 30)


def test_mensagem_do_erro_para_dados_vazios():
    with pytest.raises(ValueError, match="Não existem dados"):
        calcular_mse_quadratico([], 0.001, 0.2, 30)


def test_dado_com_formato_invalido_levanta_erro():
    with pytest.raises((TypeError, ValueError)):
        calcular_mse_quadratico([(10, 20, 30)], 0.001, 0.2, 30)


# ---------- Testes isolados, com as dependências simuladas ----------

def test_usa_prever_e_calcular_erro_com_os_argumentos_corretos(monkeypatch):
    chamadas_previsao = []
    chamadas_erro = []

    def previsao_falsa(cpu, a, peso, bias):
        chamadas_previsao.append((cpu, a, peso, bias))
        return 10

    def erro_falso(real, previsto):
        chamadas_erro.append((real, previsto))
        # A diferença (999) deve ser ignorada: o MSE usa só o erro quadrático
        return 999, real * 10

    monkeypatch.setattr(modulo_mse, "prever_temperatura_quadratica", previsao_falsa)
    monkeypatch.setattr(modulo_mse, "calcular_erro", erro_falso)

    resultado = calcular_mse_quadratico([(1, 2), (3, 4)], a=0.5, peso=7, bias=1)

    assert chamadas_previsao == [(1, 0.5, 7, 1), (3, 0.5, 7, 1)]
    assert chamadas_erro == [(2, 10), (4, 10)]   # (real, previsto)
    assert resultado == pytest.approx((20 + 40) / 2)


def test_dados_vazios_nao_chamam_as_dependencias(monkeypatch):
    def nao_deve_ser_chamada(*args, **kwargs):
        raise AssertionError("não deveria ser chamada")

    monkeypatch.setattr(modulo_mse, "prever_temperatura_quadratica", nao_deve_ser_chamada)
    monkeypatch.setattr(modulo_mse, "calcular_erro", nao_deve_ser_chamada)

    with pytest.raises(ValueError):
        calcular_mse_quadratico([], 0.001, 0.2, 30)
