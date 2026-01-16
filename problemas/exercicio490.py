"""
Crie uma função eh_par(n) que retorne True se o número for par e False caso
contrário.
"""


def eh_par(numero):
    if not isinstance(numero, (int)):
        print("Parametro numero precisa ser do tipo Inteiro")
        return False

    return numero % 2 == 0


testes = [
    (1, False),
    (2, True),
    (-1, False),
    (-2, True),
    (1.1, False),
    (2.0, False),
    ('1', False),
    (None, False),
    (True, False),
    (False, True),
    (1 + 1, True),
    (2 + 1, False),
    ([1, 2, 3], False),
    (sum([1, 2, 3]), True),
    ((1, 2, 3), False),
]

for dados in testes:
    valor_teste, resultado_esperado = dados
    print(f"{dados}: {eh_par(valor_teste) == resultado_esperado}")
