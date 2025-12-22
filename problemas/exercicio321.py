def total_com_desconto(*precos):
    total = sum(precos)

    if total >= 300:
        desconto = 0.15
    elif total >= 200:
        desconto = 0.10
    else:
        desconto = 0.05

    return total * (1 - desconto)


print(total_com_desconto(110, 90, 30))
