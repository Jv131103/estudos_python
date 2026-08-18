def raiz_digital(numero):
    if numero < 10:
        return numero  # caso base: já é 1 dígito só

    soma = numero % 10 + raiz_digital(numero // 10)

    if soma < 10:
        return soma
    return raiz_digital(soma)  # ainda tem mais de 1 dígito, chama de novo


print(raiz_digital(9875))
