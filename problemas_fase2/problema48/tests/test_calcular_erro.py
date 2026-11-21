import pytest
# Ajuste o import se o seu módulo tiver outro nome ou estiver em src/.
from src.calcular_erro import calcular_erro


@pytest.mark.parametrize(
    "real, previsto, diferenca_esperada, erro_esperado",
    [
        (40, 35, 5, 25),
        (50, 45, 5, 25),
        (95, 85, 10, 100),
    ],
)
def test_exemplos_do_enunciado(real, previsto, diferenca_esperada, erro_esperado):
    assert calcular_erro(real, previsto) == (diferenca_esperada, erro_esperado)


def test_previsao_igual_ao_real_gera_erro_zero():
    assert calcular_erro(40, 40) == (0, 0)


def test_previsao_maior_que_o_real_gera_diferenca_negativa():
    diferenca, erro = calcular_erro(35, 40)
    assert diferenca == -5
    assert erro == 25


def test_erro_quadratico_nunca_e_negativo():
    _, erro = calcular_erro(10, 100)
    assert erro >= 0


def test_erro_quadratico_e_igual_para_diferencas_opostas():
    _, erro_1 = calcular_erro(40, 35)
    _, erro_2 = calcular_erro(35, 40)
    assert erro_1 == erro_2


def test_valores_decimais():
    diferenca, erro = calcular_erro(40.5, 38.0)
    assert diferenca == pytest.approx(2.5)
    assert erro == pytest.approx(6.25)


def test_retorna_tupla_com_dois_valores():
    resultado = calcular_erro(40, 35)
    assert isinstance(resultado, tuple)
    assert len(resultado) == 2
