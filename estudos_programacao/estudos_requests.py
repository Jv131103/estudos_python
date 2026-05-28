import requests


# Parte 1
def buscar_cep(cep: str) -> None:
    if len(cep) != 8:
        print("CEP INVÁLIDO, PRECISA TER UM TAMANHO DE 8 CARACTERES")
    elif not cep.isnumeric():
        print("CEP PRECISA SER NUMÉRICO")
    else:
        print()
        print(f"Buscando cep {cep}...")
        print()
        try:
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            if not response.ok:
                print(f"Erro ao analisar CEP: {response.json()}")
                return

            dados = response.json()
            if dados.get("erro"):
                print("CEP não encontrado!")
                return

            print("====== CONSULTA CEP ======")
            print(f"CEP: {dados['cep']}")
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
        except requests.exceptions.ConnectionError:
            print("Erro de conexão!")
            return
        except requests.exceptions.Timeout:
            print("Tempo de resposta esgotado!")
            return


# Parte 2
def buscar_posts(quantidade=5):
    print("======= POSTS =======")
    for _id in range(1, quantidade + 1):
        post = buscar_post_por_id(_id)
        if not post:
            print("Id não encontrado para post")
            return
        print(f"#{post['id']} - {post['title']}")
        print(f"    Corpo: {post['body']}")
        print()


def buscar_post_por_id(id, saida=False):
    try:
        url = f"https://jsonplaceholder.typicode.com/posts/{id}"
        response = requests.get(url, timeout=5)
        post = response.json()
        if saida and post:
            print("======= POST =======")
            print(f"#{post['id']} - {post['title']}")
            print(f"    Corpo: {post['body']}")
            print()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Erro de conexão!")
        return {}
    except requests.exceptions.Timeout:
        print("Tempo de resposta esgotado!")
        return {}


def trata_input(msg):
    while True:
        inp = input(msg).strip().upper().replace("-", "")
        if not inp:
            print("Digite uma opção válida!")
            continue
        return inp


def trata_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um valor numérico inteiro")


def executar_cep():
    cep = trata_input("Digite um CEP: ")
    buscar_cep(cep)


def executar_posts():
    escolha = [
        ["1", "POR ID"],
        ["2", "PRIMEIROS N ID"],
        ["0", "SAIR"]
    ]
    for opc1, opc2 in escolha:
        print(f"{opc1} - {opc2}")

    while True:
        print()
        opc = trata_input(">>> ")
        if opc in escolha[0]:
            _id = trata_int("ID a consultar: ")
            buscar_post_por_id(_id, saida=True)
        elif opc in escolha[1]:
            qtd = trata_int("Quantidade de POSTS: ")
            buscar_posts(qtd)
        elif opc in escolha[2]:
            print("Encerrando busca de POSTS")
        else:
            print("Opção inválida, digite apenas as opções sugeridas")
            continue
        print("Voltando ao menu...")
        break


def menu():
    consultas = [
        ["1", "CEP"],
        ["2", "POSTS"],
        ["0", "SAIR"]
    ]
    for opc1, opc2 in consultas:
        print(f"{opc1} - {opc2}")

    while True:
        print()
        opc = trata_input(">>> ")
        if opc in consultas[0]:
            executar_cep()
        elif opc in consultas[1]:
            executar_posts()
        elif opc in consultas[2]:
            print("ENCERRANDO...")
            break
        else:
            print("OPÇÃO INVÁLIDA!")


menu()
# buscar_cep("01001-000")
# buscar_cep("01310-100")
# buscar_posts()
