class Configuracoes:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:           # primeira vez?
            cls._instancia = super().__new__(cls)  # cria a instância
        return cls._instancia                # sempre retorna a mesma

    def __init__(self) -> None:
        # só inicializa se ainda não tiver atributos
        if not hasattr(self, "tema"):
            self.tema = "claro"


c1 = Configuracoes()
c2 = Configuracoes()
c1.tema = "escuro"
print(c2.tema)   # "escuro" — são o mesmo objeto!
print(c1 is c2)  # True
