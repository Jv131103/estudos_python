from datetime import datetime
from math import sqrt

from keras.layers import LSTM, Dense
from keras.models import Sequential
from matplotlib import pyplot
from numpy import concatenate
from pandas import DataFrame, concat, read_csv
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


# Ajusta o formato da data
def parse(x):
    return datetime.strptime(x, '%Y %m %d %H')


# Carrega o dataset
dataset = read_csv('./IA/series_temporais/raw.csv',  parse_dates = [['year', 'month', 'day', 'hour']], index_col=0, date_parser=parse)
dataset.drop('No', axis=1, inplace=True)

# Atribui nome às colunas
dataset.columns = ['pollution', 'dew', 'temp', 'press', 'wnd_dir', 'wnd_spd', 'snow', 'rain']
dataset.index.name = 'date'

# Altera os NaNs para zero
dataset['pollution'].fillna(0, inplace=True)

# Remove as primeiras 24 horas
dataset = dataset[24:]

# Salva o arquivo
dataset.to_csv('./IA/series_temporais/pollution.csv')

# Mostra as primeiras 10 linhas
print(dataset.head(10))

# Carrega o dataset
dataset = read_csv('./IA/series_temporais/pollution.csv', header=0, index_col=0)
values = dataset.values

# Especifica as colunas para plotar
groups = [0, 1, 2, 3, 5, 6, 7]
i = 1
pyplot.figure()
for group in groups:
    pyplot.subplot(len(groups), 1, i)
    pyplot.plot(values[:, group])
    pyplot.title(dataset.columns[group], y=0.5, loc='right')
    i += 1
pyplot.show()


# Converte a série em aprendizado supervisionado
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    # put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg


# Carrega a base de dados e exclui a coluna de direção do vento (categórica)
dataset = read_csv('./IA/series_temporais/pollution.csv', header=0, index_col=0)
dataset.drop(columns=['wnd_dir'], inplace=True)

# Garanta que todos os dados são numéricos
values = dataset.values
values = values.astype('float32')

# Normaliza as features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
dataset_scaled = DataFrame(scaled, columns=dataset.columns)

# Escolhe a variável a ser prevista
target_variable = 'pollution'

# Separa X (features) e y (target)
X = dataset_scaled.drop(columns=[target_variable])  # Remove a variável alvo das entradas
y = dataset_scaled[[target_variable]]               # Mantém a variável alvo separada

# Aplica a função para transformar os dados, usando 3 valores (lags) como entrada
n_lags = 3
df_X_supervised = series_to_supervised(X, n_in=n_lags, n_out=0)  # Somente entradas (X)
df_y_supervised = series_to_supervised(y, n_in=n_lags, n_out=1)  # Apenas saída (y)

# Juntando entradas (X) e saída (y)
df_final = concat([df_X_supervised, df_y_supervised.iloc[:, -1]], axis=1)

# Exibindo o DataFrame final com X e y prontos para treinamento
print(df_final.head())

# Dividindo os dados em treino e teste
values = df_final.values
n_train_hours = 365 * 24
train = values[:n_train_hours, :]
test = values[n_train_hours:, :]

# Separando features e labels
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]

# Reshape num valor 3D [samples, timesteps, features]
train_X = train_X.reshape(
    (
        train_X.shape[0],
        n_lags,
        int(train_X.shape[1] / n_lags)
    )
)
test_X = test_X.reshape(
    (
        test_X.shape[0],
        n_lags,
        int(test_X.shape[1] / n_lags)))
print()
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)

# Projeta a rede neural
model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')

# Faz o fiting do modelo no treino
history = model.fit(train_X, train_y, epochs=50,
                    batch_size=72, verbose=2, shuffle=False)

# Plota a loss do treino
pyplot.plot(history.history['loss'], label='train')
pyplot.legend()
pyplot.show()

# Faz predições no teste
yhat = model.predict(test_X)

# Calcula RMSE
rmse = sqrt(mean_squared_error(test_y, yhat))
print('Teste RMSE: %.3f' % rmse)

# Plota as curvas do TEST_Y real e predito
pyplot.plot(yhat[:100], label='y predito')  # Primeiros 100 pontos
pyplot.plot(test_y[:100], label='y real')   # Primeiros 100 pontos
pyplot.legend()
pyplot.show()
