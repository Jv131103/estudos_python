# Ignorar warnings
import warnings

warnings.filterwarnings("ignore")

# Bibliotecas para uso e visualização de dados
import numpy as np
import pandas as pd
# Import de modelos preditivos
from sklearn.linear_model import LinearRegression
# Import de métricas
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Imports para seleção de modelos
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neural_network import MLPRegressor
# Imports para preparação de dados
from sklearn.preprocessing import StandardScaler


def metricas(X_tr_scaled, y_tr, y_ts, y_pr, model, id_modelo):

    y_pr_tr = model.predict(X_tr_scaled)

    # Erro quadrático médio
    print(f"MSE do TREINO ({id_modelo}): ", mean_squared_error(y_tr, y_pr_tr))
    print(f"MSE do TESTE  ({id_modelo}): ", mean_squared_error(y_ts, y_pr))

    # Erro absoluto médio
    print(f"MAE do TREINO ({id_modelo}): ", mean_absolute_error(y_tr, y_pr_tr))
    print(f"MAE do TESTE  ({id_modelo}): ", mean_absolute_error(y_ts, y_pr))

    # R²
    print(f"R² do TREINO ({id_modelo}): ", r2_score(y_tr, y_pr_tr))
    print(f"R² do TESTE  ({id_modelo}): ", r2_score(y_ts, y_pr))


df = pd.read_csv("./libs/python-ScikitLearn/advertising.csv")

# Separação de DADOS e LABEL
X = df.drop(columns=["Sales"])
y = df["Sales"]

# Dividindo dados para TREINO e TESTE
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Padronização dos dados
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train)
X_test_scaled = ss.transform(X_test)

# Treinando o modelo
modelo = LinearRegression()
modelo.fit(X_train_scaled, y_train)

# Fazendo as predições
y_pred = modelo.predict(X_test_scaled)

# Metricas para regressao linear
metricas(X_train_scaled, y_train, y_test, y_pred, modelo, "Reg Linear")

# Treinando uma RNA padrão e realizando predições
modelo_rn = MLPRegressor(max_iter=1000, random_state=97)
modelo_rn.fit(X_train_scaled, y_train)
y_pred_rn = modelo_rn.predict(X_test_scaled)

# Metricas para RNA otimizada
metricas(X_train_scaled, y_train, y_test, y_pred_rn, modelo_rn, "RN")

# Treinando uma RNA padrão e realizando predições
modelo_otimizado = MLPRegressor(hidden_layer_sizes=(10, 5,),
                         max_iter=1000,
                         solver="lbfgs",
                         learning_rate="adaptive",
                         random_state=97)
modelo_otimizado.fit(X_train_scaled, y_train)
y_pred_rn = modelo_otimizado.predict(X_test_scaled)

# Metricas para RNA otimizada
metricas(X_train_scaled, y_train, y_test, y_pred_rn, modelo_otimizado, "RN OTIMIZADO")

# Treinando uma RNA padrão e realizando predições
modelo_otimizado = MLPRegressor(hidden_layer_sizes=(10, 5,),
                         max_iter=1000,
                         solver="lbfgs",
                         learning_rate="adaptive",
                         random_state=93)
modelo_otimizado.fit(X_train_scaled, y_train)
y_pred_rn = modelo_otimizado.predict(X_test_scaled)

# Metricas para RNA otimizada
metricas(X_train_scaled, y_train, y_test, y_pred_rn, modelo_otimizado, "RN OTIMIZADO 2")

# Treinando uma RNA padrão e realizando predições
modelo_otimizado = MLPRegressor(hidden_layer_sizes=(10, 5,),
                         max_iter=1000,
                         solver="lbfgs",
                         learning_rate="adaptive",
                         random_state=3)
modelo_otimizado.fit(X_train_scaled, y_train)
y_pred_rn = modelo_otimizado.predict(X_test_scaled)

# Metricas para RNA otimizada
metricas(X_train_scaled, y_train, y_test, y_pred_rn, modelo_otimizado, "RN OTIMIZADO 3")
