class Cache:
    def __init__(self) -> None:
        self.capacidade = 3
        self.cache = {}
        self.ordem = []  # Lista para controlar quem foi usado por último

    def get(self, chave):
        if chave not in self.cache:
            return None  # Ou levanta erro, mas None é mais seguro

        # Como a chave foi usada, ela vai para o final da lista de prioridade
        self.ordem.remove(chave)
        self.ordem.append(chave)

        return self.cache[chave]

    def put(self, chave, valor):
        # Cenário 1: A chave já existe, só vamos atualizar
        if chave in self.cache:
            self.ordem.remove(chave)

        # Cenário 2: Chave nova E o cache tá lotado!
        elif len(self.cache) >= self.capacidade:
            # O primeiro elemento da lista ([0]) é o mais antigo (LRU)
            lru_chave = self.ordem.pop(0)
            del self.cache[lru_chave]  # Remove ele do dicionário de vez

        # Agora salvamos o valor novo e jogamos a chave pro final da lista
        self.cache[chave] = valor
        self.ordem.append(chave)


# --- TESTANDO O SEU CACHE NOVO ---
c = Cache()

c.put("A", 1)  # Cache: {'A': 1} | Ordem: ['A']
c.put("B", 2)  # Cache: {'A': 1, 'B': 2} | Ordem: ['A', 'B']
c.put("C", 3)  # Cache: {'A': 1, 'B': 2, 'C': 3} | Ordem: ['A', 'B', 'C']

# Agora o cache está LOTADO. Se colocarmos o 'D', o 'A' (mais antigo) deve sumir:
c.put("D", 4)  # Remove 'A'!

print(c.get("A"))  # Retorna None (já era)
print(c.get("B"))  # Retorna 2. E agora o 'B' vai pro final da ordem!

# Como o 'B' foi usado no get, a ordem virou ['C', 'D', 'B'].
# Se adicionarmos o 'E', quem roda agora é o 'C'!
c.put("E", 5)

print(c.get("C"))  # Retorna None (o C rodou!)
print(c.get("D"))  # Retorna 4
