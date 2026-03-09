import pytest
from src.main import somar_matriz, somar_matriz2, somar_matriz3, somar_matriz4


@pytest.mark.parametrize(
    "matriz,soma_matriz",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [6, 15, 24]),
        ([[2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]], [20, 30, 40]),
        ([[5, 7, 9], [7, 9, 12], [3, 5, 7]], [21, 28, 15])
    ]
)
class TestSomaMatrizes:
    def test_soma_matriz_v1(self, matriz, soma_matriz):
        assert somar_matriz(matriz) == soma_matriz

    def test_soma_matriz_v2(self, matriz, soma_matriz):
        assert somar_matriz2(matriz) == soma_matriz

    def test_soma_matriz_v3(self, matriz, soma_matriz):
        assert somar_matriz3(matriz) == soma_matriz

    def test_soma_matriz_v4(self, matriz, soma_matriz):
        assert somar_matriz4(matriz) == soma_matriz
