"""
Crie uma função que aceite um tipo base
e passe objetos filhos sem mudar o código.
"""

import os


class ExecutarPowerShell:
    def executar_terminal(self, comando):
        return comando


class ExecutarBash:
    def executar_terminal(self, comando):
        return comando


def executar(comando, dado):
    return comando.executar_terminal(dado)


if os.name == "posix":
    print(executar(ExecutarBash(), "ls -la"))
else:
    print(executar(ExecutarPowerShell(), "dir"))
