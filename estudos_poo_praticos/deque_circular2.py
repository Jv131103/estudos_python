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


dc = DequeCircular(5)
dc.insert_front(1)
dc.insert_front(2)
dc.insert_front(3)
dc.insert_last(4)
dc.insert_last(5)
print(dc.get_front(), dc.get_rear())
print(dc.delete_front(), dc.delete_last())
print(dc.get_front(), dc.get_rear())
print(dc.vetor)

print()

dc2 = DequeCircular(5)
dc2.insert_last(1)
dc2.insert_last(2)
dc2.insert_front(3)
dc2.delete_last()
dc2.insert_front(4)
print(dc2.get_front(), dc2.get_rear())
print(dc2.vetor)
