"""
Faça um programa que:

    Crie um dicionário com tarefas pendentes

    Use popitem para remover tarefas uma a uma

    Mostre a tarefa removida e o estado atual do dicionário

    Continue até o dicionário ficar vazio

DICAS

    popitem remove o último item inserido

    Pense nisso como uma pilha de tarefas
"""

tarefas = {
    "1": "Estudar programação",
    "2": "Estudar Biologia",
    "3": "Ler a bíblia",
    "4": "Ler e estudar tomismo e agostinianismo",
    "5": "Estudar Estoicismo",
    "6": "Praticar poesia",
    "7": "Se entreter com algo"
}


def remover(dicionario):
    return dicionario.popitem()


while len(tarefas) > 0:
    print(tarefas)
    dado = input("Remover? [S/N] ").upper()
    if dado == "N":
        break

    remover(tarefas)

print("FIM")
