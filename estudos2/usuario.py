import json
from pathlib import Path

FILES = Path().cwd() / "jsons" / "usuario.json"
if not Path.exists(FILES):
    FILES.parent.mkdir(parents=True, exist_ok=True)
    FILES.write_text("{}", encoding="utf-8")
    print(f"Arquivo criado em: {FILES}")


def criar_usuario(usuario):
    with open(FILES, mode="r", encoding="utf-8") as file:
        try:
            valores = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            valores = {}

    valores.update(usuario)

    try:
        with open(FILES, mode="w", encoding="utf-8") as file:
            json.dump(valores, file, indent=4, ensure_ascii=False)
            print(f"Usuário {valores['nome']} cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar no arquivo: {e}")


def carregar():
    try:
        usuario = {}
        with open(FILES, mode="r", encoding="utf-8") as file:
            usuario = json.load(file)
            if not usuario:
                print("Usuário não encontrado!")
                return
            print(f"Usuário {usuario['nome']} retornado")
    except Exception as e:
        print(f"Erro ao carregar usuario: {e}")

    return usuario


usuario = {"nome": "Ana", "idade": 28, "email": "ana@teste.com"}
criar_usuario(usuario)
print()
usuario_atualizado = carregar()
print(usuario_atualizado)
print()
usuario_atualizado["idade"] = 29
criar_usuario(usuario_atualizado)
