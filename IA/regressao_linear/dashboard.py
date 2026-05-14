import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


st.set_page_config(
    page_title="Dashboard Regressão Linear",
    layout="wide"
)

st.title("Dashboard de Machine Learning — Regressão Linear")
st.write("Modelo para prever nota com base nas horas de estudo.")


# =========================
# 1. CARREGAR CSV
# =========================
try:
    df = pd.read_csv("./IA/regressao_linear/notas.csv")
except FileNotFoundError:
    df = pd.read_csv("notas.csv")


st.header("1. Dados do CSV")
st.dataframe(df.head(20))

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de linhas", df.shape[0])

with col2:
    st.metric("Total de colunas", df.shape[1])

with col3:
    st.metric("Média das notas", round(df["nota"].mean(), 2))

# =========================
# 1.1 DIAGNÓSTICO DOS DADOS
# =========================
st.header("1.1 Diagnóstico dos Dados")

st.write("Valores ausentes por coluna:")
st.dataframe(df.isna().sum())

st.write("Tipos das colunas:")
st.dataframe(df.dtypes.astype(str).reset_index().rename(
    columns={"index": "coluna", 0: "tipo"}
))

st.write("Linhas duplicadas:", df.duplicated().sum())

st.write("Estatísticas gerais:")
st.dataframe(df.describe())


# =========================
# 1.2 LIMPEZA DOS DADOS
# =========================
st.header("1.2 Limpeza dos Dados")

df_original = df.copy()

# remover duplicadas
df = df.drop_duplicates()

# converter para número
df["horas_estudo"] = pd.to_numeric(df["horas_estudo"], errors="coerce")
df["nota"] = pd.to_numeric(df["nota"], errors="coerce")

# remover valores ausentes
df = df.dropna(subset=["horas_estudo", "nota"])

# regras de negócio
df = df[df["horas_estudo"] >= 0]
df = df[(df["nota"] >= 0) & (df["nota"] <= 10)]

st.success("Limpeza concluída.")

col_l1, col_l2, col_l3 = st.columns(3)

with col_l1:
    st.metric("Linhas antes", df_original.shape[0])

with col_l2:
    st.metric("Linhas depois", df.shape[0])

with col_l3:
    st.metric("Linhas removidas", df_original.shape[0] - df.shape[0])

st.write("Dados após limpeza:")
st.dataframe(df.head(20))

if df.shape[0] < 10:
    st.error("Poucos dados após a limpeza. Gere mais dados antes de treinar.")
    st.stop()

# =========================
# 2. SEPARAR X E y
# =========================
X = df[["horas_estudo"]]
y = df["nota"]

test_size = st.sidebar.slider(
    "Tamanho do teste",
    min_value=0.1,
    max_value=0.5,
    value=0.2,
    step=0.05
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=test_size,
    random_state=42
)


# =========================
# 3. TREINAR MODELO
# =========================
modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)


# =========================
# 4. RESULTADOS
# =========================
resultado = pd.DataFrame({
    "horas_estudo": X_test["horas_estudo"],
    "real": y_test,
    "previsto": y_pred
})

resultado["erro"] = resultado["real"] - resultado["previsto"]
resultado["erro_abs"] = abs(resultado["erro"])


# =========================
# 5. MÉTRICAS
# =========================
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

st.header("2. Métricas do Modelo")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("MAE", round(mae, 3))

with m2:
    st.metric("MSE", round(mse, 3))

with m3:
    st.metric("RMSE", round(rmse, 3))

with m4:
    st.metric("R²", round(r2, 3))


st.write("Coeficiente aprendido:", modelo.coef_[0])
st.write("Intercepto aprendido:", modelo.intercept_)


# =========================
# 6. TABELA REAL VS PREVISTO
# =========================
st.header("3. Real vs Previsto")
st.dataframe(resultado)


# =========================
# 7. GRÁFICO: DADOS + RETA
# =========================
st.header("4. Gráfico da Regressão Linear")

fig, ax = plt.subplots()

ax.scatter(df["horas_estudo"], df["nota"], label="Dados reais")
ax.plot(
    df["horas_estudo"].sort_values(),
    modelo.predict(pd.DataFrame({
        "horas_estudo": df["horas_estudo"].sort_values()
    })),
    label="Reta do modelo"
)

ax.set_xlabel("Horas de estudo")
ax.set_ylabel("Nota")
ax.set_title("Horas de estudo vs Nota")
ax.legend()

st.pyplot(fig)


# =========================
# 8. GRÁFICO DE ERROS
# =========================
st.header("5. Erros do Modelo")

fig2, ax2 = plt.subplots()

ax2.scatter(resultado["previsto"], resultado["erro"])
ax2.axhline(0, linestyle="--")

ax2.set_xlabel("Valor previsto")
ax2.set_ylabel("Erro")
ax2.set_title("Erro = Real - Previsto")

st.pyplot(fig2)


# =========================
# 9. PREVISÃO INTERATIVA
# =========================
st.header("6. Fazer uma nova previsão")

horas_novas = st.number_input(
    "Digite quantas horas o aluno estudou:",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

nova_entrada = pd.DataFrame({
    "horas_estudo": [horas_novas]
})

previsao = modelo.predict(nova_entrada)[0]

st.success(f"Previsão de nota para {horas_novas} horas de estudo: {previsao:.2f}")

# rode com: streamlit run dashboard.py
