def criar_aluno(nome, nota):
    return {
        "nome": nome,
        "nota": nota
    }


aluno = criar_aluno(nome="Ana", nota=8.5)
print(aluno)
print(aluno["nota"])
