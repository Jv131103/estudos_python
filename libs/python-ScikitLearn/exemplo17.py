# Importando as bibliotecas necessárias
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Carregar os dados (substitua pelo caminho do seu dataset)
crop_yield_data = pd.read_csv("./libs/python-ScikitLearn/crop_yield.csv")

# Converter dados categóricos em valores numéricos usando one-hot encoding
crop_yield_data = pd.get_dummies(crop_yield_data,
                                 columns=['Crop'],
                                 prefix=['Crop'],
                                 drop_first=True)

# Supondo que a coluna 'yield' é a variável dependente (target)
# Separar os dados em X (features) e y (target)
X = crop_yield_data.drop(columns=['Yield'])
y = crop_yield_data['Yield']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

# Escalar os dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modelo de Regressão Linear sem PCA
regressor = LinearRegression()
regressor.fit(X_train_scaled, y_train)

# Prever e calcular o erro (sem PCA)
y_pred_no_pca = regressor.predict(X_test_scaled)
mse_no_pca = mean_squared_error(y_test, y_pred_no_pca)
print(f"Erro Quadrático Médio sem PCA: {mse_no_pca}")

# Aplicar PCA para reduzir a dimensionalidade antes do treinamento
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# Modelo de Regressão Linear com PCA
regressor_pca = LinearRegression()
regressor_pca.fit(X_train_pca, y_train)

# Prever e calcular o erro (com PCA)
y_pred_pca = regressor_pca.predict(X_test_pca)
mse_with_pca = mean_squared_error(y_test, y_pred_pca)
print(f"Erro Quadrático Médio com PCA: {mse_with_pca}")

# Comparando os resultados
if mse_no_pca < mse_with_pca:
    print("O modelo sem PCA teve um desempenho melhor.")
else:
    print("O modelo com PCA teve um desempenho melhor.")
