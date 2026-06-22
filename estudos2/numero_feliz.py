def eh_feliz(numero):
    ja_foi = set()

    while True:
        soma = 0
        while numero > 0:
            digito = numero % 10
            soma += digito**2
            numero = numero // 10

        if soma == 1:
            return True
        elif soma in ja_foi:
            return False

        ja_foi.add(soma)
        numero = soma


print(eh_feliz(19))
print(eh_feliz(2))
print(eh_feliz(145))
