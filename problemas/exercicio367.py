def is_positive(x):
    return x > 0


dados = [
    [10, True],
    [1, True],
    [13, True],
    [0, False],
    [-10, False],
    [-1, False],
    [-13, False]
]

for dado in dados:
    valor, saida = dado
    assert is_positive(valor) == saida
