def por_extenso(numero):
    if numero < 0 or numero > 99:
        return "Fora do intervalo"

    unidades = [
        "zero",
        "um",
        "dois",
        "três",
        "quatro",
        "cinco",
        "seis",
        "sete",
        "oito",
        "nove",
        "dez",
        "onze",
        "doze",
        "treze",
        "quatorze",
        "quinze",
        "dezesseis",
        "dezessete",
        "dezoito",
        "dezenove"
    ]
    dezenas = [
        "",
        "",
        "vinte",
        "trinta",
        "quarenta",
        "cinquenta",
        "sessenta",
        "setenta",
        "oitenta",
        "noventa"
    ]

    if numero < 20:
        # pega direto da lista unidades
        return unidades[numero]
    elif numero % 10 == 0:
        # ex: 30, 40... só a dezena
        return dezenas[numero // 10]
    else:
        # ex: 47 → "quarenta" + " e " + "sete"
        unidade = numero % 10
        dezena = numero // 10

        return f"{dezenas[dezena]} e {unidades[unidade]}"


print(por_extenso(5))
print(por_extenso(15))
print(por_extenso(20))
print(por_extenso(30))
print(por_extenso(47))
print(por_extenso(99))
print(por_extenso(100))
print(por_extenso(-5))
