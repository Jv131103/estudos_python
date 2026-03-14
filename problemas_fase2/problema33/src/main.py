class ArrayDinamico:

    def __init__(self):
        self._capacity = 1
        self._size = 0
        self.data = [None] * self._capacity

    def append(self, value):

        if self._size == self._capacity:
            self._resize()

        self.data[self._size] = value
        self._size += 1

    def _resize(self):

        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity

        for i in range(self._size):
            new_data[i] = self.data[i]

        self.data = new_data
        self._capacity = new_capacity

    def get(self, indice):

        if indice < 0 or indice >= self._size:
            raise IndexError("indice fora do array")

        return self.data[indice]

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def __str__(self):
        return str(self.data[:self._size])


if __name__ == "__main__":
    a = ArrayDinamico()

    a.append(1)
    a.append(2)
    a.append(3)

    print(a)
    print(a.size())
    print(a.capacity())
