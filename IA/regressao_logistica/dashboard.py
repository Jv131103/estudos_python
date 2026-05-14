import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)


st.set_page_config(
    page_title="Dashboard Regressão Logística",
    layout="wide"
)

st.title("Dashboard de Machine Learning — Regressão Logística")
st.write("Modelo para prever se o aluno será aprovado ou reprovado.")


# =========================
# 1. CARREGAR CSV
# =========================
try:
    df = pd.read_csv("./IA/regressao_logistica/alunos.csv")
except FileNotFoundError:
    df = pd.read_csv("alunos.csv")


st.header("1. Dados do CSV")
st.dataframe(df.head(20))


# =========================
# 1.1 DIAGNÓSTICO
# =========================
st.header("1.1 Diagnóstico dos Dados")

st.write("Valores ausentes:")
st.dataframe(df.isna().sum())

st.write("Tipos das colunas:")
st.dataframe(
    df.dtypes.astype(str)
    .reset_index()
    .rename(columns={"index": "coluna", 0: "tipo"})
)

st.write("Linhas duplicadas:", df.duplicated().sum())

st.write("Estatísticas gerais:")
st.dataframe(df.describe())


# =========================
# 1.2 LIMPEZA
# =========================
st.header("1.2 Limpeza dos Dados")

df_original = df.copy()

df = df.drop_duplicates()

df["horas_estudo"] = pd.to_numeric(df["horas_estudo"], errors="coerce")
df["faltas"] = pd.to_numeric(df["faltas"], errors="coerce")
df["aprovado"] = pd.to_numeric(df["aprovado"], errors="coerce")

df = df.dropna(subset=["horas_estudo", "faltas", "aprovado"])

df = df[df["horas_estudo"] >= 0]
df = df[df["faltas"] >= 0]
df = df[df["aprovado"].isin([0, 1])]

st.success("Limpeza concluída.")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Linhas antes", df_original.shape[0])

with c2:
    st.metric("Linhas depois", df.shape[0])

with c3:
    st.metric("Linhas removidas", df_original.shape[0] - df.shape[0])

st.write("Dados após limpeza:")
st.dataframe(df.head(20))

if df.shape[0] < 10:
    st.error("Poucos dados após limpeza.")
    st.stop()


# =========================
# 2. SEPARAR X E y
# =========================
X = df[["horas_estudo", "faltas"]]
y = df["aprovado"]

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
    random_state=42,
    stratify=y
)


# =========================
# 3. TREINAR MODELO
# =========================
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
y_proba = modelo.predict_proba(X_test)[:, 1]


# =========================
# 4. RESULTADOS
# =========================
resultado = pd.DataFrame({
    "horas_estudo": X_test["horas_estudo"],
    "faltas": X_test["faltas"],
    "real": y_test,
    "previsto": y_pred,
    "prob_aprovado": y_proba
})

resultado["acertou"] = resultado["real"] == resultado["previsto"]


# =========================
# 5. MÉTRICAS
# =========================
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

st.header("2. Métricas do Modelo")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Accuracy", round(accuracy, 3))

with m2:
    st.metric("Precision", round(precision, 3))

with m3:
    st.metric("Recall", round(recall, 3))

with m4:
    st.metric("F1-score", round(f1, 3))


st.write("Coeficientes aprendidos:")
st.write(pd.DataFrame({
    "feature": X.columns,
    "coeficiente": modelo.coef_[0]
}))

st.write("Intercepto:", modelo.intercept_[0])


# =========================
# 6. TABELA REAL VS PREVISTO
# =========================
st.header("3. Real vs Previsto")
st.dataframe(resultado)


# =========================
# 7. MATRIZ DE CONFUSÃO
# =========================
st.header("4. Matriz de Confusão")

cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots()
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Reprovado", "Aprovado"]
)
disp.plot(ax=ax)
st.pyplot(fig)


# =========================
# 8. RELATÓRIO DE CLASSIFICAÇÃO
# =========================
st.header("5. Classification Report")

report = classification_report(
    y_test,
    y_pred,
    target_names=["Reprovado", "Aprovado"],
    output_dict=True,
    zero_division=0
)

st.dataframe(pd.DataFrame(report).transpose())


# =========================
# 9. GRÁFICO: HORAS X FALTAS
# =========================
st.header("6. Distribuição dos Alunos")

fig2, ax2 = plt.subplots()

ax2.scatter(
    df["horas_estudo"],
    df["faltas"],
    c=df["aprovado"]
)

ax2.set_xlabel("Horas de estudo")
ax2.set_ylabel("Faltas")
ax2.set_title("Horas de estudo x Faltas")

st.pyplot(fig2)


# =========================
# 10. PREVISÃO INTERATIVA
# =========================
st.header("7. Fazer uma nova previsão")

horas_novas = st.number_input(
    "Horas de estudo:",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

faltas_novas = st.number_input(
    "Quantidade de faltas:",
    min_value=0,
    max_value=100,
    value=5,
    step=1
)

nova_entrada = pd.DataFrame({
    "horas_estudo": [horas_novas],
    "faltas": [faltas_novas]
})

classe = modelo.predict(nova_entrada)[0]
probabilidade = modelo.predict_proba(nova_entrada)[0][1]

if classe == 1:
    st.success(f"Previsão: APROVADO — probabilidade: {probabilidade:.2%}")
else:
    st.error(f"Previsão: REPROVADO — probabilidade de aprovação: {probabilidade:.2%}")


# rode com:
# streamlit run dashboard.py
