def soma_numeros_maiores_que_10(lista):
    print(lista)
    soma = 0
    for valor in lista:
        if valor > 10:
            soma += valor

    return soma


soma = soma_numeros_maiores_que_10(list(range(0, 21, 2)))
print(soma)
