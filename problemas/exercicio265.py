class Aluno:
    def __init__(self, nome, nota) -> None:
        self.nome = nome
        self.nota = nota

    def aprovado(self):
        return self.nota >= 6


a1 = Aluno("Mathias do Bope", 10)
print(a1.aprovado())
