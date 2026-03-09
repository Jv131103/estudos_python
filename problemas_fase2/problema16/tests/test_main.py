from src.main import (busca1, busca2, busca3, busca4, busca5, busca6, busca7,
                      busca8)

ALGORITMOS = [
    busca1,
    busca2,
    busca3,
    busca4,
    busca5,
    busca6,
    busca7,
    busca8,
]


def test_busca_basica():

    lista = [7, 3, 9, 1, 3]
    alvo = 3

    esperado = 1

    for algoritmo in ALGORITMOS:
        assert algoritmo(lista.copy(), alvo) == esperado


def test_inicio():

    lista = [5, 2, 3, 4]
    alvo = 5

    esperado = 0

    for algoritmo in ALGORITMOS:
        assert algoritmo(lista.copy(), alvo) == esperado


def test_final():

    lista = [1, 2, 3, 4, 9]
    alvo = 9

    esperado = 4

    for algoritmo in ALGORITMOS:
        assert algoritmo(lista.copy(), alvo) == esperado


def test_nao_encontrado():

    lista = [1, 2, 3, 4]
    alvo = 99

    esperado = -1

    for algoritmo in ALGORITMOS:
        assert algoritmo(lista.copy(), alvo) == esperado


def test_lista_vazia():

    lista = []
    alvo = 10

    esperado = -1

    for algoritmo in ALGORITMOS:
        assert algoritmo(lista.copy(), alvo) == esperado


def test_valores_repetidos():

    lista = [2, 2, 2, 2]
    alvo = 2

    esperado = 0

    for algoritmo in ALGORITMOS:
        assert algoritmo(lista.copy(), alvo) == esperado


def test_lista_grande():

    lista = list(range(1000))
    alvo = 777

    esperado = 777

    for algoritmo in ALGORITMOS:
        assert algoritmo(lista.copy(), alvo) == esperado
