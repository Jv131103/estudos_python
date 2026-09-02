import json
from datetime import datetime
from pathlib import Path

FILES = Path().cwd() / "jsons" / "eventos.json"

if FILES.exists():
    FILES.unlink()  # remove o arquivo antigo, que está no formato incompatível


def registrar_evento(caminho_arquivo, tipo, mensagem):
    dados = {"tipo": tipo, "mensagem": mensagem, "timestamp": datetime.now().isoformat()}
    with open(caminho_arquivo, "a", encoding="utf-8") as file:
        file.write(json.dumps(dados, ensure_ascii=False) + "\n")


def resumo_por_tipo(caminho_arquivo):
    novo = {}
    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        for linha in file:
            if linha.strip():
                d = json.loads(linha)
                novo[d["tipo"]] = novo.get(d["tipo"], 0) + 1
    return novo


registrar_evento(FILES, "erro", "Falha ao conectar")
registrar_evento(FILES, "info", "Sistema iniciado")
registrar_evento(FILES, "erro", "Timeout na API")

print(resumo_por_tipo(FILES))
