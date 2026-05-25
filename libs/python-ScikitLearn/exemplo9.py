import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder


data = {
    "Cultura": ["Milho", "Soja", "Café", "Cana-de-açúcar", "Arroz", "Algodão"],
    "Região": ["Norte", "Sul", "Sudeste", "Nordeste", "Centro-Oeste", "Nordeste"],
    "Produção (toneladas)": [5000, 12000, 8000, 15000, 11000, 7000],
    "Preço por Tonelada (R$)": [750, 1300, 2000, 600, 900, 1400],
    "Tipo de Solo": ["Argiloso", "Arenoso", "Misto", "Argiloso", "Arenoso", "Misto"]
}

df_agro = pd.DataFrame(data)

print("Dataset original:")
print(df_agro.head())

print("\n" + "=" * 80 + "\n")

# Label Encoding na coluna Cultura
label_encoder = LabelEncoder()
df_agro["Cultura_LabelEncoded"] = label_encoder.fit_transform(df_agro["Cultura"])

print("Label Encoding - Cultura:")
print(df_agro[["Cultura", "Cultura_LabelEncoded"]])

print("\n" + "=" * 80 + "\n")

# One-Hot Encoding na coluna Região
onehot_encoder = OneHotEncoder(sparse_output=False)

onehot_encoded = onehot_encoder.fit_transform(df_agro[["Região"]])

encoded_columns = onehot_encoder.get_feature_names_out(["Região"])

onehot_df = pd.DataFrame(
    onehot_encoded,
    columns=encoded_columns,
    index=df_agro.index
)

df_agro = pd.concat([df_agro, onehot_df], axis=1)

print("One-Hot Encoding - Região:")
print(df_agro[["Região"] + list(encoded_columns)])

print("\n" + "=" * 80 + "\n")

# Ordinal Encoding na coluna Tipo de Solo
ordinal_encoder = OrdinalEncoder(
    categories=[["Arenoso", "Argiloso", "Misto"]]
)

df_agro["TipoSolo_OrdinalEncoded"] = ordinal_encoder.fit_transform(
    df_agro[["Tipo de Solo"]]
)

print("Ordinal Encoding - Tipo de Solo:")
print(df_agro[["Tipo de Solo", "TipoSolo_OrdinalEncoded"]])

print("\n" + "=" * 80 + "\n")


wine = load_wine()

df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)
df_wine["target"] = wine.target

X = df_wine.drop(columns=["target"])
y = df_wine["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

print("Tamanho do conjunto original:", X.shape)
print("Tamanho do conjunto de treinamento:", X_train.shape)
print("Tamanho do conjunto de teste:", X_test.shape)

print("\nTarget antes do split:")
print(df_wine["target"].head())

print("\nTarget de treinamento:")
print(y_train.head())
