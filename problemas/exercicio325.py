class Curso:
    def __init__(self, nome: str, carga_horaria: int) -> None:
        if carga_horaria <= 0:
            raise ValueError("carga_horaria deve ser > 0")
        self.nome = nome
        self.carga_horaria = carga_horaria


class Aluno:
    def __init__(self, nome: str, matricula: str) -> None:
        self.nome = nome
        self.matricula = matricula
        self.cursos: list[Curso] = []

    def validar_matricula(self) -> bool:
        return (
            len(self.matricula) == 8
            and self.matricula.startswith("2025")
            and self.matricula[4:].isdigit()
        )

    def matricular(self, curso: Curso) -> bool:
        if not self.validar_matricula():
            print("Matrícula inválida. Use o formato 2025XXXX (dígitos).")
            return False

        if curso in self.cursos:
            print("Aluno já matriculado nesse curso.")
            return False

        self.cursos.append(curso)
        return True

    def desmatricular(self, nome_do_curso: str) -> bool:
        for i, curso in enumerate(self.cursos):
            if curso.nome == nome_do_curso:
                self.cursos.pop(i)
                return True

        print("Aluno não está matriculado nesse curso.")
        return False

    def listar_cursos(self) -> list[str]:
        return [c.nome for c in self.cursos]

    def total_carga_horaria(self) -> int:
        return sum(c.carga_horaria for c in self.cursos)


biologia = Curso("Biologia", 2000)
matematica = Curso("Matemática", 3000)
ciencia_da_computacao = Curso("Ciência da Computação", 3000)
logica = Curso("Lógica Matemática", 1000)

aluno = Aluno("João", "20251234")
aluno.matricular(biologia)
aluno.matricular(matematica)
aluno.matricular(ciencia_da_computacao)
aluno.matricular(logica)
aluno.listar_cursos()
print(aluno.total_carga_horaria())
aluno.desmatricular(biologia)
print(aluno.total_carga_horaria())
