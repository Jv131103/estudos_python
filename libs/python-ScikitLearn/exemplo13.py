from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
import pandas as pd
# Importando todas as métricas necessárias
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier


# Carregando novamente o dataset Wine
wine = load_wine()
X = wine.data  # Características
y = wine.target  # Rótulos

# Convertendo para DataFrame para melhor visualização
df = pd.DataFrame(X, columns=wine.feature_names)
df['target'] = y

# Dividindo o conjunto de dados em 70% treino e 30% teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# KNN
model_knn = KNeighborsClassifier()
model_knn.fit(X_train, y_train)
y_pred = model_knn.predict(X_test)

# Calculando e exibindo a Acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.2f}")

# Calculando e exibindo a Precisão
precision = precision_score(y_test, y_pred, average='weighted')
print(f"Precisão (Weighted): {precision:.2f}")

# Calculando e exibindo o Recall
recall = recall_score(y_test, y_pred, average='weighted')
print(f"Recall (Weighted): {recall:.2f}")

# Calculando e exibindo o F1-Score
f1 = f1_score(y_test, y_pred, average='weighted')
print(f"F1-Score (Weighted): {f1:.2f}")

# Calculando e exibindo a Matriz de Confusão
matrix = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão:")
print(matrix)
