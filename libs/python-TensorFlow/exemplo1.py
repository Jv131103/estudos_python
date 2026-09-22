import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from tensorflow import keras

# Carregar o dataset
fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print()
print(train_images.shape)
print(len(train_labels))
print(train_labels)
print(test_images.shape)
print(len(test_labels))

# Salva as classes
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Exibir algumas imagens
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(train_images[i])
    plt.xlabel(class_names[train_labels[i]])
plt.show()

# Normalizar os dados
train_images = train_images / 255.0
test_images = test_images / 255.0


# Torna as imagens lineares - Entrada para o Sklearn
def flatten(f):
    flat_list = [item for sublist in f for item in sublist]
    return flat_list


# Criar as features para uso do sklearn
train_images_features = [flatten(image) for image in train_images]
test_images_features = [flatten(image) for image in test_images]

# Arquitetura da rede
ann = MLPClassifier(hidden_layer_sizes=(128,),
                    activation="relu",
                    solver="adam",
                    learning_rate_init=0.001,
                    max_iter=10,
                    random_state=42,
                    verbose=True)

# Treinamento do modelo
ann.fit(train_images_features, train_labels)

# Predição e avaliação
preds = ann.predict(test_images_features)
print("Acurácia: ", accuracy_score(test_labels, preds))

# Definição da semente de aleatoriedade
tf.random.set_seed(42)

# Define o modelo
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

# Compilar o modelo
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"]
              )

# O que tem neste modelo?
model.summary()

# Treinamento do modelo
model.fit(train_images, train_labels, epochs=10)

# Avaliação do modelo
test_loss, test_acc = model.evaluate(test_images, test_labels)

print("Test loss: ", test_loss)
print("Test  ACC: ", test_acc)
