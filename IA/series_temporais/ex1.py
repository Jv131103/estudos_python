# Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.layers import LSTM, Dense, Dropout
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import layers, models

# Leitura do dataset
df = pd.read_csv("./IA/series_temporais/LSTM_TATA_train.csv")
print(df)

# Puxando apenas a coluna do valor da ação na ABERTURA
training_set = df.iloc[:, 1:2].values
print(type(training_set))

# Plotando a série histórica
plt.figure(figsize=(20, 9))
plt.plot(range(df.shape[0]),
         df["Open"][-1::-1])
plt.title("Série temporal da ação")
plt.xticks(
    range(0, df["Date"].shape[0], 50),
    df["Date"][-1: 0: -50],
    rotation=45
)
plt.xlabel("Datas")
plt.ylabel("Preço de abertura")
plt.show()

# Padronizando os dados
mm = MinMaxScaler()
training_set_scaled = mm.fit_transform(training_set)

print(training_set_scaled)

# Criando o dataset da série temporal
X_train = []
y_train = []
for i in range(60, 2035):
    X_train.append(training_set_scaled[i - 60: i, 0])
    y_train.append(training_set_scaled[i, 0])

X_train, y_train = np.array(X_train), np.array(y_train)

# Reescalando o formato do treino
X_train = np.reshape(X_train, (X_train.shape[0],
                               X_train.shape[1],
                               1))

print(X_train.shape)

# Definindo a arquitetura da rede
reg = Sequential()

reg.add(LSTM(
    units=50,
    return_sequences=True,
    input_shape=(X_train.shape[1], 1))
)
reg.add(Dropout(0.2))

reg.add(LSTM(
    units=50,
    return_sequences=True)
)
reg.add(Dropout(0.2))

reg.add(LSTM(
    units=50,
    return_sequences=True)
)
reg.add(Dropout(0.2))

reg.add(LSTM(units=50))
reg.add(Dropout(0.2))

reg.add(Dense(units=1))

# Compilando a rede montada
reg.compile(optimizer="adam", loss="mean_squared_error")

# Treinando a rede
with tf.device('/device:GPU:0'):
    reg.fit(
        X_train,
        y_train,
        epochs=100,
        batch_size=32
    )

# Lendo os dados de teste
df_test = pd.read_csv("./IA/series_temporais/LSTM_TATA_test.csv")
real_stock_price = df_test.iloc[:, 1:2].values

# Considerando que os dados são contínuos, temos que concatenar os arquivos
dataset_total = pd.concat((df["Open"],
                          df_test["Open"]),
                          axis=0)

# Dos dados concatenados, os exemplos de teste estão no final da
# concatenação pulando os últimos 60, devido ao tamanho da nossa
# janela. Aplique a padronização também (MinMax)
inputs = dataset_total[len(dataset_total) - len(df_test) - 60:].values
inputs = inputs.reshape(-1, 1)
inputs = mm.transform(inputs)

# Preparando os dados de teste nos mesmos moldes dos dados de treinamento
X_test = []
for i in range(60, 76):
    X_test.append(inputs[i - 60: i, 0])

# Ajustando o tamanho do teste, nos mesmos moldes do treinamento
X_test = np.array(X_test)
X_test = np.reshape(X_test,
                    (X_test.shape[0], X_test.shape[1], 1))

# Predizendo valores das ações
predicted_stock_prices = reg.predict(X_test)

# Voltando os valores preditos na escala [0, 1] para a escala original
predicted_stock_prices = mm.inverse_transform(predicted_stock_prices)

# Mostrando os resultados
plt.plot(real_stock_price,
         color="black",
         label="Ações da TATA")
plt.plot(predicted_stock_prices,
         color="green",
         label="Ações PREDITAS da TATA")
plt.title("Predição de ações da TATA Consultoria")
plt.xlabel("Tempo")
plt.xticks(
    range(0, df_test["Date"].shape[0]),
    df_test["Date"].loc[-1: 0: -1],
    rotation=45
)
plt.ylabel("Preço da ação")
plt.legend()
plt.show()
