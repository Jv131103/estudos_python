class Agenda:
    def __init__(self) -> None:
        self.contatos = {}

    def contato_existe(self, nome):
        return nome in self.contatos

    def adicionar_contato(self, nome, telefone):
        self.contatos[nome] = telefone

    def remover_contato(self, nome):
        if not self.contato_existe(nome):
            print("Nome não existe nos contatos")
            return

        del self.contatos[nome]

    def buscar_contato(self, nome):
        if not self.contato_existe(nome):
            print("Nome não existe nos contatos")
            return
        return self.contatos[nome]

    def listar_contatos(self):
        print("CONTATOS")
        print()
        for pessoa, telefone in self.contatos.items():
            print(f"Pessoa: {pessoa} | Telefone: {telefone}")
            print("--" * 30)


ag = Agenda()
ag.adicionar_contato("Renato", "99999-1234")
ag.adicionar_contato("João", "98888-7777")
print(ag.buscar_contato("Renato"))
ag.remover_contato("João")
ag.listar_contatos()
