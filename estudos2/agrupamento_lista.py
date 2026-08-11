def resumo_por_turma(alunos):
    d = {}

    # 1°: Pegar chaves
    for aluno in alunos:
        d[aluno['turma']] = {"notas": [], "aprovados": [], "melhor_aluno": ""}

    # 2°: Separar alunos e adicionar notas
    for aluno in alunos:
        t = d[aluno['turma']]
        if aluno["nota"] >= 7:
            t["aprovados"].append(aluno['nome'])

        t["notas"].append(aluno['nota'])

    # 3°: Pegando melhor aluno
    for aluno in alunos:
        turma = aluno['turma']
        if aluno['nota'] == max(d[turma]['notas']):
            d[turma]["melhor_aluno"] = aluno['nome']

    # 4°: Inciar agrupamento final
    resultado = {}
    for turma, dados in d.items():
        media = sum(dados["notas"]) / len(dados["notas"])
        resultado[turma] = {
            "media": round(media, 2),
            "aprovados": dados["aprovados"],
            "melhor_aluno": dados["melhor_aluno"]
        }

    return resultado


alunos = [
    {"nome": "Ana", "nota": 8.5, "turma": "A"},
    {"nome": "Bruno", "nota": 4.0, "turma": "B"},
    {"nome": "Carla", "nota": 9.2, "turma": "A"},
    {"nome": "Diego", "nota": 6.8, "turma": "B"},
    {"nome": "Elis", "nota": 7.0, "turma": "A"},
]


print(resumo_por_turma(alunos))
