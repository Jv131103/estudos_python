def verificar_saca(peso):
    if 50 <= peso <= 55:
        print("Está no peso ideal (venda normal)")
    elif 45 <= peso < 50:
        print("Abaixo do peso, mas até 10% menor (venda com desconto)")
    else:
        print("Fora do padrão (recolher para reensacamento)")


verificar_saca(27)
verificar_saca(39)
verificar_saca(49)
print()
verificar_saca(50)
verificar_saca(52)
verificar_saca(55)
print()
verificar_saca(56)
verificar_saca(65)
verificar_saca(100)
