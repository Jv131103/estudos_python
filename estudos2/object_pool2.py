class ObjectPool:
    def __init__(self) -> None:
        self.pool = []
        self.capacidade_maxima = 5

    def acquire(self):
        # Se houver dicionários disponíveis no pool, reutiliza o último
        if self.pool:
            print(
                f"Reutilizando dict do pool. Disponíveis antes: {len(self.pool)}"
            )
            return self.pool.pop()

        # Se o pool estiver vazio, cria um dicionário novo do zero
        print("Pool vazio! Criando um novo dict...")
        return {}

    def release(self, obj):
        # SÓ guarda de volta se o pool não estiver lotado
        if len(self.pool) < self.capacidade_maxima:
            # Limpa o dicionário antes de guardar para garantir que ele volte "zerado"
            obj.clear()
            self.pool.append(obj)
            print(f"Dict devolvido com sucesso. Total no pool: {len(self.pool)}")
        else:
            # Se já tem 5, o pool ignora e o Python descarta o objeto da memória
            print("Pool lotado (capacidade 5)! Objeto descartado.")


# --- TESTANDO OS LIMITES DO SEU POOL ---
pool = ObjectPool()

# Vamos pegar 6 objetos (todos vão ser criados do zero porque o pool começa vazio)
dicts = [pool.acquire() for _ in range(6)]

print("\n--- Devolvendo os objetos ---")
# Vamos devolver todos os 6. O pool deve aceitar 5 e descartar o último!
for d in dicts:
    pool.release(d)

print("\n--- Pegando objetos novamente ---")
# Se pedirmos um objeto agora, ele vai reutilizar um dos 5 que estão no pool
outro_dict = pool.acquire()
