import json
from datetime import datetime
from pathlib import Path

FILES = Path().cwd() / "jsons" / "eventos.json"
if not Path.exists(FILES):
    FILES.parent.mkdir(parents=True, exist_ok=True)
    FILES.write_text("[]", encoding="utf-8")
    print(f"Arquivo criado em: {FILES}")


def registrar_evento(caminho_arquivo, tipo, mensagem):
    # ATENÇÃO: esse padrão de ler-modificar-escrever NÃO é seguro em concorrência.
    # Se duas chamadas rodarem "ao mesmo tempo", ambas podem ler o arquivo
    # com o mesmo conteúdo inicial, e a segunda escrita sobrescreve a primeira,
    # perdendo o evento que foi registrado por ela. Isso é uma "race condition" —
    # o mesmo tipo de problema que bancos de dados resolvem com locks/transações.
    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        try:
            valores = json.load(file)
        except FileNotFoundError:
            valores = []
        except json.decoder.JSONDecodeError:
            print(f"AVISO: '{caminho_arquivo}' continha JSON inválido — recriando do zero. Dados anteriores foram perdidos.")
            valores = []

    dados = {
        "tipo": tipo,
        "mensagem": mensagem,
        "timestamp": datetime.now().isoformat()
    }

    valores.append(dados)

    try:
        with open(caminho_arquivo, mode="w", encoding="utf-8") as file:
            json.dump(valores, file, indent=4, ensure_ascii=False)
            print("log registrado com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar log no arquivo: {e}")


def resumo_por_tipo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        try:
            valores = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            valores = []

        novo = {}

        for d in valores:
            novo[d['tipo']] = novo.get(d['tipo'], 0) + 1

        return novo


registrar_evento(FILES, "erro", "Falha ao conectar")
registrar_evento(FILES, "info", "Sistema iniciado")
registrar_evento(FILES, "erro", "Timeout na API")

print(resumo_por_tipo(FILES))
