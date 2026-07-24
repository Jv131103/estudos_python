import json
from pathlib import Path

FILES = Path().cwd() / "jsons" / "contatos.json"
if not Path.exists(FILES):
    FILES.parent.mkdir(parents=True, exist_ok=True)
    FILES.write_text("[]", encoding="utf-8")
    print(f"Arquivo criado em: {FILES}")


def adicionar_contato(nome, telefone, email):
    with open(FILES, mode="r", encoding="utf-8") as file:
        try:
            valores = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            valores = []

    valores.append(
        {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }
    )

    try:
        with open(FILES, mode="w", encoding="utf-8") as file:
            json.dump(valores, file, indent=4, ensure_ascii=False)
            print(f"Usuário {nome} cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar no arquivo: {e}")


def buscar_contato(nome):
    with open(FILES, mode="r", encoding="utf-8") as file:
        encontrou = False
        try:
            nome = nome.title().strip()
            valores = json.load(file)
            for valor in valores:
                if nome == valor["nome"] or nome in valor["nome"]:
                    encontrou = True
                    print(f"Encotrado: {valor['nome']}")
                    print(f"\t{valor['telefone']}")
                    print(f"\t{valor['email']}")
                    print()

            if not encontrou:
                print(f"Usuário {nome} não encontrado")

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print("Dados não encontrados!\nADICIONE CONTATOS")


def remover_contato(nome):
    with open(FILES, mode="r", encoding="utf-8") as file:
        try:
            nome = nome.title().strip()
            valores = json.load(file)
            for valor in valores:
                if nome == valor["nome"]:
                    print(f"Usuário: {valor['nome']}")
                    print("removendo...")
                    valores.remove(valor)
                    break
            else:
                print("Usuário não encontrado!")
                return
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print("Dados não encontrados!\nADICIONE CONTATOS")

    try:
        with open(FILES, mode="w", encoding="utf-8") as file:
            json.dump(valores, file, indent=4, ensure_ascii=False)
            print(f"Usuário {nome} removido com sucesso!")
    except Exception as e:
        print(f"Erro ao reescrver no arquivo: {e}")


def listar_contatos():
    with open(FILES, mode="r", encoding="utf-8") as file:
        try:
            valores = json.load(file)
            if not valores:
                print("Lista Vazia!")
                return

            for valor in valores:
                print(f"Usuário: {valor['nome']}")
                print(f"\t{valor['telefone']}")
                print(f"\t{valor['email']}")
                print()
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print("Dados não encontrados!\nADICIONE CONTATOS")


adicionar_contato("Clemente de Roma", "11 99474-5152", "clementebispoderoma229@gmail.com")
buscar_contato("Hip")
remover_contato("Hipócrates")
buscar_contato("Hip")
remover_contato("Hipócrates")
listar_contatos()
