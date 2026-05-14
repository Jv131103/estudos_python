import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
)


st.set_page_config(
    page_title="Dashboard KNN",
    layout="wide"
)

st.title("Dashboard de Machine Learning — KNN")
st.write("Modelo para prever se o aluno será aprovado ou reprovado.")


# =========================
# 1. CARREGAR CSV
# =========================
try:
    df = pd.read_csv("./IA/knn/alunos.csv")
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

colunas_numericas = [
    "horas_estudo",
    "faltas",
    "sono_horas",
    "participacao",
    "media_atividades",
    "aprovado",
]

for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(df[coluna], errors="coerce")

df = df.dropna(subset=colunas_numericas)

df = df[df["horas_estudo"] >= 0]
df = df[df["faltas"] >= 0]
df = df[df["sono_horas"] >= 0]
df = df[(df["participacao"] >= 0) & (df["participacao"] <= 10)]
df = df[(df["media_atividades"] >= 0) & (df["media_atividades"] <= 10)]
df = df[df["aprovado"].isin([0, 1])]

st.success("Limpeza concluída.")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Linhas antes", df_original.shape[0])

with c2:
    st.metric("Linhas depois", df.shape[0])

with c3:
    st.metric("Linhas removidas", df_original.shape[0] - df.shape[0])

st.dataframe(df.head(20))

if df.shape[0] < 10:
    st.error("Poucos dados após limpeza.")
    st.stop()


# =========================
# 2. SEPARAR X E y
# =========================
X = df[
    [
        "horas_estudo",
        "faltas",
        "sono_horas",
        "participacao",
        "media_atividades",
    ]
]

y = df["aprovado"]


# =========================
# SIDEBAR
# =========================
test_size = st.sidebar.slider(
    "Tamanho do teste",
    min_value=0.1,
    max_value=0.5,
    value=0.2,
    step=0.05
)

n_neighbors = st.sidebar.slider(
    "Número de vizinhos (K)",
    min_value=1,
    max_value=50,
    value=5,
    step=1
)


# =========================
# 3. TREINO / TESTE
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=test_size,
    random_state=42,
    stratify=y
)


# =========================
# 4. PADRONIZAÇÃO
# =========================
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# =========================
# 5. TREINAR MODELO
# =========================
modelo = KNeighborsClassifier(
    n_neighbors=n_neighbors
)

modelo.fit(X_train_scaled, y_train)


# =========================
# 6. PREVISÕES
# =========================
y_pred = modelo.predict(X_test_scaled)
y_proba = modelo.predict_proba(X_test_scaled)[:, 1]


resultado = pd.DataFrame({
    "horas_estudo": X_test["horas_estudo"],
    "faltas": X_test["faltas"],
    "sono_horas": X_test["sono_horas"],
    "participacao": X_test["participacao"],
    "media_atividades": X_test["media_atividades"],
    "real": y_test,
    "previsto": y_pred,
    "prob_aprovado": y_proba,
})

resultado["acertou"] = resultado["real"] == resultado["previsto"]


# =========================
# 7. MÉTRICAS
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


st.write("K usado:", n_neighbors)


# =========================
# 8. TABELA REAL VS PREVISTO
# =========================
st.header("3. Real vs Previsto")
st.dataframe(resultado)


# =========================
# 9. MATRIZ DE CONFUSÃO
# =========================
st.header("4. Matriz de Confusão")

cm = confusion_matrix(y_test, y_pred)

fig_cm, ax_cm = plt.subplots()
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Reprovado", "Aprovado"]
)
disp.plot(ax=ax_cm)
st.pyplot(fig_cm)


# =========================
# 10. CLASSIFICATION REPORT
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
# 11. PREVISÃO INTERATIVA
# =========================
st.header("6. Fazer uma nova previsão")

horas_novas = st.number_input("Horas de estudo:", 0.0, 24.0, 8.0, 0.5)
faltas_novas = st.number_input("Quantidade de faltas:", 0, 100, 2, 1)
sono_novo = st.number_input("Horas de sono:", 0.0, 24.0, 7.0, 0.5)
participacao_nova = st.number_input("Participação:", 0.0, 10.0, 8.0, 0.5)
media_atividades_nova = st.number_input("Média das atividades:", 0.0, 10.0, 8.5, 0.5)

nova_entrada = pd.DataFrame({
    "horas_estudo": [horas_novas],
    "faltas": [faltas_novas],
    "sono_horas": [sono_novo],
    "participacao": [participacao_nova],
    "media_atividades": [media_atividades_nova],
})

nova_entrada_scaled = scaler.transform(nova_entrada)

classe = modelo.predict(nova_entrada_scaled)[0]
probabilidade = modelo.predict_proba(nova_entrada_scaled)[0][1]

if classe == 1:
    st.success(f"Previsão: APROVADO — probabilidade: {probabilidade:.2%}")
else:
    st.error(f"Previsão: REPROVADO — probabilidade de aprovação: {probabilidade:.2%}")


# rode com:
# streamlit run dashboard.py
