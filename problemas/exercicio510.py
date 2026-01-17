"""
Considere as seguintes flags:

    LER       = 1 << 0   # 001
    ESCREVER  = 1 << 1   # 010
    EXECUTAR  = 1 << 2   # 100

Faça um programa que:

    1. Crie uma variável permissao com:

        . LER e ESCREVER ativados

    2. Verifique usando &:

        . se pode ler

        . se pode executar

    3. Imprima mensagens claras, por exemplo:

        . "Pode ler"

        . "Não pode executar"
"""

LER = 1 << 0   # 001
ESCREVER = 1 << 1   # 010
EXECUTAR = 1 << 2   # 100

permissao = LER | ESCREVER  # 001 | 010 = 011

if permissao & LER:
    print("Pode ler")
else:
    print("Não pode ler")

if permissao & EXECUTAR:
    print("Pode executar")
else:
    print("Não pode executar")
