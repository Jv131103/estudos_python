def is_par(numero):
    return numero & 1 == 0


testes = [
    (2, True),
    (3, False),
    (9, False),
    (10, True),
    (12, True),
    (21, False)
]


for teste in testes:
    num, resp = teste
    assert is_par(num) == resp, f"Número {num} de resposta {resp} não bateu com a função"
