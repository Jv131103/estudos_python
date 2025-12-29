def nao_eh_vazio(a):
    if a is None or not a:
        return False
    return True


testes = [
    ['ola', True],
    ['', False],
    [1, True],
    [0, False],
    [1.35, True],
    [0.0, False],
    [[], False],
    [[1, True, None, "OLA"], True]
]

for teste in testes:
    valor, resultado = teste
    assert nao_eh_vazio(valor) == resultado
