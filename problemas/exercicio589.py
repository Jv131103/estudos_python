"""
Faça um programa que:

    Crie uma exceção base AppError

    Crie duas exceções que herdam dela

    Lance cada uma em situações diferentes

Capture:

    uma exceção específica

    depois a base
"""


class BaseError(Exception):
    pass


class SenhaInvalida(BaseError):
    pass


class AcessoNegado(BaseError):
    pass


usuario = {
    "nome": "JV",
    "senha": "12345",
    "permissao_de_acesso": 1
}


def validar_usuario(senha):
    if senha != usuario["senha"]:
        raise SenhaInvalida("SENHA DE USUÁRIO NÃO CORRESPONDE COM PADRÃO")

    if not usuario["permissao_de_acesso"]:
        raise AcessoNegado(f"Acesso negado para usuário {usuario['nome']}")

    return True


try:
    validar_usuario("senha_errada")
except SenhaInvalida as e:
    print(f"Erro específico de senha: {e}")
except BaseError as e:
    print(f"Erro genérico da aplicação: {e}")
else:
    print("Usuário validado com sucesso")
