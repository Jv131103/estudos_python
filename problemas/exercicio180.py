from pathlib import Path


class MiniAgenda:
    def __init__(self) -> None:
        self.arquivo = Path().cwd() / 'arquivos' / 'agenda.txt'

    def adicionar_contato(self, nome, telefone, email):
        string_retorno = f"{nome};{telefone};{email}\n"

        with open(self.arquivo, "a", encoding="utf-8") as arquivo:
            arquivo.write(string_retorno)

    def listar_contatos(self):
        print("++" * 30)
        print("\t\t\tCONTATOS")
        print("++" * 30)
        with open(self.arquivo, 'r', encoding="utf-8") as arquivo:
            for dado in arquivo.readlines():
                nome, telefone, email = dado.split(";")
                print(f"Nome contato: {nome}")
                print(f"Telefone contato: {telefone}")
                print(f"email contato: {email}")

    def buscar_contato(self, nome_parcial):
        print("++" * 30)
        print(f"\t\tDados Encontrados para {nome_parcial}")
        print("++" * 30)
        with open(self.arquivo, 'r', encoding="utf-8") as arquivo:
            for dado in arquivo.readlines():
                if nome_parcial in dado:
                    nome, telefone, email = dado.split(";")
                    print(f"Nome contato: {nome}")
                    print(f"Telefone contato: {telefone}")
                    print(f"email contato: {email}")

    def remover_contato(self, nome_exato):
        with open(self.arquivo, 'r', encoding="utf-8") as arquivo:
            dados = arquivo.readlines()

        with open(self.arquivo, 'w', encoding="utf-8") as arquivo:
            for dado in dados:
                if nome_exato not in dado:
                    arquivo.write(dado)

    def atualizar_contato(self, nome_exato, telefone=None, email=None):
        novo_texto = []

        with open(self.arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                if nome_exato in linha:
                    _, telefone_antigo, email_antigo = linha.split(";")
                    linha = linha.replace(telefone_antigo, str(telefone)).replace(email_antigo, str(email) + "\n")
                novo_texto.append(linha)

        with open(self.arquivo, "w", encoding="utf-8") as f:
            f.writelines(novo_texto)


agenda = MiniAgenda()
agenda.adicionar_contato("Joao Carlucho", "76765656", "caluchoso@email.com")
agenda.adicionar_contato("Caio Pinto", "33242333", "caio@pinto.com")
agenda.adicionar_contato("Joao", "123456789", "joao@email.com")
agenda.adicionar_contato("Maria", "987654321", "teste@maria.com")
agenda.adicionar_contato("Joao Carlos", "9765438", "joao@carlos.com")
agenda.adicionar_contato("Lauro", "976543123", "lauro@pinto.com")
agenda.listar_contatos()
agenda.buscar_contato("Joao")
agenda.remover_contato("Maria")
agenda.atualizar_contato("Joao", "67574664", "novo_email@gmail.com")
