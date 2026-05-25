import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


# Carregando novamente o dataset
wine = load_wine()
X = wine.data  # Características
y = wine.target  # Rótulos

# Convertendo para DataFrame para melhor visualização
df = pd.DataFrame(X, columns=wine.feature_names)
df['target'] = y

# Escolhendo X e y para fazer o split
X = df.drop('target', axis=1)
y = df['target']

# Dividindo o DataFrame em 70% para treino e 30% para teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Instanciando o modelo
model = RandomForestClassifier()

# Treinamento do modelo
model.fit(X_train, y_train)

# Predição
y_pred = model.predict(X_test)

# Avaliando a acurácia do modelo usando o método score()
accuracy = model.score(X_test, y_test)
print(f"Acurácia do modelo: {accuracy:.2f}")

# Testando diferentes algoritmos de classificação
# Random Forest
model_rf = RandomForestClassifier()
model_rf.fit(X_train, y_train)
accuracy_rf = model_rf.score(X_test, y_test)
print(f"Acurácia com Random Forest: {accuracy_rf:.2f}")

# SVM
model_svm = SVC()
model_svm.fit(X_train, y_train)
accuracy_svm = model_svm.score(X_test, y_test)
print(f"Acurácia com SVM: {accuracy_svm:.2f}")

# KNN
model_knn = KNeighborsClassifier()
model_knn.fit(X_train, y_train)
accuracy_knn = model_knn.score(X_test, y_test)
print(f"Acurácia com KNN: {accuracy_knn:.2f}")
