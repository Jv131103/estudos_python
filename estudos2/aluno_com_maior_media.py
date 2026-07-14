alunos = [
    {"nome": "Ana", "media": 8},
    {"nome": "Carlos", "media": 7},
    {"nome": "Maria", "media": 9},
]

# Heurística: ordenar pela maior média
alunos.sort(key=lambda aluno: aluno["media"], reverse=True)

print(alunos[0])
