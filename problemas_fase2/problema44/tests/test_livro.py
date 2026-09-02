import pytest
from src.livro import Livro


def test_livro_ja_emprestado_retorna_erro():
    livro = Livro("Batata", "Batatinha", 1)
    livro.emprestar()
    with pytest.raises(ValueError, match="Não há cópias disponpiveis"):
        livro.emprestar()


def test_livro_ja_devolvido_retorna_erro():
    livro = Livro("Batata", "Batatinha", 1)
    livro.emprestar()
    livro.devolver()
    with pytest.raises(ValueError, match="Livro inexistente para devolução"):
        livro.devolver()


def test_livro_deve_estar_disponivel():
    livro = Livro("Batata", "Batatinha", 2)
    livro.emprestar()
    assert livro.esta_disponivel()


def test_livro_deve_estar_indisponivel():
    livro = Livro("Batata", "Batatinha", 2)
    livro.emprestar()
    livro.emprestar()
    assert not livro.esta_disponivel()
