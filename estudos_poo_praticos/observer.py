class EventManager:
    def __init__(self):
        self.eventos = {}

    def registrar(self, nome, funcao):
        if nome not in self.eventos:
            self.eventos[nome] = []

        self.eventos[nome].append(funcao)

    def disparar(self, nome, *args):
        if nome in self.eventos:
            for funcao in self.eventos[nome]:
                funcao(*args)


em = EventManager()
em.registrar("login", lambda u: print(f"Bem-vindo, {u}!"))
em.registrar("login", lambda u: print(f"Log: usuário {u} entrou"))
em.disparar("login", "Ana")
