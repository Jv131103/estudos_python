alunos = [
    {"nome": "Ana", "notas": [8, 7, 9]},
    {"nome": "Marri", "notas": [5, 7, 3]},
    {"nome": "Maria", "notas": [10, 7, 10]},
]


def analise_notas(alunos):
    maior_nota = 0
    aluno_nota_max = ""
    novo = {}
    novo["aprovados"] = []

    for aluno in alunos:
        aluno['media'] = sum(aluno['notas']) // len(aluno['notas'])
        if aluno['media'] > maior_nota:
            maior_nota = aluno['media']
            aluno_nota_max = aluno['nome']

        if aluno['media'] >= 6:
            novo['aprovados'].append(aluno)

    novo["media_maior"] = aluno_nota_max
    novo['aprovados'] = sorted(
        novo['aprovados'],
        key=lambda x: x['media']
    )
    return novo


print(analise_notas(alunos))
