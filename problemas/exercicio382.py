class CacheLRU:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.cache = {}        # chave -> valor
        self.ordem = []        # LRU -> MRU

    def get(self, chave):
        if chave not in self.cache:
            return None

        # marca como mais recente
        self.ordem.remove(chave)
        self.ordem.append(chave)

        return self.cache[chave]

    def put(self, chave, valor):
        if chave in self.cache:
            # atualiza e marca como recente
            self.cache[chave] = valor
            self.ordem.remove(chave)
            self.ordem.append(chave)
            return

        if len(self.cache) == self.capacidade:
            # remove o menos recente
            lru = self.ordem.pop(0)
            del self.cache[lru]

        self.cache[chave] = valor
        self.ordem.append(chave)


cache = CacheLRU(3)
cache.put("A", 1)
cache.put("B", 2)
cache.put("C", 3)

cache.get("A")        # A vira mais recente
cache.put("D", 4)    # remove B (menos recente)

print(cache.cache)
print(cache.ordem)
