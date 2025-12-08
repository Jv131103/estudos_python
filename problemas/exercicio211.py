def palindromo_recursivo(texto):
    texto = texto.replace(" ", "").lower()

    # Caso base: vazio ou 1 caractere → é palíndromo
    if len(texto) <= 1:
        return True

    # Se as extremidades forem diferentes → não é palíndromo
    if texto[0] != texto[-1]:
        return False

    # Chamada recursiva reduzindo a string
    return palindromo_recursivo(texto[1:-1])


print(palindromo_recursivo("arara"))
print(palindromo_recursivo("radar"))
print(palindromo_recursivo("python"))
