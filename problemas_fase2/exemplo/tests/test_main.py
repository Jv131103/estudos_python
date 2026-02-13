from src.main import (ContadorDeCaracteres, contar_unicos_otimizado,
                      contar_unicos_simples)


def test_simples():
    assert contar_unicos_simples("banana") == 3


def test_otimizado():
    assert contar_unicos_otimizado("banana") == 3


def test_classe():
    contador = ContadorDeCaracteres("banana")
    assert contador.contar_simples() == 3
    assert contador.contar_otimizado() == 3


# Execute py -m pytest
# Ou py -m pytest <your_test>.py
