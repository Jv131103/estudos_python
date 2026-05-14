import pandas as pd

df = pd.read_csv("./IA/email/emails.csv")

df.loc[df["email"].str.lower().str.strip() == "teste@teste.com", "valido"] = 0

df.to_csv("./IA/email/emails.csv", index=False)

print("Corrigido!")
