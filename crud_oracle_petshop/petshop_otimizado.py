import crud_otimizado as crd


def pedir_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas números.")


def main():
    conn = crd.connect_database()

    options = {
        "1": ["Cadastrar Pet", crd.create],
        "2": ["Listar Pets", crd.read],
        "3": ["Alterar Pet", crd.update],
        "4": ["Excluir Pet", crd.delete],
        "5": ["Excluir todos os pets", crd.delete_all],
        "6": ["Sair", None],
    }

    while True:
        print("\n------ CRUD - PETSHOP ------\n")
        for opcao, tipo in options.items():
            print(f"{opcao} - {tipo[0]}")
        print()

        resposta = input("Escolha: ").strip()

        match resposta:
            case "1":
                tipo = input("Tipo do PET: ").strip()
                nome = input("Nome do PET: ").strip()
                idade = pedir_inteiro("Idade do PET: ")
                options[resposta][1](conn, tipo, nome, idade)

            case "2":
                pets = options[resposta][1](conn)
                if not pets:
                    print("Nenhum registro encontrado.")
                else:
                    print("Listando...")
                    for pet in pets:
                        print(pet)

            case "3":
                pet_id = pedir_inteiro("ID do PET: ")
                tipo = input("Novo tipo do PET: ").strip()
                nome = input("Novo nome do PET: ").strip()
                idade = pedir_inteiro("Nova idade do PET: ")
                options[resposta][1](conn, pet_id, tipo, nome, idade)

            case "4":
                pet_id = pedir_inteiro("ID do PET: ")
                options[resposta][1](conn, pet_id)

            case "5":
                confirmacao = input("Você tem certeza disso? [S/N] ").strip().upper()
                if confirmacao == "S":
                    options[resposta][1](conn)
                else:
                    print("Dados não excluídos.")

            case "6":
                print("Encerrando...")
                break

            case _:
                print("Digite uma opção válida.")

    crd.close_database(conn)


if __name__ == "__main__":
    main()
