class Livro:
    def __init__(self, titulo, autor, copias_totais=1) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__copias_totais = copias_totais
        self.__copias_disponiveis = copias_totais

    def emprestar(self):
        if not self.__copias_disponiveis:
            raise ValueError("Não há cópias disponpiveis")

        print(f"Emprestando {self.__titulo}({self.__autor})...")
        self.__copias_disponiveis -= 1
        print(f"Restantes: {self.__copias_disponiveis}")

    def devolver(self):
        if self.__copias_disponiveis >= self.__copias_totais:
            raise ValueError("Livro inexistente para devolução")

        self.__copias_disponiveis += 1
        print(f"Devolvendo {self.__titulo}({self.__autor})...")
        print(f"Restantes: {self.__copias_disponiveis}")

    def esta_disponivel(self):
        if self.__copias_disponiveis >= 1:
            return True
        return False

    @property
    def titulo(self):
        return self.__titulo

    @property
    def copias_disponiveis(self):
        return self.__copias_disponiveis


if __name__ == "__main__":
    livro = Livro("Dom Casmurro", "Machado de Assis", copias_totais=2)
    livro.emprestar()
    livro.emprestar()
    print(livro.esta_disponivel())
    try:
        livro.emprestar()
    except ValueError as ve:
        print(ve)
    livro.devolver()
    print(livro.esta_disponivel())
