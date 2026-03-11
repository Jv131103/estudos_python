from src.main import atendimento2


def test_atendimento2_saida(capsys):
    atendimento2()

    saida = capsys.readouterr().out

    esperado = (
        "Atendendo João\n"
        "Atendendo Maria\n"
        "Atendendo Pedro\n"
        "Atendendo Douglas\n"
    )

    assert saida == esperado
