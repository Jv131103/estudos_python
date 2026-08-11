def resumo_por_turma(alunos):
    d = {}

    for aluno in alunos:
        turma = aluno['turma']
        if turma not in d:
            d[turma] = {"notas": [], "aprovados": [], "melhor_aluno": None, "melhor_nota": float("-inf")}

        t = d[turma]
        t["notas"].append(aluno['nota'])

        if aluno['nota'] >= 7:
            t["aprovados"].append(aluno['nome'])

        if aluno['nota'] > t["melhor_nota"]:
            t["melhor_nota"] = aluno['nota']
            t["melhor_aluno"] = aluno['nome']

    resultado = {}
    for turma, dados in d.items():
        resultado[turma] = {
            "media": round(sum(dados["notas"]) / len(dados["notas"]), 2),
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
