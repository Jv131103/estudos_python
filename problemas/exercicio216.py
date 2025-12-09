def filtrar_vogais(lista):
    so_iniciais_vogais = []
    for texto in lista:
        texto = texto.lower()
        if texto[0] in ['a', 'e', 'i', 'o', 'u']:
            so_iniciais_vogais.append(texto)

    return so_iniciais_vogais


print(filtrar_vogais(["python", "sql", "algoritmo", "estrutura", "java", "oop"]))
