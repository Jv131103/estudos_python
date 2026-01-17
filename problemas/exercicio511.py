"""
Usando as mesmas flags:

    LER       = 1 << 0
    ESCREVER  = 1 << 1
    EXECUTAR  = 1 << 2

Faça um programa que:

    1. Leia duas permissões diferentes (ex: p1 e p2)

        . cada uma é uma combinação de flags

    2. Calcule:

        . p_and → permissões em comum (&)

        . p_or → permissões combinadas (|)

        . p_xor → permissões exclusivas (^)

    3. Para cada resultado, mostre quais permissões estão ativas (ler, escrever,
    executar)

Dica mental:

    & → o que ambos têm

    | → tudo que existe

    ^ → só o que é diferente
"""
LER = 1 << 0  # 001
ESCREVER = 1 << 1  # 010
EXECUTAR = 1 << 2  # 100


def mostrar_permissoes(p):
    permissoes = []

    if p & LER:
        permissoes.append("LER")
    if p & ESCREVER:
        permissoes.append("ESCREVER")
    if p & EXECUTAR:
        permissoes.append("EXECUTAR")

    if permissoes:
        return ", ".join(permissoes)
    return "Nenhuma"


p1 = int(input("Digite p1: "))
p2 = int(input("Digite p2: "))

p_and = p1 & p2
p_or = p1 | p2
p_xor = p1 ^ p2

print(f"\np1 & p2 = {p_and} → {mostrar_permissoes(p_and)}")
print(f"p1 | p2 = {p_or} → {mostrar_permissoes(p_or)}")
print(f"p1 ^ p2 = {p_xor} → {mostrar_permissoes(p_xor)}")
