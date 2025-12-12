class Livro:
    def __init__(self, titulo, autor, ano) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True


class Biblioteca:
    def __init__(self) -> None:
        self.acervo = []

    def eh_livro(self, livro):
        return isinstance(livro, Livro)

    def adicionar_livro(self, livro):
        if not self.eh_livro(livro):
            print("Não guardado, por que não é um livro!")
            return

        if self.buscar_por_titulo(livro.titulo):
            print("Já existe um livro com esse título no acervo.")
            return

        self.acervo.append(livro)

    def buscar_por_titulo(self, titulo):
        t = titulo.strip().lower()
        for livro in self.acervo:
            if livro.titulo.strip().lower() == t:
                return livro
        print(f"Título {titulo} não encontrado em nosso acervo!")
        return None

    def emprestar(self, titulo):
        livro = self.buscar_por_titulo(titulo)
        if not livro:
            return

        if not livro.disponivel:
            print(f"Título {titulo} não emprestado por estar em uso!")
            return

        print(f"Título {titulo} emprestado!")
        livro.disponivel = False

    def devolver(self, titulo):
        livro = self.buscar_por_titulo(titulo)
        if not livro:
            return

        if livro.disponivel:
            print(f"Título {titulo} não foi emprestado!")
            return
        print(f"Título {titulo} devolvido!")
        livro.disponivel = True

    def listar_disponiveis(self):
        encontrados = [livro for livro in self.acervo if livro.disponivel]
        if not encontrados:
            print("Nenhum item disponível no acervo")
            return

        for livro in encontrados:
            print(f"Título: {livro.titulo}\nAutor: {livro.autor}\nAno: {livro.ano}\n")


b = Biblioteca()
b.adicionar_livro(Livro("Dom Casmurro", "Machado", 1899))
b.adicionar_livro(Livro("Meditações", "Marco Aurério", 180))
b.adicionar_livro(Livro("Sumas Teológicas 1 a 5", "Tomás de Aquino", 1269))
b.emprestar("Dom Casmurro")
b.emprestar("Dom Casmurro")
b.devolver("Dom Casmurro")
b.devolver("Dom Casmurro")
print()
b.listar_disponiveis()
