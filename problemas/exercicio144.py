import pandas as pd

anos = list(range(2010, 2020))
chaves = ['Receita produto A', 'Receita produto B']
valores = [
    [1001.19, 1500.55, 857.94, 110.33, 29.45, 33.55, 44.70, 430, 120, 177],
    [20, 33.5, 91.4, 4.5, 111, 230, 900, 801.2, 101.4, 202.6]
]

produtos = dict(
    zip(chaves, valores)
)
print(produtos)

frame = pd.DataFrame(produtos, index=anos)
print(frame)

receita_total = [(ano, a + b) for ano, a, b in zip(anos, valores[0], valores[1])]
print(receita_total)
