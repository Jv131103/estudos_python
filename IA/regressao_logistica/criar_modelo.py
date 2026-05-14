import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, accuracy_score, recall_score, precision_score, confusion_matrix


df = pd.read_csv("./IA/regressao_logistica/alunos.csv")

X = df[["horas_estudo", "faltas"]]
y = df["aprovado"]

print(X)
print()
print(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

modelo = LogisticRegression()

# Colocando padrões:
# EX:
# mais horas → chance sobe
# mais faltas → chance cai
modelo.fit(X_train, y_train)

# Prever classes
y_pred = modelo.predict(X_test)
print(y_pred)  # Exemplo: [1 0 1] <-> [aprovado, reporvado, aprovado]

# Prever probabilidade:
# Leitura EX:
# Linha: [0.12 0.88] -> 12% classe 0, 88% classe 1
# Ou seja: 88% chance de aprovação
# Ele decide usando regra padrão se probabilidade >= 0.5 então classe 1
y_proba = modelo.predict_proba(X_test)

# Métricas

# Acurácia
acc = accuracy_score(y_test, y_pred)
print(acc)  # Se:0.90, 90% acertos

# Precision
# quando o modelo disse SIM, acertou?
precision = precision_score(y_test, y_pred)
print(precision)

# Recall
# dos positivos reais, quantos achou?
rec = recall_score(y_test, y_pred)
print(rec)

# f1 - score
# precision + recall
f1score = f1_score(y_test, y_pred)
print(f1score)

# Matriz de confusão:
# Super importante.
# Como ler:
# TN FP
# FN TP
# Visual:
#                PREVISTO
#              NÃO    SIM
#
# REAL NÃO       8      2
# REAL SIM       1      9
# Significa:
# Acertou: 8 negativos | 9 positivos
# Errou: 2 falsos positivos | 1 falso negativo
cm = confusion_matrix(y_test, y_pred)
print(cm)
