"""
Crie uma função maior(a, b) que retorne o maior valor entre dois números.
"""


def maior(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Parâmetros precisam ser do tipo numérico")
        return

    if a > b:
        return a
    return b


testes = (
    [2, 3, 3],
    [4, 2, 4],
    [-1, -2, -1],
    [-5, -3, -3],
    [True, False, 1],
    [False, True, 1],
    ['1', 2, None],
    [1, '2', None],
    ['1', '2', None],
)

for teste in testes:
    a, b, esperado = teste

    print(f"{teste}: {maior(a, b) == esperado}")
