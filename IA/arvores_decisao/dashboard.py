import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
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
    page_title="Dashboard Árvore de Decisão",
    layout="wide"
)

st.title("Dashboard de Machine Learning — Árvore de Decisão")
st.write("Modelo para prever se o aluno será aprovado ou reprovado.")


# =========================
# 1. CARREGAR CSV
# =========================
try:
    df = pd.read_csv("./IA/arvores_decisao/alunos.csv")
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
df["sono_horas"] = pd.to_numeric(df["sono_horas"], errors="coerce")
df["aprovado"] = pd.to_numeric(df["aprovado"], errors="coerce")

df = df.dropna(subset=["horas_estudo", "faltas", "sono_horas", "aprovado"])

df = df[df["horas_estudo"] >= 0]
df = df[df["faltas"] >= 0]
df = df[df["sono_horas"] >= 0]
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
X = df[["horas_estudo", "faltas", "sono_horas"]]
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

max_depth = st.sidebar.slider(
    "Profundidade máxima da árvore",
    min_value=1,
    max_value=10,
    value=3,
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
# 4. TREINAR MODELO
# =========================
modelo = DecisionTreeClassifier(
    max_depth=max_depth,
    random_state=42
)

modelo.fit(X_train, y_train)


# =========================
# 5. PREVISÕES
# =========================
y_pred = modelo.predict(X_test)
y_proba = modelo.predict_proba(X_test)[:, 1]


resultado = pd.DataFrame({
    "horas_estudo": X_test["horas_estudo"],
    "faltas": X_test["faltas"],
    "sono_horas": X_test["sono_horas"],
    "real": y_test,
    "previsto": y_pred,
    "prob_aprovado": y_proba
})

resultado["acertou"] = resultado["real"] == resultado["previsto"]


# =========================
# 6. MÉTRICAS
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


st.write("Profundidade real da árvore:", modelo.get_depth())
st.write("Quantidade de folhas:", modelo.get_n_leaves())


# =========================
# 7. TABELA REAL VS PREVISTO
# =========================
st.header("3. Real vs Previsto")
st.dataframe(resultado)


# =========================
# 8. MATRIZ DE CONFUSÃO
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
# 9. CLASSIFICATION REPORT
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
# 10. DESENHAR ÁRVORE
# =========================
st.header("6. Visualização da Árvore")

fig_tree, ax_tree = plt.subplots(figsize=(18, 8))

plot_tree(
    modelo,
    feature_names=X.columns,
    class_names=["Reprovado", "Aprovado"],
    filled=True,
    rounded=True,
    fontsize=9,
    ax=ax_tree
)

st.pyplot(fig_tree)


# =========================
# 11. IMPORTÂNCIA DAS FEATURES
# =========================
st.header("7. Importância das Features")

importancia = pd.DataFrame({
    "feature": X.columns,
    "importancia": modelo.feature_importances_
}).sort_values("importancia", ascending=False)

st.dataframe(importancia)

fig_imp, ax_imp = plt.subplots()
ax_imp.bar(importancia["feature"], importancia["importancia"])
ax_imp.set_title("Importância das Features")
ax_imp.set_ylabel("Importância")

st.pyplot(fig_imp)


# =========================
# 12. PREVISÃO INTERATIVA
# =========================
st.header("8. Fazer uma nova previsão")

horas_novas = st.number_input(
    "Horas de estudo:",
    min_value=0.0,
    max_value=24.0,
    value=6.0,
    step=0.5
)

faltas_novas = st.number_input(
    "Quantidade de faltas:",
    min_value=0,
    max_value=100,
    value=5,
    step=1
)

sono_novo = st.number_input(
    "Horas de sono:",
    min_value=0.0,
    max_value=24.0,
    value=7.0,
    step=0.5
)

nova_entrada = pd.DataFrame({
    "horas_estudo": [horas_novas],
    "faltas": [faltas_novas],
    "sono_horas": [sono_novo]
})

classe = modelo.predict(nova_entrada)[0]
probabilidade = modelo.predict_proba(nova_entrada)[0][1]

if classe == 1:
    st.success(f"Previsão: APROVADO — probabilidade: {probabilidade:.2%}")
else:
    st.error(f"Previsão: REPROVADO — probabilidade de aprovação: {probabilidade:.2%}")


# rode com:
# streamlit run dashboard.py
