"""
Crie uma classe Usuario com:

    construtor normal
    método de classe criar_admin
"""


class Usuario:
    def __init__(self, username, is_admin=False) -> None:
        self.username = username
        self.is_admin = is_admin

    @classmethod
    def criar_admin(cls, username):
        return cls(username, is_admin=True)


user = Usuario("MathpH")
print(user.is_admin)  # False

user_adm = Usuario.criar_admin("adm1.0")
print(user_adm.is_admin)  # True
