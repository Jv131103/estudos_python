"""
Usuario com senha encapsulada e checagem sem “vazar” senha

    Objetivo: encapsular credenciais e expor só o necessário.

    Requisitos

        Classe Usuario

        Atributos:

        nome (público)

        _senha (privado)

        Proibir acessar a senha diretamente:

        property senha deve lançar erro (ex: AttributeError("Acesso negado"))

    Métodos:

        definir_senha(nova) com regra: mínimo 8 chars, precisa ter 1 número

        autenticar(tentativa) retorna True/False

"""


class Usuario:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._senha = None

    @property
    def senha(self):
        raise AttributeError("Acesso Negado!")

    def definir_senha(self, nova):
        if len(nova) <= 8:
            raise ValueError("A senha precisa conter no mínimo 8 caracteres")

        for item in nova:
            if item.isdigit():
                break
        else:
            raise ValueError("A senha precisa conter pelo menos 1 número")

        self._senha = nova

    def autenticar(self, tentativa):
        return tentativa == self._senha


if __name__ == "__main__":

    user = Usuario("JVJs")

    user.definir_senha("Acesso123@")

    print(user.autenticar("errada"))
    print(user.autenticar("Acesso123@"))
