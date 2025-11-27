from datetime import datetime


class Estoque:
    def __init__(self) -> None:
        # cada item: [nome, qtd, preco, descricao, data_registro]
        self.estoque = []

    def cadastrar_produto(self, nome, qtd, preco, descricao):
        pos_produto = self.procurar_produto(nome)
        if pos_produto is not None:
            print(f"Produto '{nome}' já cadastrado!")
            return

        data_registro = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.estoque.append([nome, qtd, preco, descricao, data_registro])
        print(f"Produto '{nome}' cadastrado com sucesso!")

    def remover_produto(self, nome):
        pos_produto = self.procurar_produto(nome)
        if pos_produto is None:
            print("Produto não encontrado")
            return

        removido = self.estoque.pop(pos_produto)
        print(f"Produto '{removido[0]}' removido com sucesso!")

    def procurar_produto(self, nome):
        nome = nome.lower()
        for i, item in enumerate(self.estoque):
            nome_item = item[0].lower()
            if nome_item == nome:
                return i
        return None

    def retornar_status_procura_produto(self, nome):
        pos = self.procurar_produto(nome)
        if pos is None:
            print("Produto não encontrado")
            return
        print(f"Produto '{nome}' encontrado na posição {pos + 1}")

    def ver_produtos(self):
        print("**" * 30)
        print("\t\t\tESTOQUE")
        print("**" * 30)

        if not self.estoque:
            print("Nenhum produto cadastrado.")
            print("**" * 30)
            return

        for item in self.estoque:
            nome, qtd, preco, descricao, data_registro = item
            print(f"Produto: {nome}")
            print("--" * 30)
            print(f"\tQuantidade em estoque: {qtd}")
            print(f"\tPreço do produto: R$ {preco:.2f}")
            print(f"\tDescrição do produto: {descricao}")
            print(f"\tData de registro: {data_registro}")
            print("**" * 30)


def gerar_opcoes():
    itens_das_opcoes = [
        "Cadastrar produto",
        "Remover produto",
        "Procurar produto",
        "Ver produtos",
        "Sair"
    ]
    for idx in range(1, 6):
        print(f"{idx} - {itens_das_opcoes[idx - 1]}")


def main():
    estoque = Estoque()
    while True:
        print("==" * 30)
        gerar_opcoes()
        print("==" * 30)
        opc = input("Escolha a sua opção: ")
        print()

        match opc:
            case "1":
                nome = input("Nome do produto: ")
                qtd = int(input("Quantidade do produto: "))
                preco = float(input("Preço do produto: ").replace(",", "."))
                descricao = input("Descrição do produto: ")
                estoque.cadastrar_produto(nome, qtd, preco, descricao)
                print("--" * 30)

            case "2":
                nome = input("Nome do produto a remover: ")
                estoque.remover_produto(nome)
                print("--" * 30)

            case "3":
                nome = input("Nome do produto a procurar: ")
                estoque.retornar_status_procura_produto(nome)
                print("--" * 30)

            case "4":
                estoque.ver_produtos()
                input("PRESSIONE ENTER PARA CONTINUAR...")

            case "5":
                print("FIM!")
                break

            case _:
                print("ESCOLHA INVÁLIDA, DIGITE APENAS AS OPÇÕES ACIMA")
                print("--" * 30)


if __name__ == "__main__":
    main()
