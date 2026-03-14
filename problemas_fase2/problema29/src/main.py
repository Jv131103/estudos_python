class RingBuffer:

    def __init__(self, tamanho):
        self.buffer = [None] * tamanho
        self.index = 0
        self.tamanho = tamanho
        self.count = 0
        self.snapshots = []

    def adicionar(self, log):

        self.buffer[self.index] = log
        self.index = (self.index + 1) % self.tamanho

        if self.count < self.tamanho:
            self.count += 1

    def get_logs(self):

        logs = []

        start = (self.index - self.count) % self.tamanho

        for i in range(self.count):
            pos = (start + i) % self.tamanho
            logs.append(self.buffer[pos])

        return logs

    def snapshot(self):
        self.snapshots.append(self.get_logs().copy())

    def get_snapshots(self):
        return self.snapshots

    def is_full(self):
        return self.count == self.tamanho


if __name__ == "__main__":
    r = RingBuffer(4)

    r.adicionar("A")
    r.adicionar("B")
    r.adicionar("C")
    r.adicionar("D")

    r.snapshot()

    r.adicionar("E")
    r.adicionar("F")

    r.snapshot()

    print("Estado atual:")
    print(r.get_logs())

    print("\nSnapshots:")
    print(r.get_snapshots())
