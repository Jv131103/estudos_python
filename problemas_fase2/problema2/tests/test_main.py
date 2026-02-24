import pytest
from src.inverso import inverso
from src.main import is_palinder
from src.tratar import trata_caracteres_especiais, trata_string


@pytest.mark.parametrize(
    "entrada,invertido",
    [
        ("ovo", "ovo"),
        ("arroz", "zorra"),
        ("1999", "9991"),
        ("Batat Doce", "ecoD tataB")
    ]
)
def test_inverso(entrada, invertido):
    assert inverso(entrada) == invertido


@pytest.mark.parametrize(
    "texto_original,texto_esperado",
    [
        ("Olá", "Ol"),
        ("VÉU", "VU"),
        ("Rosa é vermelha", "Rosavermelha")
    ]
)
def test_tratar_especiais_for_unicode(texto_original, texto_esperado):
    assert trata_caracteres_especiais(texto_original) == texto_esperado


@pytest.mark.parametrize(
    "entrada,saida",
    [
        ("SALVE", "salve"),
        ("Violetas", "violetas"),
        ("caChorro", "cachorro"),
        ("Olá", "ol")
    ]
)
def test_tratat_string(entrada, saida):
    assert trata_string(entrada) == saida


@pytest.mark.parametrize(
    "entrada,response", [
        ("Ame a ema", True),
        ("OVO", True),
        ("Ame o poema", True),
        ("O lobo ama o bolo.", True),
        ("Socorram-me, subi no ônibus em Marrocos.", True),
        ("batata doce", False),
        ("Rosas sao vermelhas e violetas são azuis", False),
        ("Se o sol é amarelo, então o amarelo é o sol", False)
    ]
)
def test_palinder(entrada, response):
    assert is_palinder(entrada) == response
