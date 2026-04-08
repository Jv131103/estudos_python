import re


def limpar(text):
    text = text.lower()
    return re.sub(r'[^a-z0-9]', '', text)  # remove tudo que não é letra/número


def is_palinder1(text):
    text = limpar(text.lower().strip())

    inverso = text[::-1]

    return text == inverso


def is_palinder2(text):
    text = limpar(text.lower().strip())
    dados = []
    for i in range(len(text)-1, -1, -1):
        dados.append(text[i])

    inverso = "".join(dados)

    return text == inverso


def is_palinder3(text):
    text = limpar(text.lower().strip())
    dados = []
    i = 0
    j = len(text) - 1
    while i < len(text):
        dados.append(text[j])
        i += 1
        j -= 1
    inverso = "".join(dados)
    return text == inverso


def is_palinder4(text):
    text = limpar(text.lower().strip())

    pilha = []
    for valor in text:
        pilha.append(valor)

    dados = []
    while pilha:
        dados.append(pilha.pop())

    inverso = "".join(dados)

    return text == inverso


lista = ["arara", 'Ana', "racecar", "python", "A man a plan a canal Panama"]
funcoes = [
    is_palinder1,
    is_palinder2,
    is_palinder3,
    is_palinder4
]

for funcao in funcoes:
    print(f"Função: {funcao.__name__}")
    for dados in lista:
        print(f"\t{dados} = {funcao(dados)}")
    print()
