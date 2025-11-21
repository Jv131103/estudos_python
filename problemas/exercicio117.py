empresas = ['ABEV3', 'AZUL4', 'BTOW3', 'RENT3', 'JBSS3']
precos = [12.85, 22.55, 115.08, 49.03, 24.41]

dicionario = {empresa: preco for empresa, preco in zip(empresas, precos)}
print(dicionario)
