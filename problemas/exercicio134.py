temperatura_capitais_brasil = [
    ('Boa Vista', 32.4),
    ('Brasília', 26.6),
    ('Campo Grande', 28.8),
    ('Cuiabá', 38.6),
    ('Salvador', 37.1),
    ('São Paulo', 38.8),
    ('Rio de Janeiro', 34.7)
]

temperatura_em_k = list(map(lambda c: (c[0], round(c[1] + 273.15, 1)), temperatura_capitais_brasil))
print(temperatura_em_k)

temperatura_em_fh = list(map(lambda c: (c[0], round(c[1] * 9 / 5 + 32, 1)), temperatura_capitais_brasil))
print(temperatura_em_fh)
