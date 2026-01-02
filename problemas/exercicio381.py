class FilaPrioridade:
    def __init__(self):
        self.fila = []
        self.sequencia = 0

    def push(self, valor, prioridade):
        self.fila.append([prioridade, self.sequencia, valor])
        self.sequencia += 1

    def pop(self):
        if not self.fila:
            raise IndexError("pop de fila vazia")

        melhor_idx = 0
        melhor_prio, melhor_seq, _ = self.fila[0]

        for i, (prio, seq, val) in enumerate(self.fila):
            if (prio < melhor_prio) or (prio == melhor_prio and seq < melhor_seq):
                melhor_idx = i
                melhor_prio, melhor_seq = prio, seq

        return self.fila.pop(melhor_idx)[2]

    def vazia(self):
        return len(self.fila) == 0

    def __str__(self):
        return str(self.fila)


fp = FilaPrioridade()
fp.push('A', 2)
fp.push('B', 1)
fp.push('C', 1)
print(fp)
fp.pop()
print(fp)
