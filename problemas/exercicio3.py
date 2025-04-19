"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura de tinta
é de 1 litro para cada 3 metros quadrados de tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta
a serem compradas e o preço total.
"""

tamanho = float(input("Tamanho em metros quadrados da área a ser pintada: "))
litros_necessarios = tamanho / 3
latas = litros_necessarios / 18
preco_final = 80 * latas
print(f"Preco final do produto: R$ {preco_final:.2f}")
