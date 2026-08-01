import pandas as pd

dados = [
    {"nome": "Ana", "idade": 23, "salario": 3500},
    {"nome": "Bruno", "idade": 35, "salario": None},
    {"nome": "Carla", "idade": 29, "salario": 4200},
    {"nome": "Diego", "idade": None, "salario": 3900},
]

df = pd.DataFrame(dados)

print(f"3 Primeiras linhas:\n{df.head(3)}")
print()
print(f"Estatísticas descritivas (média, desvio padrão, min, max...):\n{df.describe()}")

print("Valores nulos por coluna:")
print(df.isnull().sum())

df_sem_nulos = df.dropna()
print("\nDataFrame sem linhas nulas:")
print(df_sem_nulos)
print()

salarios_superiores = df[df['salario'] > 3800]
print(f"Salarios SUPERIORES a 3800:\n{salarios_superiores}")
print()

produtos = [
    {"nome": "mouse", "valor": 68.9},
    {"nome": "teclado", "valor": 189.76},
    {"nome": "monitor", "valor": 2800.23},
    {"nome": "placa de vídeo", "valor": 3500.90},
    {"nome": "placa mãe", "valor": 1890.98},
    {"nome": "processador", "valor": 2000},
    {"nome": "mouse", "valor": 48.9},
    {"nome": "teclado", "valor": 500},
]

df_p = pd.DataFrame(produtos)
total_vendido_por_produto = df_p.groupby("nome")["valor"].sum()
print(total_vendido_por_produto)
