class Aluno:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, valor: float):
        if valor < 0 or valor > 10:
            raise ValueError("Nota inválida, deve estar entre 0 e 10.")
        self.notas.append(valor)

    @property
    def media(self) -> float:
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self) -> str:
        m = self.media
        if m >= 7:
            return "Aprovado"
        elif m >= 5:
            return "Recuperação"
        return "Reprovado"

    def __str__(self) -> str:
        return f"Aluno({self.nome}) - Média: {self.media:.2f}"


a = Aluno("Renato")
a.adicionar_nota(8)
a.adicionar_nota(6)
a.adicionar_nota(5)

print(a.media)        # 6.33
print(a.situacao())   # Recuperação
print(a)              # Aluno: Renato | Média: 6.33
