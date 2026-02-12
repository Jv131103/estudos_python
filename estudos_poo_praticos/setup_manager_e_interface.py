from abc import ABC, abstractmethod


# Interface
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, dado):
        pass


# Implementação
class RepoMemoria(Repositorio):
    def salvar(self, dado):
        print("Salvo:", dado)


# Manager
class UsuarioManager:
    def __init__(self, repo: Repositorio):
        self.repo = repo

    def criar(self, nome):
        usuario = {"nome": nome}
        self.repo.salvar(usuario)
        return usuario


# Setup
def setup():
    repo = RepoMemoria()
    return UsuarioManager(repo)


manager = setup()
manager.criar("Renato")
