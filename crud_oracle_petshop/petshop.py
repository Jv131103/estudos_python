import crud as crd

CONN = crd.conect_database()

options = {
    "1": ["Cadastrar Pet", crd.create],
    "2": ["Listar Pet", crd.read],
    "3": ["Alterar Pet", crd.update],
    "4": ["Excluir Pet", crd.delete],
    "5": ["EXCLUIR TODOS OS PETS", crd.delete_all],
    "6": ["SAIR", ""],
}

while True:
    print("------ CRUD - PETSHOP ------")
    print()
    for opcao, tipo in options.items():
        print(f"{opcao} - {tipo[0]}")
    print()

    resposta = input("Escolha: ")
    match resposta:
        case "1":
            tipo = input("Tipo do PET: ").strip()
            nome = input("Nome do PET: ").strip()
            while True:
                try:
                    idade = int(input("Idade do PET: "))
                    break
                except ValueError:
                    print("Digite apenas números")

            options[resposta][-1](CONN, tipo, nome, idade)
        case "2":
            options[resposta][-1](CONN)
        case "3":
            while True:
                try:
                    _id = int(input("ID do PET: "))
                    break
                except ValueError:
                    print("Digite apenas números")
            if not crd.read_one(CONN, _id):
                print(f"Nenhum pet cadastrado com o id {_id}")
            else:
                tipo = input("Tipo do PET: ").strip()
                nome = input("Nome do PET: ").strip()
                while True:
                    try:
                        idade = int(input("Idade do PET: "))
                        break
                    except ValueError:
                        print("Digite apenas números")

                options[resposta][-1](CONN, _id, tipo, nome, idade)
        case "4":
            while True:
                try:
                    _id = int(input("ID do PET: "))
                    break
                except ValueError:
                    print("Digite apenas números")
            options[resposta][-1](CONN, _id)
        case "5":
            vc_tem_certeza = input("Você têm certeza disso? [S/N] ").strip()
            if vc_tem_certeza == "S":
                options[resposta][-1](CONN)
            else:
                print("Dados não excluídos! SEGUINDO CADASTROS...")
        case "6":
            print("Encerrando...")
            break
        case _:
            print("Digite uma opção válida")

crd.close_database(CONN)
