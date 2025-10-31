# Tipo de dado que possui chave-valor, ou seja, para cada chave associa um
# valor correspondente

dict1 = {
    "chave1": "valor1",
    "chave2": "valor2"
}

print(dict1, type(dict1))

dados = {
    "nome": "XBOX",
    "valor": 2500,
    "estoque": 50,
    'categoria': "video games"
}

# Acessando itens por elementos, ou seja, chaves
print(dados['nome'])
print(dados["valor"])

dict2 = {
    "chave1": [1, 3, 5],
    "chave2": [2, 4, 6],
    "chave3": (7, 8, 9),
    "chave4": (13, 15, 17),
    "chave5": "Vou pegar algo específico"
}

# Para acessar com iteráveis, podemos fazer
print(dict2["chave1"][0])
print(dict2["chave3"][0])
print(dict2["chave5"][0])

# Podemos fatiar (slicing)
print(dict2["chave1"][1:])
print(dict2["chave3"][::-1])
print(dict2["chave5"][4:9])

# Mudando valores
dados["valor"] = 3000
print(dados)

# swap entre os valores de duas chaves
dados["nome"], dados["valor"] = dados["valor"], dados["nome"]
print(dados)

# swap em dicionários diferentes
a = {"x": 10}
b = {"y": 20}

a["x"], b["y"] = b["y"], a["x"]
print(a, b)

# Adicionando novos itens ao dicionário
dados["garantia"] = True
print(dados)

# Removendo um item (usando del)
# PS: Se não especificar, ele apagará literalmente tudo relacionado sobre o
# dicionário
del dados["estoque"]
print(dados)

# Removendo e retornando o valor (com pop)
# Aqui, é obrigatório especificar a chave que quer remover
categoria_removida = dados.pop("categoria")
print(dados)
print(categoria_removida)

# Pegando um valor sem erro caso a chave não exista (get)
print(dados.get("nome"))
print(dados.get("inexistente"))        # retorna None
print(dados.get("inexistente", "N/A"))  # retorna valor padrão

# Pegando só as chaves, só os valores ou tudo junto
print(dados.keys())     # retorna só as chaves
print(dados.values())   # retorna só os valores
print(dados.items())    # retorna pares (chave, valor)

# Criando um dicionário a partir de listas (zip)
chaves = ["a", "b", "c"]
valores = [1, 2, 3]

novo_dict = dict(zip(chaves, valores))
print(novo_dict)

# Mesclando dicionários (sem loop)
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d3 = d1 | d2     # Python 3.9+
print(d3)

# Copiando dicionário (importante para não alterar o original)
# Esta é uma cópia parcial, ou seja, não copia tudo que pode ter dentro do dict
copia = dados.copy()
print(copia)

# Convertendo um dicionário em lista (somente chaves / valores / pares)
lista_chaves = list(dados.keys())
lista_valores = list(dados.values())
lista_itens = list(dados.items())

print(lista_chaves)
print(lista_valores)
print(lista_itens)

# Criando dicionário com valor padrão (fromkeys)
d4 = dict.fromkeys(["id", "nome", "email"], None)
print(d4)

# Verificando se chave existe no dicionário (sem if ainda, só o booleano)
print("nome" in dados)      # True ou False
print("idade" in dados)

# update() — Mesclar ou modificar valores existentes
dados.update({"valor": 3500, "estoque": 80})
print(dados)
# Também funciona como merge parcial:
dados.update({"novo_item": "teste"})
print(dados)

# setdefault() — Pega valor se existir, senão cria a chave
x = dados.setdefault("fabricante", "Microsoft")
print(dados)
print(x)   # retorna o valor atribuído
# Se a chave já existe, não muda:
y = dados.setdefault("nome", "PlayStation")
print(dados)  # "nome" continua o mesmo
print(y)

# Dicionário dentro de dicionário (estrutura aninhada)
# Também podemos fazer listas de dicionários
produto = {
    "nome": "Notebook",
    "preço": 4500,
    "info": {
        "ram": "16GB",
        "ssd": "512GB",
        "processador": "i7"
    }
}

print(produto["info"]["ssd"])

# Também podemos fazer listas de dicionários
produtos = [
    {"nome": "Notebook"}, {"nome": "PC-DESKTOP"}
]

# Tuplas podem ser chaves (listas NÃO podem)
# Isso ocorre, por chaves em dicionários, devem ser imutáveis e não podem ser
# alterados.
d = {(1, 2): "ponto", (3, 4): "outro"}
print(d)

# Ordenando dicionários

# Por chave
ordenado_chaves = dict(sorted(dados.items()))
print(ordenado_chaves)

# Por valor
ordenado_valores = dict(sorted(dados.items(), key=lambda item: item[1]))
print(ordenado_valores)
