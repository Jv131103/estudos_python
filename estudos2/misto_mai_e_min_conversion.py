texto = "Python 3.12"

resultado = ""
i = 0

while i < len(texto):
    c = texto[i]

    if 'a' <= c <= 'z':
        # De minúscula para maiúscula
        resultado += chr(ord(c) - 32)
    elif 'A' <= c <= 'Z':
        # De maiúscula para minúscula
        resultado += chr(ord(c) + 32)
    else:
        # Mantém números e símbolos intactos
        resultado += c

    i += 1

print(resultado)  # Saída: pYTHON 3.12
