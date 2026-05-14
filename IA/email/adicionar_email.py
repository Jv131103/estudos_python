from pathlib import Path
import pandas as pd

from pipeline import (
    extrair_features_email,
    validar_email,
    normalizar_email,
)


CAMINHO_CSV = Path("./IA/email/emails.csv")


def adicionar_email_csv(email):
    email = normalizar_email(email)

    features = extrair_features_email(email)
    valido = validar_email(email)

    nova_linha = {
        "email": email,
        **features,
        "valido": valido,
    }

    df_novo = pd.DataFrame([nova_linha])

    if CAMINHO_CSV.exists():
        df_antigo = pd.read_csv(CAMINHO_CSV)

        df_antigo["email"] = df_antigo["email"].apply(normalizar_email)

        df_final = pd.concat(
            [df_antigo, df_novo],
            ignore_index=True
        )

        df_final = df_final.drop_duplicates(
            subset=["email"],
            keep="last"
        )

    else:
        df_final = df_novo

    df_final.to_csv(CAMINHO_CSV, index=False)

    return nova_linha
