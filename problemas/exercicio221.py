def somar_numeros(texto):
    soma = 0
    caracteres = texto.split()
    for caracter in caracteres:
        uniao = ""
        if caracter.isdigit():
            soma += int(caracter)
        else:
            for char in caracter:
                if char.isdigit():
                    uniao += char

            if uniao.isdigit():
                soma += int(uniao)

    return soma


print(somar_numeros("O produto X custa 120 reais, mas com 30% de desconto fica 84."))
