class Aluno:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        if not isinstance(nota, (int, float)):
            raise ValueError("Nota precisa ser do tipo numérico")

        if not (0 <= nota <= 10):
            raise ValueError("Nota precisa estar entre [0, 10]")

        self.notas.append(nota)

    def media(self):
        if not self.notas:
            raise ValueError(f"Sem notas para Aluno {self.nome}")
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        media = self.media()

        if media >= 7:
            return "Aprovado"
        return "Reprovado"

    def __str__(self) -> str:
        return f"Boletin do aluno {self.nome}: (media={self.media():.2f}, situacao={self.situacao()})"


a1 = Aluno("João")
a1.adicionar_nota(8)
a1.adicionar_nota(6)
a1.adicionar_nota(7)
print(a1)
