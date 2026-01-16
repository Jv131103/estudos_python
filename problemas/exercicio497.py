"""
Crie uma função gerar_multiplicador(n) que retorne uma função lambda capaz de
multiplicar qualquer número por n.
"""


def gerar_multiplicador(n):
    return lambda x: n * x


print(gerar_multiplicador(2)(2))
print(gerar_multiplicador(2)(4))

print()

dobro = gerar_multiplicador(2)
print(dobro(2))
print(dobro(4))
