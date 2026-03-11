from src.main import impressao_menu_interativo, impressao_menu_simulado


def test_impressao_menu_simulado_saida(capsys):
    impressao_menu_simulado()

    saida = capsys.readouterr().out

    esperado = (
        "Imprimindo documentoA\n"
        "Imprimindo documentoB\n"
    )

    assert saida == esperado


def test_interativo_imprime_dois_documentos_e_desliga(monkeypatch, capsys):
    entradas = iter([
        "imprimir documentoA",
        "imprimir documentoB",
        "executar impressão",
        "executar impressão",
        "desligar",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    impressao_menu_interativo()

    saida = capsys.readouterr().out

    assert "Imprimindo documentoA" in saida
    assert "Imprimindo documentoB" in saida
    assert "Desligando impressão..." in saida
    assert "Impressão limpa!" in saida


def test_interativo_mostra_fila_vazia_ao_executar_sem_documentos(monkeypatch, capsys):
    entradas = iter([
        "executar impressão",
        "desligar",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    impressao_menu_interativo()

    saida = capsys.readouterr().out

    assert "Fila de impressão vazia" in saida


def test_interativo_comando_vazio(monkeypatch, capsys):
    entradas = iter([
        "",
        "desligar",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    impressao_menu_interativo()

    saida = capsys.readouterr().out

    assert "Digite um comando válido." in saida


def test_interativo_imprimir_sem_nome(monkeypatch, capsys):
    entradas = iter([
        "imprimir",
        "desligar",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    impressao_menu_interativo()

    saida = capsys.readouterr().out

    assert "Arquivo de documento não encontrado" in saida


def test_interativo_comando_invalido(monkeypatch, capsys):
    entradas = iter([
        "apagar tudo",
        "desligar",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    impressao_menu_interativo()

    saida = capsys.readouterr().out

    assert "Comando inválido" in saida
    assert "Digite apenas:" in saida


def test_interativo_desligar_com_documentos_pendentes(monkeypatch, capsys):
    entradas = iter([
        "imprimir documentoA",
        "imprimir documentoB",
        "desligar",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    impressao_menu_interativo()

    saida = capsys.readouterr().out

    assert "Desligando impressão..." in saida
    assert "documentoA não impresso!" in saida
    assert "documentoB não impresso!" in saida
    assert "Impressão limpa!" in saida
