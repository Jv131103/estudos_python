class HashTable:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        if self.size / self.capacity >= 0.75:
            self._rehash()

        index = self._hash(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])
        self.size += 1

    def get(self, key):
        index = self._hash(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def _rehash(self):
        print(f"Rehash: {self.capacity} -> {self.capacity * 2}")

        old_table = self.table
        self.capacity *= 2
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)


ht = HashTable()

for i in range(10):
    ht.put(f"chave{i}", i)
    print(f"inseriu chave{i}")
