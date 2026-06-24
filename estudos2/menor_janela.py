from collections import Counter


def menor_janela(texto, alvo):
    if not texto or not alvo:
        return ""

    preciso = Counter(alvo)      # {"A":1, "B":1, "C":1}
    necessario = len(preciso)       # 3 caracteres distintos necessários
    tenho = {}                 # frequência da janela atual
    formado = 0                  # quantos já foram satisfeitos

    esq = 0
    melhor = ""

    for dir in range(len(texto)):

        # 1) Entra o caractere da direita
        c = texto[dir]
        tenho[c] = tenho.get(c, 0) + 1

        # 2) Verifica se esse caractere satisfez uma necessidade
        if c in preciso and tenho[c] == preciso[c]:
            formado += 1

        # 3) Janela válida → tenta contrair pela esquerda
        while formado == necessario:
            janela_atual = texto[esq:dir + 1]
            if not melhor or len(janela_atual) < len(melhor):
                melhor = janela_atual

            # Remove o caractere da esquerda
            saindo = texto[esq]
            tenho[saindo] -= 1
            if saindo in preciso and tenho[saindo] < preciso[saindo]:
                formado -= 1
            esq += 1

    return melhor


print(menor_janela("ADOBECODEBANC", "ABC"))  # BANC
