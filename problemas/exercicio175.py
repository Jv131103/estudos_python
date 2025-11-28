def media_ponderada(alunos):
    soma_peso = 0
    soma_nota_peso = 0

    for aluno in alunos:
        _, nota, peso = aluno
        soma_peso += peso
        soma_nota_peso += nota * peso

    return soma_nota_peso / soma_peso


alunos = [
    ("Renato", 8.0, 3),
    ("Maria", 9.5, 2),
    ("João", 7.0, 5)
]
print(media_ponderada(alunos))
