class PizzaBuilder:
    def __init__(self) -> None:
        self.builder = {}
        self.ingredientes = []
        self.tam = "pequeno"
        self.mass = "fina"
        self.mol = "tomate"

    def tamanho(self, tamanho):
        if not tamanho:
            raise ValueError("É preciso escolher um tamanho")
        elif tamanho.strip().lower() not in ["grande", "medio", "pequeno"]:
            raise ValueError("Digite apenas: grande | medio | pequeno")

        self.tam = tamanho
        return self

    def massa(self, tipo):
        if not tipo:
            raise ValueError("É preciso escolher um tipo de massa")
        elif tipo.strip().lower() not in ["fina", "grossa", "especial"]:
            raise ValueError("Digite apenas: fina | grossa | especial")

        self.mass = tipo
        return self

    def molho(self, tipo):
        if not tipo:
            raise ValueError("É preciso escolher um tipo de molho")

        self.mol = tipo
        return self

    def adicionar_ingrediente(self, ingrediente):
        if not ingrediente:
            raise ValueError("É preciso escolher um ingrediente")

        self.ingredientes.append(ingrediente)
        return self

    def build(self):
        self.builder["tamanho"] = self.tam
        self.builder["massa"] = self.mass
        self.builder["molho"] = self.mol
        self.builder["ingredientes"] = self.ingredientes
        return self

    def __str__(self) -> str:
        return f"Pizza {self.builder['tamanho']} | massa {self.builder['massa']} | molho {self.builder['molho']} | ingredientes: {', '.join(self.builder['ingredientes'])}"


pizza = (
    PizzaBuilder()
    .tamanho("grande")
    .massa("fina")
    .molho("tomate")
    .adicionar_ingrediente("queijo")
    .adicionar_ingrediente("pepperoni")
    .build()
)

print(pizza)
