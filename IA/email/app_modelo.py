import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from pipeline import (
    preparar_dataframe,
    extrair_features_email,
    validar_email,
    FEATURES,
)
from adicionar_email import adicionar_email_csv


CAMINHO_CSV = "./IA/email/emails.csv"


def treinar_modelo():
    df = pd.read_csv(CAMINHO_CSV)
    df = preparar_dataframe(df)

    X = df[FEATURES]
    y = df["valido"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    modelo = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )

    modelo.fit(X_train, y_train)

    return modelo


modelo = treinar_modelo()


while True:
    email = input("\nDigite um email ou 'sair': ").strip()

    if email.lower() == "sair":
        print("\nEncerrando...")
        break

    valido_regra = validar_email(email)

    if valido_regra == 0:
        print("\n❌ Email INVÁLIDO pela regra de negócio")
        print("Motivo provável: formato inválido ou domínio bloqueado.")

    else:
        features = extrair_features_email(email)

        entrada = pd.DataFrame([features])
        entrada = entrada[FEATURES]

        previsao = modelo.predict(entrada)[0]
        probabilidade = modelo.predict_proba(entrada)[0][1]

        if previsao == 1:
            print("\n✅ Email provavelmente VÁLIDO")
            print(f"Probabilidade: {probabilidade:.2%}")
        else:
            print("\n❌ Email provavelmente INVÁLIDO")
            print(f"Probabilidade de ser válido: {probabilidade:.2%}")

    salvar = input(
        "\nDeseja salvar esse email no CSV e re-treinar o modelo? [s/n]: "
    ).strip().lower()

    if salvar == "s":
        linha = adicionar_email_csv(email)

        print("\nEmail salvo no CSV:")
        print(linha)

        print("\nRe-treinando modelo...")
        modelo = treinar_modelo()
        print("✅ Modelo atualizado com sucesso.")

    else:
        print("\nEmail não salvo.")
