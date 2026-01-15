"""
Faça um programa que:

    Leia uma string representando um comando:

        "add", "remove", "list", "exit"

Use match para:

    "add" → imprimir "Adicionando item"

    "remove" → "Removendo item"

    "list" → "Listando itens"

    "exit" → "Encerrando"

    qualquer outro → "Comando inválido"

Depois, refaça a lógica sem match, usando if/elif/else, e compare legibilidade.

COMPARAÇÃO DIRETA:
| Critério        | match     | if/elif | dict      |
| --------------- | --------- | ------- | --------- |
| Clareza         | ⭐⭐⭐⭐  | ⭐⭐⭐  | ⭐⭐⭐⭐ |
| Escalabilidade  | ⭐⭐⭐⭐  | ⭐⭐    | ⭐⭐⭐⭐ |
| Simplicidade    | ⭐⭐⭐    | ⭐⭐    | ⭐⭐⭐⭐ |
| Versões antigas | ❌        | ✅      | ✅        |
"""


def versao_match():
    opcao = input().strip().lower()

    match opcao:
        case "add":
            print("Adicionando item")
        case "remove":
            print("Removendo item")
        case "list":
            print("Listando itens")
        case "exit":
            print("Encerrando")
        case _:
            print(f"Comando {opcao} inválido!")


def versao_if():
    opcao = input().strip().lower()

    if opcao == "add":
        print("Adicionando item")
    elif opcao == "remove":
        print("Removendo item")
    elif opcao == "list":
        print("Listando itens")
    elif opcao == "exit":
        print("Encerrando")
    else:
        print(f"Comando {opcao} inválido!")


def versao_dict():
    opcoes = {
        "add": "Adicionando item",
        "remove": "Removendo item",
        "list": "Listando itens",
        "exit": "Encerrando"
    }

    opcao = input().strip().lower()

    print(opcoes.get(opcao, f"Comando {opcao} inválido!"))


versao_match()
print()
versao_if()
print()
versao_dict()
