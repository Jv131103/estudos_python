import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)


# =========================
# 1. CARREGAR CSV
# =========================
df = pd.read_csv("./IA/svm/alunos.csv")


# =========================
# 2. DIAGNÓSTICO
# =========================
print("\nHEAD:")
print(df.head())

print("\nINFO:")
print(df.info())

print("\nAUSENTES:")
print(df.isna().sum())

print("\nDUPLICADOS:")
print(df.duplicated().sum())

print("\nDESCRIBE:")
print(df.describe())


# =========================
# 3. LIMPEZA
# =========================
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


# =========================
# 4. SEPARAR X E y
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
# 5. TREINO / TESTE
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)


# =========================
# 6. PADRONIZAÇÃO
# =========================
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# =========================
# 7. CRIAR MODELO SVM
# =========================
modelo = SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale",
    probability=True,
    random_state=42,
)


# =========================
# 8. TREINAR
# =========================
modelo.fit(X_train_scaled, y_train)


# =========================
# 9. PREVER
# =========================
y_pred = modelo.predict(X_test_scaled)
y_proba = modelo.predict_proba(X_test_scaled)[:, 1]


# =========================
# 10. RESULTADO
# =========================
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

print("\nREAL VS PREVISTO:")
print(resultado.head(20))


# =========================
# 11. MÉTRICAS
# =========================
print("\nMÉTRICAS:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
print("F1-score:", f1_score(y_test, y_pred, zero_division=0))

print("\nMATRIZ DE CONFUSÃO:")
print(confusion_matrix(y_test, y_pred))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred, zero_division=0))


# =========================
# 12. NOVA PREVISÃO
# =========================
novo_aluno = pd.DataFrame({
    "horas_estudo": [8],
    "faltas": [2],
    "sono_horas": [7],
    "participacao": [8],
    "media_atividades": [8.5],
})

novo_aluno_scaled = scaler.transform(novo_aluno)

classe = modelo.predict(novo_aluno_scaled)[0]
probabilidade = modelo.predict_proba(novo_aluno_scaled)[0][1]

print("\nNOVA PREVISÃO:")
print(novo_aluno)

if classe == 1:
    print(f"Resultado: APROVADO | Probabilidade: {probabilidade:.2%}")
else:
    print(f"Resultado: REPROVADO | Probabilidade de aprovação: {probabilidade:.2%}")
