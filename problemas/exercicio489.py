"""
Crie uma função soma(a, b) que receba dois números e retorne a soma.
"""


def soma(n1, n2):
    if (
        not isinstance(n1, (int, float, complex))
        or not isinstance(n2, (int, float, complex))
    ):
        print("Parâmetros precisam ser do tipo Numérico")
        return
    return n1 + n2


testes = [
    (2, 2, 4),
    (3, 2, 5),
    ('1', 2, None),
    (1, '2', None),
    ('1', '2', None),
    (-2, 3, 1),
    (2.2, 3.2, 5.4)
]

for valores in testes:
    n1, n2, esperado = valores
    print(f"{valores}: {soma(n1, n2) == esperado}")
