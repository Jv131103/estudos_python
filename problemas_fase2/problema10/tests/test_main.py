import pytest
from src.main import (gerar_lista_inplace, gerar_lista_nao_inplace,
                      gerar_lista_nao_inplace2, posicao_circular_ifversion,
                      posicao_circular_mathversion, posicao_circular_ternario,
                      posicao_circular_try, posicao_circular_whileversion)

FUNCOES = [
    posicao_circular_mathversion,
    posicao_circular_ifversion,
    posicao_circular_whileversion,
    posicao_circular_ternario,
    posicao_circular_try,
]


@pytest.mark.parametrize("lista,i,esperado", [
    ([1, 2, 3, 4], 0, 3),
    ([1, 2, 3, 4], 1, 5),
    ([1, 2, 3, 4], 2, 7),
    ([1, 2, 3, 4], 3, 5),
])
def test_posicao_circular(lista, i, esperado):

    for func in FUNCOES:
        assert func(lista, i) == esperado


@pytest.mark.parametrize("lista,esperado", [
    ([1, 2, 3, 4], [3, 5, 7, 5]),
    ([2, 4, 3], [6, 7, 5]),
])
def test_gerar_lista(lista, esperado):
    assert gerar_lista_inplace(lista.copy(), posicao_circular_mathversion) == esperado
    assert gerar_lista_nao_inplace(lista.copy(), posicao_circular_mathversion) == esperado
    assert gerar_lista_nao_inplace2(lista.copy(), posicao_circular_mathversion) == esperado


def test_todas_posicoes_equivalentes():

    lista = [1, 2, 3, 4, 5]

    for i in range(len(lista)):

        resultados = [
            posicao_circular_mathversion(lista, i),
            posicao_circular_ifversion(lista, i),
            posicao_circular_whileversion(lista, i),
            posicao_circular_ternario(lista, i),
            posicao_circular_try(lista, i),
        ]

        assert len(set(resultados)) == 1
