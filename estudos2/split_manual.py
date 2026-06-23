def split_manual(string):
    palavras = []
    palavra_atual = ""

    for char in string:
        if not char.isspace():
            palavra_atual += char  # Vai montando a palavra letra por letra
        else:
            if palavra_atual:  # Se a palavra não estiver vazia, terminou uma palavra!
                palavras.append(palavra_atual)
                palavra_atual = ""  # Reseta o acumulador

    # Não esqueça de adicionar a última palavra se a string não terminar em espaço
    if palavra_atual:
        palavras.append(palavra_atual)

    return palavras


print(split_manual("Python   é    bom"))  # Saída: ['Python', 'é', 'bom']
