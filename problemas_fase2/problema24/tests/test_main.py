import pytest
from src.main import (decimal_para_binario, gerar_binario_fila_lista_direta,
                      gerar_binarios_bin, gerar_binarios_fila,
                      gerar_binarios_fstring, gerar_binarios_manual,
                      gerar_binarios_recursivo)


@pytest.mark.parametrize(
    "numero, esperado",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (3, "11"),
        (4, "100"),
        (5, "101"),
        (8, "1000"),
        (10, "1010"),
    ],
)
def test_decimal_para_binario(numero, esperado):
    assert decimal_para_binario(numero) == esperado


def test_gerar_binarios_fila_com_5():
    assert gerar_binarios_fila(5) == ["1", "10", "11", "100", "101"]


def test_gerar_binario_fila_lista_direta_com_5():
    assert gerar_binario_fila_lista_direta(5) == ["1", "10", "11", "100", "101"]


def test_gerar_binarios_manual_com_5():
    assert gerar_binarios_manual(5) == ["1", "10", "11", "100", "101"]


def test_gerar_binarios_bin_com_5():
    assert gerar_binarios_bin(5) == ["1", "10", "11", "100", "101"]


def test_gerar_binarios_fstring_com_5():
    assert gerar_binarios_fstring(5) == ["1", "10", "11", "100", "101"]


def test_gerar_binarios_recursivo_com_5():
    assert gerar_binarios_recursivo(5) == ["1", "10", "11", "100", "101"]


def test_geradores_com_zero():
    assert gerar_binarios_fila(0) == []
    assert gerar_binario_fila_lista_direta(0) == []
    assert gerar_binarios_manual(0) == []
    assert gerar_binarios_bin(0) == []
    assert gerar_binarios_fstring(0) == []
    assert gerar_binarios_recursivo(0) == []


def test_geradores_com_um():
    esperado = ["1"]

    assert gerar_binarios_fila(1) == esperado
    assert gerar_binario_fila_lista_direta(1) == esperado
    assert gerar_binarios_manual(1) == esperado
    assert gerar_binarios_bin(1) == esperado
    assert gerar_binarios_fstring(1) == esperado
    assert gerar_binarios_recursivo(1) == esperado


@pytest.mark.parametrize("n", [1, 2, 5, 10, 20])
def test_todas_as_implementacoes_geram_mesmo_resultado(n):
    esperado = gerar_binarios_bin(n)

    assert gerar_binarios_fila(n) == esperado
    assert gerar_binario_fila_lista_direta(n) == esperado
    assert gerar_binarios_manual(n) == esperado
    assert gerar_binarios_fstring(n) == esperado
    assert gerar_binarios_recursivo(n) == esperado
