def contar_palavras(texto):
    palavras = texto.split()
    contador = 0

    for _ in palavras:
        contador += 1

    return contador


def contar_elegante(texto):
    return len(texto.split())


print(contar_palavras("Python é uma linguagem poderosa"))
print(contar_elegante("Python é uma linguagem poderosa"))
