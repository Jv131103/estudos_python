texto = "hello world!"

resultado = ""
i = 0

while i < len(texto):
    caractere = texto[i]

    # Se está no intervalo minúsculo ('a' até 'z')
    if 'a' <= caractere <= 'z':
        # Converte para maiúscula subtraindo 32
        codigo_ascii = ord(caractere) - 32
        resultado += chr(codigo_ascii)
    else:
        # Se for espaço, pontuação ou já for maiúscula, mantém
        resultado += caractere

    i += 1

print(resultado)  # Saída: HELLO WORLD!
