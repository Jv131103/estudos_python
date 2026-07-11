from src.validar_senha import validar_senha


def test_senha_valida():
    assert validar_senha("Abcdefg1!") is True


def test_senha_curta():
    assert validar_senha("Ab1!") is False


def test_senha_sem_maiuscula():
    assert validar_senha("123@aaaaa") is False


def test_senha_sem_minuscula():
    assert validar_senha("123@AAAAA") is False


def test_senha_sem_numeros():
    assert validar_senha("aaaa@AAAAA") is False


def test_senha_sem_especiais():
    assert validar_senha("aaaa123AAAAA") is False
