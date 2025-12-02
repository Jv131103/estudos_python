class TabelaHash:
    def __init__(self, tamanho_inicial=8):
        self._tabela = [[] for _ in range(tamanho_inicial)]
        self._quantidade = 0

    def __setitem__(self, chave, valor):
        indice = hash(chave) % len(self._tabela)
        bucket = self._tabela[indice]

        for i, (ch, val) in enumerate(bucket):
            if ch == chave:
                bucket[i] = (chave, valor)
                return

        bucket.append((chave, valor))
        self._quantidade += 1

    def __getitem__(self, chave):
        indice = hash(chave) % len(self._tabela)
        bucket = self._tabela[indice]

        for ch, val in bucket:
            if ch == chave:
                return val

        raise KeyError(f"Chave não encontrada: {chave}")

    def __delitem__(self, chave):
        indice = hash(chave) % len(self._tabela)
        bucket = self._tabela[indice]

        for i, (ch, val) in enumerate(bucket):
            if ch == chave:
                bucket.pop(i)
                self._quantidade -= 1
                return

        raise KeyError(f"Chave não encontrada: {chave}")

    def __contains__(self, chave):
        try:
            self[chave]
            return True
        except KeyError:
            return False

    def __len__(self):
        return self._quantidade

    def __repr__(self):
        itens = []
        for bucket in self._tabela:
            for chave, valor in bucket:
                itens.append(f"{chave!r}: {valor!r}")
        return "{ " + ", ".join(itens) + " }"


t = TabelaHash()

t["nome"] = "Renato"
t["idade"] = 18
t["cidade"] = "São Paulo"

print(t["nome"])       # Renato
print("idade" in t)    # True

del t["idade"]
print("idade" in t)    # False

print(t)   # { 'nome': 'Renato', 'cidade': 'São Paulo' }
