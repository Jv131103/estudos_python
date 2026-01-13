"""
Crie variáveis para:

    Preço de um produto

    Quantidade comprada

    Calcule o total a pagar

Depois:

    Aumente a quantidade

    Recalcule o total

Observe como o valor da variável muda.
"""
preco = float(input("Preco do produto: "))
qtd = int(input("Quantidade comprada: "))
total = preco * qtd
print(f"Total atual: R$ {total:.2f}")

nova_qtd = int(input("Nova quantidade: "))
total = preco * nova_qtd
print(f"Total atual: R$ {total:.2f}")
