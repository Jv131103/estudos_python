# Imports
import numpy as np
import seaborn as sns
import tensorflow as tf
import tensorflow_datasets as tfds
from sklearn.metrics import confusion_matrix
from tensorflow.keras import Sequential, layers, models
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Rescaling  # Import corrigido aqui
from tensorflow.keras.utils import to_categorical

# Carregar o dataset
(train_ds, train_labels), (test_ds, test_labels) = tfds.load(
    "tf_flowers",
    split=["train[:70%]", "train[:30%]"],
    batch_size=-1,
    as_supervised=True
)

# Verificando o tamanho das variáveis
print("Tamanho do treino:", train_ds.shape)
print("Tamanho do teste:", test_ds.shape)
print("Labels do treino:", train_labels)

# Tamanho alvo: 150x150 pixels
size = (150, 150)

# Redimensionando os conjuntos de treino e teste
train_ds = tf.image.resize(train_ds, size)
test_ds = tf.image.resize(test_ds, size)

# Aplicando a representação categórica dos labels
train_labels = to_categorical(train_labels, num_classes=5)
test_labels = to_categorical(test_labels, num_classes=5)

# Verificando o tamanho das variáveis
print("Novas dimensões do treino: ")
print(train_ds.shape)
print("Nova representação dos labels: ")
print(train_labels)

# Definir a arquitetura da CNN -> camada de extração de features
hand_model = Sequential()

# Forma moderna de definir a entrada para evitar o UserWarning
hand_model.add(layers.Input(shape=(150, 150, 3)))
hand_model.add(Rescaling(1. / 255))

# Adicionando as camadas de convolução (.add em vez de .addlayers)
hand_model.add(layers.Conv2D(16, kernel_size=10, activation="relu"))
hand_model.add(layers.MaxPooling2D(3))

hand_model.add(layers.Conv2D(32, kernel_size=8, activation="relu"))
hand_model.add(layers.MaxPooling2D(2))

hand_model.add(layers.Conv2D(32, kernel_size=6, activation="relu"))
hand_model.add(layers.MaxPooling2D(2))

# Definir a arquitetura da CNN -> camada de decisão (classificação)
hand_model.add(layers.Flatten())                       # entrada
hand_model.add(layers.Dense(50, activation="relu"))    # 1ª camada oculta
hand_model.add(layers.Dense(20, activation="relu"))    # 2ª camada oculta
hand_model.add(layers.Dense(5, activation="softmax"))  # camada de decisão

# Compilar o modelo
hand_model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# Definir a estratégia de Early Stopping
es = EarlyStopping(
    monitor="val_accuracy",
    patience=5,
    restore_best_weights=True
)

# Treina o modelo
with tf.device("/device:GPU:0"):
    hand_model.fit(
        train_ds, train_labels,
        epochs=50,
        validation_split=0.2,
        batch_size=32,
        callbacks=[es]
    )

# Avaliação do modelo
loss, acc = hand_model.evaluate(test_ds, test_labels)

print(f"A loss do modelo é {loss:.2f} e a ACC é {acc:.2f}")


# Função para obter a matriz de confusão
def plot_confusion_matrix(y_test, y_pred):
    labels = list(map(np.argmax, y_test))
    labels_pred = list(map(np.argmax, y_pred))

    cf_matrix = confusion_matrix(labels, labels_pred)
    sns.heatmap(cf_matrix, annot=True)


# Matriz de confusão
preds = hand_model.predict(test_ds)
plot_confusion_matrix(test_labels, preds)

# Preprocessa os dados de treinamento e teste
train_dsTL = preprocess_input(train_ds)
test_dsTL = preprocess_input(test_ds)

# Importar o modelo de base, que será a VGG16 ***sem*** a camada de decisão
base_model = VGG16(weights="imagenet", include_top=False,
                   input_shape=train_dsTL[0].shape)

# Usar os mesmos pesos da rede treinada (sem fazer fine tuning)
base_model.trainable = False

# Observa a estrutura do modelo importado
base_model.summary()

# Define as camadas
flatten_layer = layers.Flatten()
dense_layer_1 = layers.Dense(50, activation="relu")
dense_layer_2 = layers.Dense(20, activation="relu")
prediction_layer = layers.Dense(5, activation="softmax")

# Estabelece o modelo completo
model = models.Sequential([
    base_model,        # A base CNN vem da VGG16
    flatten_layer,     # Achata as features que saem da VGG16 (base_model)
    dense_layer_1,     # 1ª camada oculta fully connected
    dense_layer_2,     # 2ª camada oculta fully connected
    prediction_layer   # Camada de saída, com 5 neurônios para classificação
])

model.summary()

# Compilar o modelo
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# Definir a estratégia de Early Stopping
es = EarlyStopping(
    monitor="val_accuracy",
    patience=5,
    restore_best_weights=True
)

# Treina o modelo
with tf.device("/device:GPU:0"):
    model.fit(
        train_dsTL, train_labels,  # alterei o nome do conjunto de treino, usando o train_dsTL
        epochs=50,
        validation_split=0.2,
        batch_size=32,
        callbacks=[es]
    )

# Avaliação do modelo: acurácia
loss, acc = model.evaluate(test_dsTL, test_labels)

print(f"A loss do modelo é {loss:.2f} e a ACC é {acc:.2f}")

# Avaliação do modelo: matriz de confusão
preds = model.predict(test_dsTL)
plot_confusion_matrix(test_labels, preds)
