import pandas as pd

# Series: pode ser considerada como uma coluna em uma tabela, onde
# cada elemento é associado a um índice. São unidimencionais
# e possuem rótulos para cada elemento.

# Criando uma Series a partir de uma lista
s = pd.Series([1, 2, 3, 4, 5])

# Acesso à posição de índice 4
print(s[4])  # Saída: 5
