def anagramas(string1, string2):
    # Normalizar: caixa baixa e remover espaços e pontuação
    def limpar(s):
        for p in ",.;!? ":
            s = s.replace(p, "")
        return s.lower()

    s1 = limpar(string1)
    s2 = limpar(string2)

    # atalhozinho: se depois de limpar o tamanho já for diferente, nem perde tempo
    if len(s1) != len(s2):
        return False

    conteudo = {}

    for ch in s1:
        conteudo[ch] = conteudo.get(ch, 0) + 1

    for ch in s2:
        conteudo[ch] = conteudo.get(ch, 0) - 1

    for valor in conteudo.values():
        if valor != 0:
            return False

    return True


print(anagramas("Roma", "Amor"))           # True
print(anagramas("Listen", "Silent"))       # True
print(anagramas("Python", "Typhon"))       # True
print(anagramas("Hello", "Olleh!"))        # True
print(anagramas("banana", "ananab"))       # True
print(anagramas("bate", "beta"))           # True
print(anagramas("teste", "teest"))         # True
print(anagramas("aaa", "aa"))              # False
