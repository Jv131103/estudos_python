from abc import ABC, abstractmethod


class Personagem(ABC):
    def __init__(self, nome, hp) -> None:
        self.nome = nome
        self.hp = hp

    @abstractmethod
    def status(self):
        print(f"nome={self.nome} | hp={self.hp}")


class Guerreiro(Personagem):
    def __init__(self, nome, hp) -> None:
        super().__init__(nome, hp)

    def ataque(self, personagem):
        if not isinstance(personagem, Personagem):
            raise ValueError("Personagem precisa ser do tipo Personagem")

        if self.hp <= 0:
            print(f"{self.nome} está morto!")
            return

        if personagem.hp <= 0:
            print(f"{personagem.nome} está morto")
            return

        print(f"{self.nome} atacou {personagem.nome} causando 30 de dano!")
        personagem.hp -= 30

    def status(self):
        return super().status()


class Mago(Personagem):
    def __init__(self, nome, hp) -> None:
        super().__init__(nome, hp)

    def magia(self, personagem):
        if not isinstance(personagem, Personagem):
            raise ValueError("Personagem precisa ser do tipo Personagem")

        if self.hp <= 0:
            print(f"{self.nome} está morto!")
            return

        if personagem.hp <= 0:
            print(f"{personagem.nome} está morto")
            return

        print(f"{self.nome} conjurou magia em {personagem.nome} causando 50 de dano!")
        personagem.hp -= 50
        self.hp -= 10

    def status(self):
        return super().status()


g = Guerreiro("Aragorn", 100)
m = Mago("Gandalf", 80)
g.ataque(m)
m.status()
m.magia(g)
m.status()
