from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("./IA/arvores_decisao/alunos.csv")

X = df[["horas_estudo", "faltas", "sono_horas"]]
y = df["aprovado"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
