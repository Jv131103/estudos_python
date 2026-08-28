from pathlib import Path


def adicionar_tarefa(arquivo):
    print("==" * 20)
    print("Digite uma tarefa, por exemplo:\n. Estudar PYTHON")
    print("--" * 20)
    tarefa = input("Digite uma tarefa: ")
    print("--" * 20)
    with open(arquivo, mode="a", encoding="utf-8") as file:
        print("Adicionando tarefa...")
        try:
            qtd = ler_tarefa(arquivo, view=False)
            if qtd is None:
                print("Erro interno")
                return False
            file.write(f"{qtd + 1}. {tarefa}\n")
            print("Tarefa adicionada com sucesso!")
            return True
        except Exception as e:
            print(f"Tarefa não adicionada por erro: {e}")
        return False


def ler_tarefa(arquivo, view=True):
    with open(arquivo, mode="r", encoding="utf-8") as file:
        try:
            linhas = file.readlines()

            if view:
                for dados in linhas:
                    print(dados, end="")

        except Exception as e:
            print(f"Tarefa não adicionada por erro: {e}")
            return None

    return len(linhas)


def main():
    FILE = Path().cwd() / 'arquivos' / 'tarefas.txt'
    if not Path.exists(FILE):
        FILE.parent.mkdir(parents=True, exist_ok=True)
        print(f"Arquivo criado em: {FILE}")

    casos = {
        'a': ["adicionar", adicionar_tarefa],
        'r': ["ler", ler_tarefa],
    }
    while True:
        print("++" * 20)
        for chave, valores in casos.items():
            print(f"{chave} - {valores[0]}")
            print("--" * 20)

        modo = input("Qual modo quer fazer? ")
        if casos.get(modo):
            print()
            casos[modo][1](FILE)
            print()
        else:
            print("Modo inválido, digite apenas os disponíveis")
            print()
            continue

        novo = input("Nova tarefa? [S/N] ").strip().upper()
        if novo != "S":
            break


main()
