def media(*numeros):
    return round(sum(numeros) / len(numeros), 2)


testes = [
    ((2, 2, 2), 2),
    ((5, 5, 5, 5), 5),
    ((10, 10), 10),
    ((4, 6, 8), 6),
    ((5.4, 3.9, 10), 6.43),
]

for teste in testes:
    tupla, resposta = teste
    assert media(*tupla) == resposta
