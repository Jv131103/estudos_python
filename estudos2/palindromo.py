def eh_palindromo1(palavra):
    contrario = []

    for i in range(len(palavra) - 1, -1, -1):
        contrario.append(palavra[i])

    return "".join(contrario) == palavra


def eh_palindromo2(palavra):
    i = 0
    j = len(palavra) - 1

    while i <= j:
        if palavra[i] != palavra[j]:
            return False

        i += 1
        j -= 1

    return True


def eh_palindromo3(palavra):
    pilha = []

    for letra in palavra:
        pilha.append(letra)

    dados = []
    while pilha:
        dados.append(pilha.pop())

    inverso = "".join(dados)

    return inverso == palavra


def eh_palindromo4(palavra):
    return palavra[::-1] == palavra


print(eh_palindromo1("arara"))
print(eh_palindromo2("arara"))
print(eh_palindromo3("arara"))
print(eh_palindromo4("arara"))
print()

print(eh_palindromo1("radar"))
print(eh_palindromo2("radar"))
print(eh_palindromo3("radar"))
print(eh_palindromo4("radar"))
print()

print(eh_palindromo1("python"))
print(eh_palindromo2("python"))
print(eh_palindromo3("python"))
print(eh_palindromo4("python"))
print()

print(eh_palindromo1("abba"))
print(eh_palindromo2("abba"))
print(eh_palindromo3("abba"))
print(eh_palindromo4("abba"))
print()

print(eh_palindromo1("abca"))
print(eh_palindromo2("abca"))
print(eh_palindromo3("abca"))
print(eh_palindromo4("abca"))
print()

print(eh_palindromo1("a"))
print(eh_palindromo2("a"))
print(eh_palindromo3("a"))
print(eh_palindromo4("a"))
print()

print(eh_palindromo1(""))
print(eh_palindromo2(""))
print(eh_palindromo3(""))
print(eh_palindromo4(""))
print()

print(eh_palindromo1("abcba"))
print(eh_palindromo2("abcba"))
print(eh_palindromo3("abcba"))
print(eh_palindromo4("abcba"))
