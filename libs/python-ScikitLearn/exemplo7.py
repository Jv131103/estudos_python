from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer, KNNImputer
import pandas as pd
import numpy as np


wine = load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)
df["target"] = wine.target

print("Dataset original:")
print(df.head())

print("\n" + "=" * 80 + "\n")

X = df.drop(columns=["target"])
y = df["target"]

scaler_standard = StandardScaler()
X_scaled = scaler_standard.fit_transform(X)

df_scaled = pd.DataFrame(X_scaled, columns=X.columns)

print("Dados com StandardScaler:")
print(df_scaled.head())

print("\n" + "=" * 80 + "\n")

scaler_minmax = MinMaxScaler()
X_minmax_scaled = scaler_minmax.fit_transform(X)

df_minmax = pd.DataFrame(X_minmax_scaled, columns=X.columns)

print("Dados com MinMaxScaler:")
print(df_minmax.head())

print("\n" + "=" * 80 + "\n")

X_missing = X.copy()

X_missing.loc[0:4, "alcohol"] = np.nan
X_missing.loc[0:2, "malic_acid"] = np.nan

print("Dados com valores ausentes:")
print(X_missing.head())

print("\nQuantidade de valores ausentes por coluna:")
print(X_missing.isnull().sum())

print("\n" + "=" * 80 + "\n")

simple_imputer = SimpleImputer(strategy="mean")
X_simple_imputed_array = simple_imputer.fit_transform(X_missing)

X_simple_imputed = pd.DataFrame(
    X_simple_imputed_array,
    columns=X.columns
)

knn_imputer = KNNImputer(n_neighbors=5)
X_knn_imputed_array = knn_imputer.fit_transform(X_missing)

X_knn_imputed = pd.DataFrame(
    X_knn_imputed_array,
    columns=X.columns
)

print("SimpleImputer:")
print(X_simple_imputed.head())

print("\n" + "=" * 80 + "\n")

print("KNNImputer:")
print(X_knn_imputed.head())
