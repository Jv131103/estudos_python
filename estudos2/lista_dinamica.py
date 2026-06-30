class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize()

        self.data[self.size] = value
        self.size += 1

    def _resize(self):
        print(f"Redimensionando: {self.capacity} -> {self.capacity * 2}")

        new_data = [None] * (self.capacity * 2)

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity *= 2

    def __repr__(self):
        return str(self.data[:self.size])


arr = DynamicArray()

for i in range(10):
    arr.append(i)
    print(arr, "capacidade:", arr.capacity)
