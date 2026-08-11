numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
palavras = ["sol", "lua", "estrela", "céu", "universo"]

pares = [numero for numero in numeros if numero % 2 == 0]
quadrados = [numero**2 for numero in numeros]
mais_de_quatro_letras = [palavra for palavra in palavras if len(palavra) > 4]

print(f"Pares: {pares}")
print(f"Quadrados: {quadrados}")
print(f"Palavras com mais de 4 letras: {mais_de_quatro_letras}")
