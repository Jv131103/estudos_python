import pandas as pd

# Análise estatística descritiva
import numpy as np

# Simulação de dados de vendas
data = {
    'Dia': range(1, 31),
    'Vendas': np.random.randint(100, 200, size=30)
}

df_vendas = pd.DataFrame(data)

# Estatísticas descritivas
print(df_vendas.describe())
print()

# Utilize os métodos head e tail antes de iniciar a análise para se
# familiarizar com os dados que estão sendo manipulados no contexto
# da aplicação.
# Os métodos head e tail permitem verificar as extremidades do conjunto
# de dados, exibindo os primeiros e os últimos registros, respectivamente,
# visando facilitar a identificação dos valores e formatos presentes na
# amostra analisada. Por padrão, esses métodos retornam apenas cinco
# registros, porém, esse montante pode ser alterado informando o
# parâmetro n com a quantidade desejada.

# head: PADRÃO 5 PRIMEIROS
print("Primeiros:", df_vendas.head())
print("Primeiros 3:", df_vendas.head(3))
print()

# tail: PADRÃO 5 ÚLTIMOS
print("Ultimos:", df_vendas.head())
print("Ultimos 3:", df_vendas.head(3))
