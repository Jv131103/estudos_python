class Pool:
    def __init__(self, tamanho):
        self.recursos = [f"Recurso-{i}" for i in range(tamanho)]
        self.em_uso = []

    def adquirir(self):
        if self.recursos:
            recurso = self.recursos.pop()
            self.em_uso.append(recurso)
            print(f"Pegou: {recurso}")
            return recurso
        else:
            print("Sem recursos disponíveis!")

    def liberar(self, recurso):
        self.em_uso.remove(recurso)
        self.recursos.append(recurso)
        print(f"Devolveu: {recurso}")


pool = Pool(2)

r1 = pool.adquirir()
r2 = pool.adquirir()
r3 = pool.adquirir()  # não tem mais

pool.liberar(r1)
r4 = pool.adquirir()
