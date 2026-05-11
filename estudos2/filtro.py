import random
import string

tamanho_lista1 = random.randint(1, 26)

lista1 = []
lista2 = []
ja_foi = []

while len(lista1) < tamanho_lista1:
    nome = random.choice(string.ascii_uppercase)
    idade = random.randint(0, 100)

    if nome not in ja_foi:
        ja_foi.append(nome)

        d = {
            "nome": nome,
            "idade": idade
        }

        lista1.append(d)

        d2 = {
            "nome": nome,
            "idade": idade,
            "maior": idade >= 18
        }

        lista2.append(d2)


def modelo1(lista1, lista2):
    i = 0

    for valores in lista2:
        if lista1[i]["nome"] == valores["nome"]:
            lista1[i].update({"adicional": valores})

    return lista1


def modelo2(lista1, lista2):
    i = 0

    for valores in lista2:
        if lista1[i]["nome"] == valores["nome"]:
            lista1[i].update({"adicional": valores})
            break

    return lista1


def modelo3(lista1, lista2):
    i = 0
    j = 0

    while i < len(lista2):
        if lista1[j]["nome"] == lista2[i]["nome"]:
            lista1[j].update({"adicional": lista2[i]})
            del lista2[i]
            i += 1
        j += 1

    return lista1


def modelo_melhor(lista1, lista2):
    indice = {}

    for pessoa in lista2:
        indice[pessoa["nome"]] = pessoa

    for pessoa in lista1:
        nome = pessoa["nome"]

        if nome in indice:
            pessoa["adicional"] = indice[nome]

    return lista1


# modelo1 -> Tempo: O(m) | Espaço: O(1)
# novo = modelo1(lista1, lista2)
# print(novo)

# modelo2 -> Tempo: O(m) no pior caso | Espaço: O(1)
# novo = modelo2(lista1, lista2)
# print(novo)

# modelo3 -> Tempo: O(m²) no pior caso | Espaço: O(1)
# novo = modelo3(lista1, lista2)
# print(novo)

# modelo_melhor -> Tempo: O(n + m) | Espaço: O(m)
novo = modelo_melhor(lista1, lista2)
print(novo)
