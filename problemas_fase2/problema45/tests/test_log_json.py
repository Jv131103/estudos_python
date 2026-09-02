import json
from datetime import datetime

from src.log_json import registrar_evento, resumo_por_tipo


def test_registrar_evento_cria_arquivo_se_nao_existe(tmp_path):
    arquivo = tmp_path / "eventos.json"
    assert not arquivo.exists()

    registrar_evento(arquivo, "info", "teste")

    assert arquivo.exists()


def test_multiplos_eventos_sao_adicionados(tmp_path):
    arquivo = tmp_path / "eventos.json"

    registrar_evento(arquivo, "erro", "Falha 1")
    registrar_evento(arquivo, "info", "Info 1")
    registrar_evento(arquivo, "erro", "Falha 2")

    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = json.load(f)

    assert len(conteudo) == 3


def test_resumo_por_tipo_com_composicao_variada(tmp_path):
    arquivo = tmp_path / "eventos.json"

    registrar_evento(arquivo, "erro", "Falha 1")
    registrar_evento(arquivo, "info", "Info 1")
    registrar_evento(arquivo, "erro", "Falha 2")
    registrar_evento(arquivo, "erro", "Falha 3")

    resultado = resumo_por_tipo(arquivo)

    assert resultado == {"erro": 3, "info": 1}


def test_resumo_por_tipo_arquivo_inexistente(tmp_path):
    arquivo = tmp_path / "nao_existe.json"
    resultado = resumo_por_tipo(arquivo)
    assert resultado == {}


def test_timestamp_congelado(tmp_path, monkeypatch):
    arquivo = tmp_path / "eventos.json"

    class DataFalsa:
        @classmethod
        def now(cls):
            return datetime(2026, 1, 1, 10, 0, 0)

    monkeypatch.setattr("src.log_json.datetime", DataFalsa)

    registrar_evento(arquivo, "info", "teste")

    with open(arquivo) as f:
        dados = json.load(f)

    assert dados[0]["timestamp"] == "2026-01-01T10:00:00"
