def strip_manual(string):
    if not string:
        return ""

    esquerda = 0
    direita = len(string) - 1

    # Anda com o ponteiro da esquerda para a direita até achar uma letra
    while esquerda <= direita and string[esquerda].isspace():
        esquerda += 1

    # Anda com o ponteiro da direita para a esquerda até achar uma letra
    while direita >= esquerda and string[direita].isspace():
        direita -= 1

    # Retorna o recorte (slice) da string original
    return string[esquerda : direita + 1]


print(f"'{strip_manual('   Olá Mundo   ')}'")  # Saída: 'Olá Mundo'
