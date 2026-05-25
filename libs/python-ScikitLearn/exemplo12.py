import numpy as np
from sklearn.metrics import accuracy_score  # importa método da acurácia

# Cria dois array de teste
y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]

# Calcula acurácia
print(accuracy_score(y_true, y_pred))
