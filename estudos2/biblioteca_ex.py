acervo = {}  # chave: ISBN, valor: dicionário do livro


def esta_em_acervo(isbn, acervo):
    return isbn in acervo


def cadastrar(acervo, isbn, titulo, autor, ano):
    livro = {}
    livro["titulo"] = titulo
    livro["autor"] = autor
    livro["ano"] = ano
    livro["disponivel"] = True
    acervo[isbn] = livro
    print(f"Livro {titulo} cadastrado com sucesso!")
    print(f"ISBN: {isbn}")


def emprestar(acervo, isbn):
    livro = acervo[isbn]

    if not livro["disponivel"]:
        print("Livro já encontra emprestado!")
        return

    livro["disponivel"] = False
    print(f"Livro {livro['titulo']} emprestado com sucesso!")
    print(f"ISBN: {isbn}")


def devolver(acervo, isbn):
    livro = acervo[isbn]

    if livro["disponivel"]:
        print("Livro já encontra-se disponível!")
        return

    livro["disponivel"] = True
    print(f"Livro {livro['titulo']} devolvido com sucesso!")
    print(f"ISBN: {isbn}")


def buscar(acervo, termo):
    encontrou = False
    for dados in acervo.values():
        if termo.lower() in dados["autor"].lower() or termo.lower() in dados["titulo"].lower():
            encontrou = True
            saida = "Disponível" if dados["disponivel"] else "Não Disponível"
            print(f"{dados['titulo']} - {dados['autor']} ({dados['ano']}) [{saida}]")

    if not encontrou:
        print(f"Termo {termo} não encontrado ...")

    return encontrou


def listar(acervo):
    for isbn, informacao in acervo.items():
        print("==" * 20)
        print(f"ISBN.......: {isbn}")
        print(f"Título.....: {informacao['titulo']}")
        print(f"Autor......: {informacao['autor']}")
        print(f"Ano........: {informacao['ano']}")
        print(f"Disponível.: {informacao['disponivel']}")


def input_tratado(msg, tipo):
    while True:
        valor = input(msg).strip().title()
        if not valor:
            print(f"{tipo} não pode ser vazio!")
            continue
        return valor


def menu():
    print("======= BIBLIOTECA PY =======")
    opcoes = [
        ["1", "Cadastrar livro"],
        ["2", "Emprestar livro"],
        ["3", "Devolver livro"],
        ["4", "Buscar"],
        ["5", "Listar acervo"],
        ["0", "Sair"],
    ]

    for opc in opcoes:
        print(f"[{opc[0]}] {opc[1]}")
    print()

    while True:
        opc = input(">> ")

        if opc == "0":
            print()
            print("FIM DO PROGRAMA!")
            print()
            break
        elif opc == "1":
            isbn = input_tratado("ISBN: ", "ISBN")
            if esta_em_acervo(isbn, acervo):
                print("==" * 20)
                print("Livro já registrado!")
                continue
            titulo = input_tratado("Título: ", "Título")
            autor = input_tratado("Autor: ", "Autor")
            ano = input_tratado("Ano: ", "Ano")
            print("==" * 20)
            cadastrar(acervo, isbn, titulo, autor, ano)
        elif opc == "2":
            isbn = input_tratado("ISBN: ", "ISBN")
            if not esta_em_acervo(isbn, acervo):
                print("==" * 20)
                print("Livro não encontrado!")
                continue
            print("==" * 20)
            emprestar(acervo, isbn)
        elif opc == "3":
            isbn = input_tratado("ISBN: ", "ISBN")
            if not esta_em_acervo(isbn, acervo):
                print("==" * 20)
                print("Livro não encontrado!")
                continue
            print("==" * 20)
            devolver(acervo, isbn)
        elif opc == "4":
            print("==" * 20)
            busca = input_tratado("Buscar: ", "Busca de autor")
            buscar(acervo, busca)
        elif opc == "5":
            listar(acervo)
        else:
            print("==" * 20)
            print("Opção inválida, digite apenas as citadas na nossa tabela")

        print("==" * 20)
        print()


if __name__ == "__main__":
    menu()
