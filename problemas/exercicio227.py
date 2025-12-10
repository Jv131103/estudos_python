class Aluno:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, valor):
        self.notas.append(valor)

    @property
    def media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        if self.media >= 7:
            return "Aprovado"
        elif 5 <= self.media < 7:
            return "Recuperação"
        else:
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
