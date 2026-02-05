"""
Crie uma classe Aluno com:

    nome

    nota

    método aprovado()

        retorna "Aprovado" se nota ≥ 6

        senão "Reprovado"
"""


class Aluno:
    def __init__(self, nome, nota) -> None:
        if not 0 <= nota <= 10:
            raise ValueError("Nota deve estar entre 0 e 10")
        self.nome = nome
        self.nota = nota

    def aprovado(self):
        return "Aprovado" if self.nota >= 6 else "Reprovado"

    def __str__(self):
        return f"{self.nome} - Nota: {self.nota} - {self.aprovado()}"


a1 = Aluno("Gilberto", 10)
print(a1.aprovado())

a2 = Aluno("Gilbert", 5)
print(a2.aprovado())

a3 = Aluno("Mathias", 6)
print(a3.aprovado())
