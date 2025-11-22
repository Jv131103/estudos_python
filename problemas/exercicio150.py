class Pessoa:
    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

    def mostrar_nome(self):
        print(self.nome)

    def mostrar_email(self):
        print(self.email)

    def mostrar_senha(self):
        print(self.senha)


pessoa = Pessoa("JOÃO", "joao@joao.com.br", "acesso123")
pessoa.mostrar_nome()
pessoa.mostrar_email()
pessoa.mostrar_senha()
