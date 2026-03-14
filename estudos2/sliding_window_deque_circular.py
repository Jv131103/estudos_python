class DequeCircular:

    def __init__(self, k):
        self.vetor = [None] * k
        self.head = 0
        self.tail = 0
        self.count = 0
        self.tamanho = k

    def insert_last(self, valor):
        if self.count == self.tamanho:
            return False

        self.vetor[self.tail] = valor
        self.tail = (self.tail + 1) % self.tamanho
        self.count += 1
        return True

    def insert_front(self, valor):
        if self.count == self.tamanho:
            return False

        self.head = (self.head - 1) % self.tamanho
        self.vetor[self.head] = valor
        self.count += 1
        return True

    def delete_front(self):
        if self.count == 0:
            return False

        self.head = (self.head + 1) % self.tamanho
        self.count -= 1
        return True

    def delete_last(self):
        if self.count == 0:
            return False

        self.tail = (self.tail - 1) % self.tamanho
        self.count -= 1
        return True

    def get_front(self):
        if self.count == 0:
            return None
        return self.vetor[self.head]

    def get_rear(self):
        if self.count == 0:
            return None
        return self.vetor[(self.tail - 1) % self.tamanho]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.tamanho

    def __str__(self):
        elementos = []
        for i in range(self.count):
            pos = (self.head + i) % self.tamanho
            elementos.append(str(self.vetor[pos]))
        return "[" + ", ".join(elementos) + "]"


def sliding_window(array, k):
    if not array or k <= 0:
        return []

    if k > len(array):
        return [max(array)]

    resultado = []
    d = DequeCircular(len(array))

    for i in range(len(array)):

        while not d.is_empty() and d.get_front() <= i - k:
            d.delete_front()

        while not d.is_empty() and array[d.get_rear()] < array[i]:
            d.delete_last()

        d.insert_last(i)

        if i >= k - 1:
            resultado.append(array[d.get_front()])

    return resultado


print(sliding_window([1, 2, 3, 4, 5], 3))
print(sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
