# Suprimir warnings
import warnings

warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import numpy as np
# Leitura de dados e gráficos
import pandas as pd
import seaborn as sns
import shap
# Preparação de dados
from imblearn.under_sampling import RandomUnderSampler
# Interpretabilidade de modelos
from lime import lime_tabular
# Modelos preditivos
from sklearn.ensemble import (AdaBoostClassifier, BaggingClassifier,
                              RandomForestClassifier, StackingClassifier,
                              VotingClassifier)
from sklearn.linear_model import LogisticRegression
# Avaliação de modelos
from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score,
                             precision_score, recall_score)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier


# Avaliando os modelos de classificação, calculando algumas métricas
def avaliar_modelo(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    return accuracy, precision, recall, f1


# Plota a matriz de confusão
def plotar_matriz_confusao(y_true, y_pred, title):

    # Matriz de confusão
    cm = confusion_matrix(y_true, y_pred)

    # Plot da matriz de confusão
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Não Saiu', 'Saiu'],
                yticklabels=['Não Saiu', 'Saiu'])
    plt.xlabel('Predição')
    plt.ylabel('Valor Real')
    plt.title(title)
    plt.show()


# CARREGAMENTO DOS DADOS
data = pd.read_csv('./libs/python-lime-and-shap/churn_modelling.csv')
print(data.sample(10))

# ANÁLISE EXPLORATÓRIA

#   - Informações gerais do dataset
print(data.info())

#   - Análises estatísticas gerais
print(data.describe())

#   - Identificação de duplicatas
print(f"Número de linhas duplicadas: {data.duplicated().sum()}")
# plt.title(title)
plt.show()

# Identificação de outliers via Boxplots:

#   - Selecionar as variáveis para o boxplot
features = ['Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']

#   - Criar uma figura com 2 linhas e 4 colunas
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

#   - Iterar pelas variáveis e criar o boxplot em cada subplot
for i, feature in enumerate(features):
    row = i // 3
    col = i % 3
    sns.boxplot(y=data[feature], ax=axes[row, col])
    axes[row, col].set_title(feature)

#   - Ajustar o layout da figura
plt.tight_layout()
plt.show()

# Plot da matriz de correlação com mapa de calor
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr(numeric_only=True),
            annot=True,
            cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlação')
plt.show()

# Eliminando linhas duplicadas
data.drop_duplicates(inplace=True)

# Eliminando features que não fazem sentido para o problema
data.drop(columns=['RowNumber', 'CustomerId', 'Surname'], inplace=True)

# Plotar o desbalanceamento da variável "Exited"
plt.figure(figsize=(6, 4))
sns.countplot(x='Exited', data=data)
plt.title('Distribuição da variável Exited')
plt.xlabel('Exited')
plt.ylabel('Contagem')
plt.show()

# Separar as features (X) e o target (y)
X = data.drop('Exited', axis=1)
y = data['Exited']

# Criar o objeto RandomUnderSampler
rus = RandomUnderSampler(sampling_strategy={0: int(y.value_counts()[0] * 0.4)}, random_state=42)

# Aplicar o undersampling aos dados
X_resampled, y_resampled = rus.fit_resample(X, y)

# Criar um novo DataFrame com os dados reamostrados
data_resampled = pd.concat([X_resampled, y_resampled], axis=1)

# Verificar a contagem de cada classe após o undersampling
plt.figure(figsize=(6, 4))
sns.countplot(x='Exited', data=data_resampled)
plt.title('Distribuição da variável Exited')
plt.xlabel('Exited')
plt.ylabel('Contagem')
plt.show()

# Convertendo variáveis categóricas para numéricas (se necessário)
X_resampled = pd.get_dummies(data_resampled, drop_first=True)

# Separando os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X_resampled.drop('Exited', axis=1),
    X_resampled['Exited'],
    test_size=0.2,
    random_state=42
)

# Padronizando as features
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train)
X_test_scaled = ss.transform(X_test)

# Modelo baseline (classificação linear)
baseline_model = LogisticRegression()
baseline_model.fit(X_train_scaled, y_train)
y_pred_baseline = baseline_model.predict(X_test_scaled)
accuracy_baseline, precision_baseline, recall_baseline, f1_baseline = avaliar_modelo(y_test, y_pred_baseline)
print(f"BASELINE: Acurácia: {accuracy_baseline:.4f}, Precisão: {precision_baseline:.4f}, Recall: {recall_baseline:.4f}, F1-Score: {f1_baseline:.4f}")

plotar_matriz_confusao(y_test, y_pred_baseline, "Matriz de Confusão - Baseline")

# Bagging - Combinação de 100 árvores independentes (similar à Floresta)
bagging_model = BaggingClassifier(estimator=DecisionTreeClassifier(),
                                  n_estimators=100,
                                  random_state=42)
bagging_model.fit(X_train_scaled, y_train)
y_pred_bagging = bagging_model.predict(X_test_scaled)

# Boosting
boosting_model = AdaBoostClassifier(n_estimators=100,
                                    random_state=42)
boosting_model.fit(X_train_scaled, y_train)
y_pred_boosting = boosting_model.predict(X_test_scaled)

# Definindo modelos base para ensembles para VOTING e STACKING
base_models = [
    ('dt', DecisionTreeClassifier(random_state=42)),
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('knn', KNeighborsClassifier()),
    ('svm', SVC())
]

# Voting - Votação entre os modelos de base
voting_model = VotingClassifier(estimators=base_models,
                                voting='hard')
voting_model.fit(X_train_scaled, y_train)
y_pred_voting = voting_model.predict(X_test_scaled)

# Stacking
stacking_model = StackingClassifier(estimators=base_models,
                                    final_estimator=LogisticRegression())
stacking_model.fit(X_train_scaled, y_train)
y_pred_stacking = stacking_model.predict(X_test_scaled)

# XGBoost
xgb_model = XGBClassifier(random_state=42)
xgb_model.fit(X_train_scaled, y_train)
y_pred_xgb = xgb_model.predict(X_test_scaled)

# Avaliação dos modelos
accuracy_bagging, precision_bagging, recall_bagging, f1_bagging = avaliar_modelo(y_test, y_pred_bagging)
accuracy_boosting, precision_boosting, recall_boosting, f1_boosting = avaliar_modelo(y_test, y_pred_boosting)
accuracy_voting, precision_voting, recall_voting, f1_voting = avaliar_modelo(y_test, y_pred_voting)
accuracy_stacking, precision_stacking, recall_stacking, f1_stacking = avaliar_modelo(y_test, y_pred_stacking)
accuracy_xgb, precision_xgb, recall_xgb, f1_xgb = avaliar_modelo(y_test, y_pred_xgb)

print(f"Bagging:\tAcurácia: {accuracy_bagging:.4f}, \
        Precisão: {precision_bagging:.4f}, \
        Recall: {recall_bagging:.4f}, \
        F1-Score: {f1_bagging:.4f}")
print()
print(f"Boosting:\tAcurácia: {accuracy_boosting:.4f}, \
        Precisão: {precision_boosting:.4f}, \
        Recall: {recall_boosting:.4f}, \
        F1-Score: {f1_boosting:.4f}")
print()
print(f"Voting:\t\tAcurácia: {accuracy_voting:.4f}, \
        Precisão: {precision_voting:.4f}, \
        Recall: {recall_voting:.4f}, \
        F1-Score: {f1_voting:.4f}")
print()
print(f"Stacking:\tAcurácia: {accuracy_stacking:.4f}, \
        Precisão: {precision_stacking:.4f}, \
        Recall: {recall_stacking:.4f}, \
        F1-Score: {f1_stacking:.4f}")
print()
print(f"XGBoost:\tAcurácia: {accuracy_xgb:.4f}, \
        Precisão: {precision_xgb:.4f}, \
        Recall: {recall_xgb:.4f}, \
        F1-Score: {f1_xgb:.4f}")
print()
# Plota as matrizes de confusão para cada modelo
plotar_matriz_confusao(y_test, y_pred_baseline, "Matriz de Confusão - Baseline")
plotar_matriz_confusao(y_test, y_pred_bagging, "Matriz de Confusão - Bagging")
plotar_matriz_confusao(y_test, y_pred_boosting, "Matriz de Confusão - Boosting")
plotar_matriz_confusao(y_test, y_pred_voting, "Matriz de Confusão - Voting")
plotar_matriz_confusao(y_test, y_pred_stacking, "Matriz de Confusão - Stacking")
plotar_matriz_confusao(y_test, y_pred_xgb, "Matriz de Confusão - XGBoost")

# LIME
explainer = lime_tabular.LimeTabularExplainer(
    X_train_scaled,
    feature_names=X_test.columns.tolist(),
    class_names=['Não Saiu', 'Saiu'],
    mode='classification'
)

# Escolha um índice da amostra de teste para explicar
i = 100
exp = explainer.explain_instance(
    X_test_scaled[i],
    stacking_model.predict_proba,
    num_features=10
)
exp.save_to_file("./libs/python-lime-and-shap/explicacao_lime.html")
print("Explicação salva em explicacao_lime.html!")

# SHAP
explainer = shap.Explainer(xgb_model.predict, X_test_scaled)
shap_values = explainer(X_test_scaled)

# Resumo das importâncias das features
shap.summary_plot(shap_values, X_test_scaled, feature_names=X_test.columns.tolist())
