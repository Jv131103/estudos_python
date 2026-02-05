"""
Crie uma classe Usuario com:

    variável de classe total_usuarios

    incremente no __init__

    Crie 3 usuários e mostre o total.
"""


class Usuario:
    total = 0

    def __init__(self) -> None:
        Usuario.total += 1

    @classmethod
    def total_usuarios(cls):
        return cls.total


user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

print(Usuario.total_usuarios())
