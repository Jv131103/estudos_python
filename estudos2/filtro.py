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
    for itens in lista1:
        for valores in lista2:
            if itens["nome"] == valores["nome"]:
                itens.update({"adicional": valores})

    return lista1


def modelo2(lista1, lista2):
    for itens in lista1:
        for valores in lista2:
            if itens["nome"] == valores["nome"]:
                itens.update({"adicional": valores})
                break

    return lista1


def modelo3(lista1, lista2):
    usados = set()  # índice dos já matched em lista2
    for pessoa1 in lista1:
        for j, pessoa2 in enumerate(lista2):
            if j not in usados and pessoa1["nome"] == pessoa2["nome"]:
                pessoa1["adicional"] = pessoa2
                usados.add(j)
                break
    return lista1


def modelo4(lista1, lista2):
    i = 0
    j = 0

    while i < len(lista1):
        if lista1[i]["nome"] == lista2[j]["nome"]:
            lista1[i].update({"detalhes": lista2[j]})
            i += 1
            j = 0
        else:
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



novo = modelo4(lista1, lista2)
print(novo)
