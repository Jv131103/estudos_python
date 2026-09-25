# Imports
import pandas as pd
from apyori import apriori

# Ler o dataset
store_data = pd.read_csv("./IA/Sistemas_de_Recomendacao/store_data.csv", header=None)
print(store_data)

records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i, j]) for j in range(20) if str(store_data.values[i, j]) != "nan"])

print(records)

association_rules = apriori(
    records,
    min_support=0.0045,
    min_confidence=0.2,
    min_lift=3,
    min_lenght=2
)

association_rules = list(association_rules)

print(len(association_rules))

# Puxa a primeira regra
print(association_rules[0])

# Agora, imprimindo a lista de recomendações
for cesta in association_rules:
    itens = [x for x in cesta[0]]
    print("Produtos da cesta: " + str(itens))
    print("Suporte: " + str(cesta[1]))

    # Lista as regras desta cesta
    idRegra = 1
    for regra in cesta[2]:
        print(f"- Regra #{idRegra}: {regra[0]} -> {regra[1]}")
        print("   - Confiança: " + str(regra[2]))
        print("   - Lift: " + str(regra[3]))
        print(regra)
        idRegra += 1

    print("=" * 15)
