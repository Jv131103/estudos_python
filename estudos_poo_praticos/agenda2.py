class Pessoa:
    def __init__(self, nome: str, telefone: str) -> None:
        self.nome = nome.title().strip()
        self.telefones = [telefone]

    def add_telefone(self, telefone: str):
        self.telefones.append(telefone)

    def remove_telefone(self, telefone: str):
        if telefone in self.telefones:
            self.telefones.remove(telefone)


class Agenda:
    def __init__(self) -> None:
        self.contatos: list[Pessoa] = []

    def add(self, pessoa: Pessoa):
        self.contatos.append(pessoa)

    def imprimir_contatos(self):
        print("\nAGENDA")
        print("++" * 20)
        for pessoa in self.contatos:
            print(f"Nome: {pessoa.nome}")
            print("Telefones:")
            for idx, tel in enumerate(pessoa.telefones, start=1):
                print(f"  {idx} - {tel}")
            print("--" * 20)


if __name__ == "__main__":
    c1 = Pessoa("Clementina", "1234567")
    c1.add_telefone("2345678")

    c2 = Pessoa("Joaquim Pinto", "54564646")
    c3 = Pessoa("Pricila Luiza", "9887687")

    agenda = Agenda()
    agenda.add(c1)
    agenda.add(c2)
    agenda.add(c3)

    agenda.imprimir_contatos()
