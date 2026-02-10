"""
Crie uma classe ValidadorSenha com método estático
que valide tamanho mínimo.
"""


class ValidadorSenha:
    @staticmethod
    def validar_tamanho_minimo(senha, tam=8):
        return len(senha) >= tam


print(ValidadorSenha.validar_tamanho_minimo("12345678"))
