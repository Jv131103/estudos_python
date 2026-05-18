import json
from datetime import datetime
from pathlib import Path

DIRETORIO = Path().cwd() / "jsons"
ARQUIVO = DIRETORIO / "tarefas.json"
ARQUIVO.parent.mkdir(parents=True, exist_ok=True)


def carregar_tarefas():
    if not ARQUIVO.exists():
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)

    if not isinstance(dados, list):
        dados = []

    print("Dados carregados com sucesso!")
    return dados  # lê o JSON, retorna lista


def salvar_tarefas(tarefas):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(tarefas, f, indent=4, ensure_ascii=False)
            print("Tarefas salvas com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")


def trata_id(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite apenas números!")


def adicionar_tarefa(tarefas, titulo, descricao):
    dados = {}
    dados["id"] = max((t["id"] for t in tarefas), default=0) + 1
    dados["titulo"] = titulo
    dados["descricao"] = descricao
    dados["status"] = "pendente"
    dados["criada_em"] = datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
    tarefas.append(dados)  # cria e appenda
    print(f"Tarefa {dados['titulo']} adicionada ao registro")
    return tarefas


def concluir_tarefa(tarefas, id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            print(f"Concluído: {tarefa['titulo']}, id={id}")
            tarefa["status"] = "concluída"
            break
    return tarefas


def remover_tarefa(tarefas, id):
    novo = []
    apagou = False
    for tarefa in tarefas:
        if tarefa['id'] == id:
            apagou = True
            print(f"Tarefa de id {id} removido com sucesso!")
            continue
        novo.append(tarefa)
    if not apagou:
        print(f"Tarefa de id {id} não encontrada!")
    return novo


def listar_tarefas(tarefas, filtro="todas"):
    if filtro == "pendentes":
        print("Retornando apenas pendentes...")
        tarefas = [tarefa for tarefa in tarefas if tarefa["status"] == "pendente"]
    elif filtro == "concluidas":
        print("Retornando apenas concluídas...")
        tarefas = [tarefa for tarefa in tarefas if tarefa["status"] == "concluída"]
    elif filtro == "todas":
        print("Retornando todos...")
    else:
        print("Filtro inixistente, digite apenas [concluido, pendente ou todas]")
        return

    if not tarefas:
        print("Sem tarefas!")
        return

    for dados in tarefas:
        status = "[PENDENTE]" if dados["status"] == "pendente" else "[CONCLUÍDA]"
        periodo = datetime.strptime(
            dados["criada_em"],
            "%Y-%m-%d %H:%M:%S"
        ).strftime("%d/%m/%Y %H:%M")
        print(f"{status} #{dados['id']} - {dados['descricao']} ({periodo})")


def menu():
    print("===== TAREFAS =====")
    opcs = [
        ["1", "Adicionar tarefa"],
        ["2", "Listar tarefas"],
        ["3", "Concluir tarefa"],
        ["4", "Remover tarefa"],
        ["0", "Sair"]
    ]

    tarefas = carregar_tarefas()

    for escolha, opc in opcs:
        print(f"[{escolha}] {opc}")
    print()

    while True:
        opc = input(">> ")

        if opc == "0":
            print("Encerrando Geranciador!")
            break
        elif opc == "1":
            titulo = input("Título: ").strip().title()
            descricao = input("Descrição: ").strip().title()
            tarefas = adicionar_tarefa(tarefas, titulo, descricao)
        elif opc == "2":
            filtro = input("Pesquisa: [pendentes, concluidas, todas] ").strip().lower()
            listar_tarefas(tarefas, filtro)
            print()
            continue
        elif opc == "3":
            _id = trata_id("Id: ")
            tarefas = concluir_tarefa(tarefas, _id)
        elif opc == "4":
            _id = trata_id("Id: ")
            tarefas = remover_tarefa(tarefas, _id)
        else:
            print("Opção inválida, digite de 0 a 4")
            print()
            continue

        salvar_tarefas(tarefas)
        print()

    print("Fim, até a próxima!")


menu()
