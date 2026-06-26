def plus_k(digits, k):
    carry = k  # Agora o carry inicial é o próprio K

    for i in range(len(digits) - 1, -1, -1):
        soma = digits[i] + carry
        digits[i] = soma % 10   # O dígito que fica é sempre o resto por 10
        carry = soma // 10      # O carry que passa é a divisão inteira por 10

        # ATENÇÃO: Só podemos parar se o carry for 0 E não houver mais o que processar
        if carry == 0:
            break

    # Se sairmos do loop e o carry ainda for maior que 0 (ex: sobrou 12)
    # precisamos inserir o resto do carry no início da lista, dígito por dígito
    while carry > 0:
        digits.insert(0, carry % 10)
        carry = carry // 10

    return digits


print(plus_k([1, 2, 7], 5))
