def eh_palindromo(s):
    if not s:
        return False

    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


palavras = [
    "arara",
    "batata",
    "radar",
    "plot",
    "aaaaa",
    "",
    "12321"
]

for palavra in palavras:
    print(f"{palavra} é palíndromo? {eh_palindromo(palavra)}")
