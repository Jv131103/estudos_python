import pytest
from src.main import remover_duplicatas_inplace, remover_duplicatas_inplace2


@pytest.mark.parametrize(
    "entrada,saida",
    [
        ([3, 1, 2, 3, 4, 1, 5], [3, 1, 2, 4, 5]),
        ([1, 1, 1, 1, 1], [1]),
        ([2, 3, 1, 4, 5, 6, 1], [2, 3, 1, 4, 5, 6])
    ]
)
class TestRemoverDuplicadasInplace:
    def test_remover_duplicatas_inplace(self, entrada, saida):
        assert remover_duplicatas_inplace(entrada.copy()) == saida

    def test_remover_duplicatas_inplace2(self, entrada, saida):
        assert remover_duplicatas_inplace2(entrada.copy()) == saida
