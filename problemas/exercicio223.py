def palavra_mais_longa(texto):
    for p in ",.!?;:":
        texto = texto.replace(p, "")

    valores = texto.split()
    maior = 0
    indice_maior = 0

    for idx, valor in enumerate(valores):
        tam = len(valor)
        if tam > maior:
            indice_maior = idx
            maior = tam

    return valores[indice_maior]


texto = "Python é uma linguagem poderosa, moderna e extremamente flexível!"
print(palavra_mais_longa(texto))
