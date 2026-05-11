# =========================
# IMPORTS
# =========================

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# =========================
# CONFIGURAÇÕES
# =========================

CAMINHO_DATASET = "./libs/python-ScikitLearn/fertilizer_prediction.csv"


# =========================
# CARREGAMENTO DO DATASET
# =========================

def carregar_dataset(caminho):
    df = pd.read_csv(caminho)

    # Padroniza os nomes das colunas
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    return df


# =========================
# VISUALIZAÇÃO INICIAL
# =========================

def visualizar_dados_iniciais(df):
    print("\nPrimeiras linhas do dataset:")
    print(df.head())

    print("\nInformações gerais:")
    print(df.info())

    print("\nColunas do dataset:")
    print(df.columns)

    print("\nDimensão do dataset:")
    print(df.shape)


# =========================
# INFORMAÇÕES PARA LIMPEZA
# =========================

def retornar_informacoes_relevantes(df):
    duplicados = df.duplicated().sum()
    print("\nNúmero de dados duplicados:", duplicados)

    print("\nValores ausentes por coluna:")
    print(df.isnull().sum())

    colunas_numericas = df.select_dtypes(include="number").columns

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df[colunas_numericas])
    plt.title("Boxplot para detectar outliers")
    plt.xticks(rotation=45)
    plt.show()


# =========================
# DISTRIBUIÇÃO DOS LABELS
# =========================

def explorar_distribuicao_labels(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(x="Fertilizer_Name", data=df)
    plt.title("Distribuição dos Tipos de Fertilizantes")
    plt.xlabel("Fertilizante")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.show()


# =========================
# CORRELAÇÃO
# =========================

def visualizar_correlacao(df):
    colunas_numericas = df.select_dtypes(include="number")

    plt.figure(figsize=(12, 8))
    sns.heatmap(
        colunas_numericas.corr(),
        annot=True,
        cmap="coolwarm"
    )
    plt.title("Matriz de Correlação")
    plt.show()


# =========================
# AJUSTES / LIMPEZA
# =========================

def ajustar_dataset(df):
    df = df.copy()

    # Remove dados duplicados
    df = df.drop_duplicates()

    # Tratamento simples de outliers na coluna Temperature
    limite_inferior = df["Temperature"].quantile(0.025)
    limite_superior = df["Temperature"].quantile(0.975)
    mediana_temperature = df["Temperature"].median()

    df["Temperature"] = df["Temperature"].apply(
        lambda valor: mediana_temperature
        if valor < limite_inferior or valor > limite_superior
        else valor
    )

    print("\nDimensão após ajustes:")
    print(df.shape)

    return df


# =========================
# PREPARAÇÃO DOS DADOS
# =========================

def preparar_dados_para_modelo(df):
    # Separando features e label
    X = df.drop("Fertilizer_Name", axis=1)
    y = df["Fertilizer_Name"]

    # Label Encoder para a variável alvo
    le = LabelEncoder()
    y = le.fit_transform(y)

    # Colunas categóricas
    categorical_cols = ["Soil_Type", "Crop_Type"]

    # One-Hot Encoding nas colunas categóricas
    ohe = OneHotEncoder(handle_unknown="ignore", sparse_output=False)

    X_encoded = pd.DataFrame(
        ohe.fit_transform(X[categorical_cols]),
        columns=ohe.get_feature_names_out(categorical_cols),
        index=X.index
    )

    # Removendo colunas categóricas originais
    X = X.drop(categorical_cols, axis=1)

    # Concatenando features numéricas + categóricas codificadas
    X = pd.concat([X, X_encoded], axis=1)

    # Dividindo treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Normalização
    scaler = MinMaxScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, le, ohe, scaler


# =========================
# TREINAMENTO DOS MODELOS
# =========================

def treinar_modelos(X_train_scaled, X_test_scaled, y_train, y_test):
    print("\n" + "=" * 50)
    print("REGRESSÃO LOGÍSTICA")
    print("=" * 50)

    # Regressão Logística
    logreg = LogisticRegression(max_iter=1000)

    logreg.fit(X_train_scaled, y_train)

    y_pred_logreg = logreg.predict(X_test_scaled)

    print("Acurácia Regressão Logística:")
    print(accuracy_score(y_test, y_pred_logreg))

    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred_logreg))

    print("\n" + "=" * 50)
    print("KNN")
    print("=" * 50)

    # KNN
    knn = KNeighborsClassifier(n_neighbors=9)

    knn.fit(X_train_scaled, y_train)

    y_pred_knn = knn.predict(X_test_scaled)

    print("Acurácia KNN:")
    print(accuracy_score(y_test, y_pred_knn))

    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred_knn))

    print("\n" + "=" * 50)
    print("SVM - KERNEL RBF")
    print("=" * 50)

    # SVM com kernel RBF
    svm_rbf = SVC(kernel="rbf")

    svm_rbf.fit(X_train_scaled, y_train)

    y_pred_svm_rbf = svm_rbf.predict(X_test_scaled)

    print("Acurácia SVM (RBF):")
    print(accuracy_score(y_test, y_pred_svm_rbf))

    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred_svm_rbf))

    print("\n" + "=" * 50)
    print("SVM - KERNEL POLINOMIAL")
    print("=" * 50)

    # SVM com kernel polinomial
    svm_poly = SVC(kernel="poly")

    svm_poly.fit(X_train_scaled, y_train)

    y_pred_svm_poly = svm_poly.predict(X_test_scaled)

    print("Acurácia SVM (Polinomial):")
    print(accuracy_score(y_test, y_pred_svm_poly))

    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred_svm_poly))

    print("\n" + "=" * 50)
    print("SVM - KERNEL LINEAR")
    print("=" * 50)

    # SVM com kernel linear
    svm_linear = SVC(kernel="linear")

    svm_linear.fit(X_train_scaled, y_train)

    y_pred_svm_linear = svm_linear.predict(X_test_scaled)

    print("Acurácia SVM (Linear):")
    print(accuracy_score(y_test, y_pred_svm_linear))

    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred_svm_linear))

    print("\n" + "=" * 50)
    print("DECISION TREE")
    print("=" * 50)

    # Decision Tree
    dt = DecisionTreeClassifier(random_state=42)

    dt.fit(X_train_scaled, y_train)

    y_pred_dt = dt.predict(X_test_scaled)

    print("Acurácia Decision Tree:")
    print(accuracy_score(y_test, y_pred_dt))

    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred_dt))


    print("\n" + "=" * 50)
    print("RANDOM FOREST")
    print("=" * 50)

    # Random Forest
    rf = RandomForestClassifier(
        n_estimators=25,
        random_state=42
    )

    rf.fit(X_train_scaled, y_train)

    y_pred_rf = rf.predict(X_test_scaled)

    print("Acurácia Random Forest:")
    print(accuracy_score(y_test, y_pred_rf))

    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred_rf))

    return (
        logreg,
        knn,
        svm_rbf,
        svm_poly,
        svm_linear,
        dt,
        rf
    )


# =========================
# EXECUÇÃO PRINCIPAL
# =========================

df = carregar_dataset(CAMINHO_DATASET)

# visualizar_dados_iniciais(df)

# retornar_informacoes_relevantes(df)

# explorar_distribuicao_labels(df)

# visualizar_correlacao(df)

df = ajustar_dataset(df)

X_train_scaled, X_test_scaled, y_train, y_test, le, ohe, scaler = preparar_dados_para_modelo(df)

print("\nDados preparados com sucesso!")
print("X_train:", X_train_scaled.shape)
print("X_test:", X_test_scaled.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)


(
    logreg,
    knn,
    svm_rbf,
    svm_poly,
    svm_linear,
    dt,
    rf
) = treinar_modelos(
    X_train_scaled,
    X_test_scaled,
    y_train,
    y_test
)
print(
    logreg,
    knn,
    svm_rbf,
    svm_poly,
    svm_linear,
    dt,
    rf
)
