import random

import pytest
from src.main import (encontrar_ponto_rotacao, encontrar_ponto_rotacao_binaria,
                      encontrar_ponto_rotacao_linear,
                      encontrar_ponto_rotacao_min_manual,
                      encontrar_ponto_rotacao_vizinhos)

ALGORITMOS = [
    encontrar_ponto_rotacao,
    encontrar_ponto_rotacao_linear,
    encontrar_ponto_rotacao_min_manual,
    encontrar_ponto_rotacao_vizinhos,
    encontrar_ponto_rotacao_binaria,
]


def gerar_lista_rotacionada(n, k):
    base = list(range(n))
    k %= n
    return base[-k:] + base[:-k]


@pytest.mark.parametrize(
    "lista,indice_esperado",
    [
        ([15, 18, 2, 3, 6, 12], 2),
        ([4, 5, 6, 7, 0, 1, 2], 4),
        ([2, 3, 4, 5, 6], 0),
    ],
)
def test_exemplos(lista, indice_esperado):
    for algoritmo in ALGORITMOS:
        assert algoritmo(lista) == indice_esperado


@pytest.mark.parametrize("n", [5, 10, 50])
def test_rotacoes(n):
    for k in range(n):
        lista = gerar_lista_rotacionada(n, k)
        esperado = k % n

        for algoritmo in ALGORITMOS:
            assert algoritmo(lista) == esperado


@pytest.mark.parametrize("n", [100, 1000])
def test_listas_grandes(n):
    k = n // 3
    lista = gerar_lista_rotacionada(n, k)
    esperado = k % n

    for algoritmo in ALGORITMOS:
        assert algoritmo(lista) == esperado


def test_random():
    for _ in range(100):
        n = random.randint(5, 100)
        k = random.randint(0, n - 1)

        lista = gerar_lista_rotacionada(n, k)
        esperado = k % n

        for algoritmo in ALGORITMOS:
            assert algoritmo(lista) == esperado


def test_lista_vazia():
    for algoritmo in ALGORITMOS:
        with pytest.raises(ValueError):
            algoritmo([])
