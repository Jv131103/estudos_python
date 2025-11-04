"""
Crie class Aluno com nome, nota e método aprovado() que retorna True/False.
"""


class Aluno:
    def __init__(self, nome: str, nota: float) -> None:
        self.nome: str = nome
        self.nota: float = nota

    def aprovado(self):
        return self.nota >= 6


if __name__ == "__main__":
    marcin3bola = Aluno("Marcinho 3 bola", 5)
    print(marcin3bola.aprovado())

    maira = Aluno("Maira Pinto", 10)
    print(maira.aprovado())
