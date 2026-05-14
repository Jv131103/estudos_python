from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
import pandas as pd


df = pd.read_csv("./IA/arvores_decisao/alunos.csv")

X = df[["horas_estudo", "faltas", "sono_horas"]]
y = df["aprovado"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Treinando modelo:
modelo = DecisionTreeClassifier(
    max_depth=3,   # Limita profundidade da árvore
    random_state=42  # Fixa aleatoriedade
)

# Treinar:
modelo.fit(X_train, y_train)

# Aprendizado:
# Diferente da regressão linear, árvore não tem coef_ nem intercept_
# Ela aprende REGRAS / PERGUNTAS
print(modelo.get_depth())        # profundidade real aprendida
print(modelo.get_n_leaves())     # quantidade de folhas (decisões finais)


# PREVER:
# EX:
# [[8, 2, 7]]
# horas=8, faltas=2, sono=7
# saída esperada:
# [1] -> aprovado
y_pred = modelo.predict(X_test)

print(y_pred)


# PREVER PROBABILIDADES:
# mostra chance de cada classe
# EX:
# [0.15, 0.85]
# 15% reprovado
# 85% aprovado
y_proba = modelo.predict_proba(X_test)

print(y_proba)


# VISÃO
# N: Dados do aluno
# M: Valor verdadeiro
# O: Modelo previu isso
# P: Acertou ou não
#
# Significado:
# Para aquele aluno com N características,
# o valor verdadeiro é M,
# o modelo previu O,
# então verificamos se acertou
resultado = pd.DataFrame({
    "horas_estudo": X_test["horas_estudo"],
    "faltas": X_test["faltas"],
    "sono_horas": X_test["sono_horas"],
    "real": y_test,
    "previsto": y_pred,
})

# acertou?
resultado["acertou"] = resultado["real"] == resultado["previsto"]

print(resultado)


# MÉTRICA 1:
# Accuracy
# percentual total de acertos
accuracy = accuracy_score(y_test, y_pred)

print(accuracy)
# EX:
# 0.91 = 91% de acerto


# MÉTRICA 2:
# Precision
# quando modelo disse APROVADO, quantas vezes acertou?
precision = precision_score(y_test, y_pred)

print(precision)


# MÉTRICA 3:
# Recall
# dos aprovados reais, quantos encontrou?
recall = recall_score(y_test, y_pred)

print(recall)


# MÉTRICA 4:
# F1-score
# equilíbrio entre precision e recall
f1 = f1_score(y_test, y_pred)

print(f1)


# MATRIZ DE CONFUSÃO
cm = confusion_matrix(y_test, y_pred)

print(cm)
