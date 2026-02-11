"""
Crie um Enum NivelAcesso
e um sistema que use match para liberar ações.
"""

from enum import Enum


class NivelAcesso(Enum):
    ADMIN = 1
    USUARIO = 2
    VISITANTE = 3


def executar_acao(nivel: NivelAcesso):
    match nivel:
        case NivelAcesso.ADMIN:
            print("Acesso total liberado")
        case NivelAcesso.USUARIO:
            print("Acesso parcial liberado")
        case NivelAcesso.VISITANTE:
            print("Acesso restrito")


acesso_user = NivelAcesso.USUARIO
executar_acao(acesso_user)
