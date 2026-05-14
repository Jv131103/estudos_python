import re
import pandas as pd


REGEX_EMAIL = re.compile(
    r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$",
    re.IGNORECASE
)


DOMINIOS_BLOQUEADOS = {
    "teste.com",
    "test.com",
    "example.com",
    "fake.com",
    "email.com",
}


FEATURES = [
    "tamanho",
    "tamanho_local",
    "tamanho_dominio",
    "tem_arroba",
    "qtd_arroba",
    "tem_ponto_dominio",
    "qtd_pontos",
    "tem_numero",
    "dominio_gmail",
    "dominio_com_br",
    "dominio_br",
    "dominio_bloqueado",
    "local_vazio",
    "dominio_vazio",
]


def normalizar_email(email):
    return str(email).strip().lower()


def separar_email(email):
    email = normalizar_email(email)

    partes = email.split("@")

    if len(partes) == 2:
        local = partes[0]
        dominio = partes[1]
    else:
        local = ""
        dominio = ""

    return email, local, dominio


def validar_email(email):
    email, local, dominio = separar_email(email)

    if email == "" or email == "nan":
        return 0

    if not REGEX_EMAIL.match(email):
        return 0

    if dominio in DOMINIOS_BLOQUEADOS:
        return 0

    return 1


def extrair_features_email(email):
    email, local, dominio = separar_email(email)

    return {
        "tamanho": len(email),
        "tamanho_local": len(local),
        "tamanho_dominio": len(dominio),
        "tem_arroba": 1 if "@" in email else 0,
        "qtd_arroba": email.count("@"),
        "tem_ponto_dominio": 1 if "." in dominio else 0,
        "qtd_pontos": email.count("."),
        "tem_numero": 1 if any(char.isnumeric() for char in email) else 0,
        "dominio_gmail": 1 if dominio.startswith("gmail.") else 0,
        "dominio_com_br": 1 if dominio.endswith(".com.br") else 0,
        "dominio_br": 1 if dominio.endswith(".br") else 0,
        "dominio_bloqueado": 1 if dominio in DOMINIOS_BLOQUEADOS else 0,
        "local_vazio": 1 if local == "" else 0,
        "dominio_vazio": 1 if dominio == "" else 0,
    }


def preparar_dataframe(df):
    df = df.copy()

    df["email"] = df["email"].apply(normalizar_email)

    df = df.drop_duplicates(subset=["email"], keep="last")

    df["valido"] = df["email"].apply(validar_email)

    features_df = df["email"].apply(extrair_features_email).apply(pd.Series)

    df_final = pd.concat(
        [
            df[["email", "valido"]],
            features_df
        ],
        axis=1
    )

    df_final = df_final.dropna()

    return df_final
