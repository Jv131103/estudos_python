"""
Crie uma classe Livro com titulo, autor, paginas e um método descricao()
que retorne uma string tipo "Título — Autor (N páginas)".
"""


class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.titulo: str = titulo
        self.autor: str = autor
        self.paginas: int = paginas

    def descricao(self):
        saida = f"{self.titulo.title()} — {self.autor.title()} ({self.paginas} paginas)"
        return saida


if __name__ == "__main__":
    l1 = Livro("Teste", "Autor Teste", 0)
    print(l1.descricao())

    l2 = Livro("1984", "George Orwell", 416)
    print(l2.descricao())
