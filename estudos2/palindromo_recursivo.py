import unicodedata


def eh_palindromo(texto):
    texto = unicodedata.normalize('NFKD', texto.lower())
    texto = "".join(c for c in texto if c.isalnum() and not unicodedata.combining(c))

    if len(texto) <= 1:
        return True

    if texto[0] != texto[-1]:
        return False

    return eh_palindromo(texto[1:-1])


print(eh_palindromo("arara"))
print(eh_palindromo("radar"))
print(eh_palindromo("python"))
print(eh_palindromo("Ana"))
print(eh_palindromo("A base do teto"))
print(eh_palindromo("Socorram-me, subi no ônibus em Marrocos"))
