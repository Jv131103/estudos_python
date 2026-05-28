from pathlib import Path

Path("./arquivos").mkdir(parents=True, exist_ok=True)


def gerar_todos(inicio, fim, file):
    total_pares = 0
    total_impares = 0
    file.write("==============================\n")
    for x in range(inicio, fim + 1):
        if x % 2 == 0:
            saida = "par"
            total_pares += 1
        else:
            saida = "ímpar"
            total_impares += 1
        file.write(f"{x} → {saida}\n")

    file.write("==============================\n")
    file.write(f"Total de pares: {total_pares}\nTotal de ímpares: {total_impares}\n")


def gerar_pares(inicio, fim, file):
    total_pares = 0
    file.write("==============================\n")
    for x in range(inicio, fim + 1):
        if x % 2 == 0:
            file.write(f"{x} → par\n")
            total_pares += 1
    file.write("==============================\n")
    file.write(f"Total de pares: {total_pares}\n")


def gerar_impares(inicio, fim, file):
    total_impares = 0
    file.write("==============================\n")
    for x in range(inicio, fim + 1):
        if x % 2 != 0:
            file.write(f"{x} → ímpar\n")
            total_impares += 1
    file.write("==============================\n")
    file.write(f"Total de ímpares: {total_impares}\n")


def gerar(inicio, fim, modo, file):
    options = {
        "todos": gerar_todos,
        "pares": gerar_pares,
        "impares": gerar_impares
    }
    options[modo](inicio, fim, file)


def gerar_arquivo(inicio=0, fim=10, modo="todos"):
    try:
        with open("./arquivos/resultado.txt", "w", encoding="utf8") as file:
            gerar(inicio, fim, modo, file)
            print()
            print("Sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except FileExistsError:
        print("Arquivo inexistente!")


def trata_input(msg):
    while True:
        opc = input(msg).strip().lower()
        if not opc:
            print("Digite um tipo: [todos, pares, impares, sair]...")
            continue
        return opc


def trata_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um valor numérico inteiro")


def menu():
    while True:
        print("Opções:\n\t[ todos ]\n\t[ pares ]\n\t[ impares ]\n\t[ sair ]")
        print()
        opc = trata_input("Digite uma opcao: ")
        if opc == "sair":
            break
        elif opc not in ["todos", "pares", "impares"]:
            print("Tipo inválido, digite apenas as opções disponíveis")
            print()
            continue

        inicio = trata_int("Começo: ")
        fim = trata_int("Fim: ")
        if inicio > fim:
            inicio, fim = fim, inicio

        gerar_arquivo(inicio, fim, opc)
        print()


menu()
