arquivo = "./arquivos/dados.txt"

print("Carregando arquivo...")

vet = []

with open(arquivo, "r") as arq:
    for linha in arq:
        # print(linha)
        vet.append(float(linha))  # Acrescenta um novo elemento ao final do vetor

print(f"Vetor carregado com {len(vet)} valores")


# Mais eficiente que manualmente
media = sum(vet) / len(vet)

# soma dos quadrados dos desvios
soma = 0
for x in vet:
    soma += (x - media) ** 2

# variância
variancia = soma / len(vet)

# desvio_padrao
desvio_padrao = variancia**(1 / 2)  # Equivalente a sqrt

print(f"Média: {media}")
print(f"Desvio Padrão: {desvio_padrao}")

lim_1_inf = media - desvio_padrao
lim_1_sup = media + desvio_padrao

lim_2_inf = media - 2 * desvio_padrao
lim_2_sup = media + 2 * desvio_padrao

perto = 0          # caso 1
longe = 0          # caso 2

for x in vet:
    # Caso 1: dentro de 1 DP
    if lim_1_inf <= x <= lim_1_sup:
        perto += 1

    # Caso 2: entre 1 e 2 DP (duas faixas)
    elif (lim_2_inf <= x < lim_1_inf) or (lim_1_sup < x <= lim_2_sup):
        longe += 1

print(f"1) Até 1 DP da média: {perto} valores")
print(f"2) Entre 1 e 2 DP da média: {longe} valores")
