class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome: str = nome


class Agenda:
    def __init__(self, pessoa: Pessoa) -> None:
        self.pessoa: Pessoa = pessoa
        self.contatos: dict = {}
        self.nome = ""
        self.telefone = ""

    def __edit(self, nome="", telefone=""):
        self.nome = nome.title().strip()
        self.telefone = telefone.strip()

    def add(self, nome: str, telefone: str):
        self.__edit(nome, telefone)
        if self.contatos.get(self.nome):
            self.contatos[self.nome].append(self.telefone)
            return
        self.contatos[self.nome] = [self.telefone]

    def remove_contato(self, nome: str):
        self.__edit(nome)
        if self.contatos.get(self.nome):
            del self.contatos[self.nome]
            return
        print(f"{self.nome} não encontrado na lista")

    def remove_telefone(self, nome, telefone):
        self.__edit(nome, telefone)
        if self.contatos.get(self.nome):
            self.contatos[self.nome].remove(self.telefone)
            return
        print(f"{self.telefone} não encontrado para o contato {nome}")

    def imprimir_contatos(self):
        print("++" * 30)
        print(f"\tContato de {self.pessoa.nome}")
        for nome, contatos in self.contatos.items():
            print("==" * 30)
            print(f"Contato: {nome}")
            print("==" * 30)
            print("Telefone(s):")
            print("--" * 30)
            for idx, contato in enumerate(contatos, start=1):
                print(f"Tel {idx}: {contato}")
                print("--" * 30)


if __name__ == "__main__":
    anathalia = Pessoa("Anathalia dos anjos")
    agenda_anathalia = Agenda(anathalia)
    agenda_anathalia.add("Clementina", "1234567")
    agenda_anathalia.add("Clementina", "2345678")
    agenda_anathalia.add("Joaquim Pinto", "54564646")
    agenda_anathalia.add("Pricila Luiza", '9887687')
    agenda_anathalia.imprimir_contatos()
    print()
    agenda_anathalia.remove_contato("Joaquim Pinto")
    agenda_anathalia.remove_telefone("Clementina", "2345678")
    agenda_anathalia.imprimir_contatos()
