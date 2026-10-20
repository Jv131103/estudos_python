import re
import string

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

df = pd.read_csv('./IA/series_temporais/SPAM text message 20170820 - Data.csv')
print(df.shape)

# Inspecionando os tipos de dados
print(df.info())

# Analisando a distribuição das classes
print()
print(df['Category'].value_counts())
print()

# Visualizando a distribuição de spam/ham
df['Category'].value_counts().plot(kind='bar')
plt.title('Distribuição de Spam/Ham')
plt.xlabel('Categoria')
plt.ylabel('Contagem')
plt.show()

# Explore the text data
print("Sample Spam Messages:")
print(df[df['Category'] == 'spam']['Message'].sample(5))

print("\nSample Ham Messages:")
print(df[df['Category'] == 'ham']['Message'].sample(5))


def clean_text(text):
    """Limpa o texto de entrada removendo HTML, pontuação e convertendo para minúsculas."""
    if isinstance(text, str):
        text = BeautifulSoup(text, "lxml").text
        text = re.sub(r'\|\|\|', r' ', text)
        text = re.sub(r'http\S+', r'<URL>', text)
        text = text.lower()
        text = text.replace('x', '')
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = text.lower()
    return text


# Aplique a função clean_text à coluna 'Message' e crie uma nova coluna 'Cleaned_Message'
df['Cleaned_Message'] = df['Message'].apply(clean_text)

# Verifique se há valores ausentes na coluna 'Cleaned_Message'
print(df['Cleaned_Message'].isnull().sum())

# Divida os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    df['Cleaned_Message'],
    df['Category'],
    test_size=0.2,
    random_state=42,
    stratify=df['Category']
)

# Preparar rótulos de destino (converter 'Categoria' em representação numérica)
label_mapping = {'ham': 0, 'spam': 1}
y_train = y_train.map(label_mapping)
y_test = y_test.map(label_mapping)

# Bag-of-Words (BoW)
vectorizer_bow = CountVectorizer()
X_train_bow = vectorizer_bow.fit_transform(X_train)
X_test_bow = vectorizer_bow.transform(X_test)

# TF-IDF
vectorizer_tfidf = TfidfVectorizer()
X_train_tfidf = vectorizer_tfidf.fit_transform(X_train)
X_test_tfidf = vectorizer_tfidf.transform(X_test)

# Embeddings de palavras (usando embeddings de palavras médios como exemplo)
# Você pode substituir isso pelo seu modelo de embedding de palavras preferido
# (Word2Vec ou GloVe) e lidar com palavras fora do vocabulário adequadamente.
def get_average_word_embedding(text, word_embedding_model):
    """
    Calculates the average word embedding of a text.

    Args:
        text: The input text string.
        word_embedding_model: A dictionary mapping words to their embeddings.

    Returns:
        The average word embedding of the text, or a zero vector if no words are found.
    """
    words = text.split()
    embeddings = [word_embedding_model.get(word, np.zeros(300)) for word in words]
    if embeddings:
        return np.mean(embeddings, axis=0)
    else:
        return np.zeros(300)


# Espaço reservado para um modelo de incorporação de palavras pré-treinado
word_embedding_model = {}

X_train_embeddings = np.array([get_average_word_embedding(text, word_embedding_model) for text in X_train])
X_test_embeddings = np.array([get_average_word_embedding(text, word_embedding_model) for text in X_test])

# Modelos para representação BoW
lr_bow = LogisticRegression(max_iter=1000)
lr_bow.fit(X_train_bow, y_train)

svm_bow = SVC()
svm_bow.fit(X_train_bow, y_train)

nb_bow = MultinomialNB()
nb_bow.fit(X_train_bow, y_train)

rf_bow = RandomForestClassifier()
rf_bow.fit(X_train_bow, y_train)

# Modelos para representação TF-IDF
lr_tfidf = LogisticRegression(max_iter=1000)
lr_tfidf.fit(X_train_tfidf, y_train)

svm_tfidf = SVC()
svm_tfidf.fit(X_train_tfidf, y_train)

nb_tfidf = MultinomialNB()
nb_tfidf.fit(X_train_tfidf, y_train)

rf_tfidf = RandomForestClassifier()
rf_tfidf.fit(X_train_tfidf, y_train)

# Modelos para Word Embeddings
lr_embeddings = LogisticRegression(max_iter=1000)
lr_embeddings.fit(X_train_embeddings, y_train)

svm_embeddings = SVC()
svm_embeddings.fit(X_train_embeddings, y_train)

rf_embeddings = RandomForestClassifier()
rf_embeddings.fit(X_train_embeddings, y_train)

nb_embeddings = MultinomialNB()
nb_embeddings.fit(X_train_embeddings, y_train)

# Dicionário de modelos treinados
trained_models = {
    'lr_bow': lr_bow,
    'svm_bow': svm_bow,
    'nb_bow': nb_bow,
    'rf_bow': rf_bow,
    'lr_tfidf': lr_tfidf,
    'svm_tfidf': svm_tfidf,
    'nb_tfidf': nb_tfidf,
    'rf_tfidf': rf_tfidf,
    'lr_embeddings': lr_embeddings,
    'svm_embeddings': svm_embeddings,
    'rf_embeddings': rf_embeddings,
    'nb_embeddings': nb_embeddings,
}

evaluation_results = {}

for model_name, model in trained_models.items():
    if 'bow' in model_name:
        y_pred = model.predict(X_test_bow)
    elif 'tfidf' in model_name:
        y_pred = model.predict(X_test_tfidf)
    elif 'embeddings' in model_name:
        y_pred = model.predict(X_test_embeddings)
    else:
        continue

    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    evaluation_results[model_name] = {
        'accuracy': accuracy,
        'f1_score': f1,
        'confusion_matrix': conf_matrix,
    }

# Vizualiza os resultados como um dataframe ordenado por acurácia
pd.DataFrame(evaluation_results).T.sort_values(by='accuracy', ascending=False)

# Escolhendo o MELHOR e o PIOR modelo para plotar a matriz de confusão
melhor = "lr_bow"
pior = "svm_embeddings"


def plot_confusion_matrix(results, model_name):
    conf_matrix = results['confusion_matrix']
    plt.figure(figsize=(6, 4))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title(f'Confusion Matrix for {model_name}')
    plt.show()


plot_confusion_matrix(evaluation_results[melhor], melhor)
print()
plot_confusion_matrix(evaluation_results[pior], pior)
