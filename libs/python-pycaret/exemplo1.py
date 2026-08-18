# Imports
import numpy as np
import pandas as pd
import pycaret
from pycaret.regression import *
from sklearn.model_selection import train_test_split

df = pd.read_csv("insurance.csv")
df.sample(10)

# Divisão de treino e teste
train, test = train_test_split(df,
                               test_size=0.2,
                               random_state=42)

# IMPORTANTE: o pycaret sempre começa com o setup()
reg = setup(data=train,         # Dados para treino
            target="charges",   # Label a ser predito
            train_size=0.7)     # Proporção de dados para treino (o resto é validação)

# Agora vamos comparar diversos modelos de regressão
compare_models(sort="R2")

# Crie o melhor modelo
gbr = create_model("gbr")

# Como tunar um modelo no próprio pycaret?
tuned_gbr = tune_model(gbr)

# Comparar predições e resultados
plot_model(tuned_gbr, plot="error")

# Quais são as features mais importantes?
plot_model(tuned_gbr, plot="feature")

# Fazendo predições no TESTE
predict_model(tuned_gbr, data=test)

# Finalizar o modelo, criando a versão completa treinada em TODOS os dados
gbr_final = finalize_model(tuned_gbr)
