import warnings

warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
from sklearn.metrics import (ConfusionMatrixDisplay, accuracy_score,
                             confusion_matrix)
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# =========================
# CARREGANDO O DATASET
# =========================

iris = load_iris()

data = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

data["class"] = iris.target


# Mostra a tabela
print(data)

# Se quiser somente as primeiras linhas
print(data.head())


# =========================
# TREINO E TESTE
# =========================

X = data.drop(columns=["class"])
y = data["class"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================
# PERCEPTRON
# =========================

p = Perceptron(random_state=42)

p.fit(X_train, y_train)

y_pred = p.predict(X_test)


# =========================
# ACURÁCIA
# =========================

print("\nAcurácia:")
print(accuracy_score(y_test, y_pred))


# =========================
# MATRIZ DE CONFUSÃO
# =========================

def matriz_confusao(teste_labels, teste_preds, labels):

    cm = confusion_matrix(
        teste_labels,
        teste_preds,
        labels=labels
    )

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=labels
    )

    disp.plot(cmap="Blues")

    plt.show()


matriz_confusao(
    y_test,
    y_pred,
    p.classes_
)


# =========================
# PAIRPLOT
# =========================

sns.pairplot(
    data=data,
    vars=[
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)"
    ],
    hue="class"
)

plt.show()

# Arquitetura
mlp = MLPClassifier(
    hidden_layer_sizes=(5,),
    verbose=True,
    max_iter=200,
    random_state=1
)

# Treinamento
mlp.fit(X_train, y_train)
y_pred = mlp.predict(X_test)

# Avaliação
matriz_confusao(y_test, y_pred, mlp.classes_)

# Alterando a função de ativação...
mlp = MLPClassifier(
    hidden_layer_sizes=(5,),
    verbose=False,
    max_iter=50,
    random_state=1,
    activation="logistic"
)

mlp.fit(X_train, y_train)
y_pred = mlp.predict(X_test)

matriz_confusao(y_test, y_pred, mlp.classes_)

#Alterando o solver para o que a própria documentação aconselha para datasets menores
mlp = MLPClassifier(
    hidden_layer_sizes=(5,),
    verbose=False,
    max_iter=50,
    random_state=1,
    activation="logistic",
    solver="lbfgs"
)

mlp.fit(X_train, y_train)
y_pred = mlp.predict(X_test)

print("ACC Teste: ", accuracy_score(y_test, y_pred))

matriz_confusao(y_test, y_pred, mlp.classes_)
