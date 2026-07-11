import pytest
from src.conta import ContaBancaria


def test_saque_insuficiente():
    conta = ContaBancaria("Ana")
    conta.depositar(100)
    with pytest.raises(ValueError):
        conta.sacar(200)


def test_deposito_neativo():
    conta = ContaBancaria("Ana")
    with pytest.raises(ValueError):
        conta.depositar(-100)


def test_saque_negativo():
    conta = ContaBancaria("Ana")
    conta.depositar(100)
    with pytest.raises(ValueError):
        conta.sacar(-50)


def test_criacao_nome_vazio():
    with pytest.raises(ValueError):
        ContaBancaria("")
