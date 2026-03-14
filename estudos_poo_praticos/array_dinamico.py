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
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity


if __name__ == "__main__":
    array = DynamicArray()
    array.append(1)
    array.append(1)
    array.append(1)
    array.append(1)
    print(array.data)
