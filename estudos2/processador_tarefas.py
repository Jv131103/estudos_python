from random import randint


class PriorityQueue:
    def __init__(self):
        self.dados = []

    def push(self, valor, prioridade):
        novo = (prioridade, valor)

        if not self.dados:
            self.dados.append(novo)
            return

        for i in range(len(self.dados)):
            if prioridade > self.dados[i][0]:
                self.dados.insert(i, novo)
                return

        self.dados.append(novo)

    def pop(self):
        if not self.dados:
            raise IndexError("fila vazia")

        return self.dados.pop(0)


def gerenciador_tarefas():
    tarefas = [
        "tarefa db_system.db prioridade 5",
        "tarefa system_os.exe prioridade 2",
        "tarefa gcc.exe prioridade 9",
        "tarefa anti_malware.py prioridade 3",
        "tarefa heap_animals.exe prioridade 10",
        "tarefa saas_enterprise.exe priridade 11",
        "tarefa manager_os.assembly prioridade 1",
        "tarefa abstract_system_development.exe priority 5"
    ]

    fp = PriorityQueue()

    for tarefa in tarefas:
        dados = tarefa.split()
        nome = dados[1]
        prioridade = int(dados[-1])
        fp.push(nome, prioridade)

    largura_processo = max(len(m) for m in tarefas)
    largura_prioridade = 12
    largura_pid = 8

    largura_total = largura_processo + largura_prioridade + largura_pid + 10

    print("=" * largura_total)
    print(
        f"| {'Processo':<{largura_processo}} "
        f"| {'Prioridade':^{largura_prioridade}} "
        f"| {'PID':^{largura_pid}} |"
    )
    print("=" * largura_total)

    while fp.dados:
        prioridade, nome = fp.pop()
        pid = randint(1, 5000)

        print(
            f"| {nome:<{largura_processo}} "
            f"| {prioridade:^{largura_prioridade}} "
            f"| {pid:^{largura_pid}} |"
        )

        print("-" * largura_total)


gerenciador_tarefas()
