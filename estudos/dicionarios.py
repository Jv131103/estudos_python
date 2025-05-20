"""
📘 DICIONÁRIOS EM PYTHON

Um **dicionário** (`dict`) é uma estrutura de dados que armazena pares **chave: valor**.

- É mutável (você pode adicionar, modificar e remover elementos).
- As chaves devem ser **hashables** (imutáveis).
- Os valores podem ser de qualquer tipo.
- Extremamente eficientes para buscas, inserções e atualizações.

🔹 Sintaxe básica:
"""

# Criando um dicionário
d = {"nome": "João", "idade": 18}

# Acessando valores pela chave
print(d["nome"])     # João

# Adicionando novo item
d["cidade"] = "SP"

# Alterando valor existente
d["idade"] = 19

# Removendo item
del d["cidade"]

# Verificando se uma chave existe
if "nome" in d:
    print("Tem nome!")

"""
🔹 Funções e métodos importantes:
"""

# Criar dicionário vazio
d = dict()

# Obter valor com fallback padrão
print(d.get("chave", "valor padrão"))

# Iterar sobre chaves
for chave in d:
    print(chave, d[chave])

# Iterar sobre valores
for valor in d.values():
    print(valor)

# Iterar sobre pares (chave, valor)
for chave, valor in d.items():
    print(chave, valor)

# Remover item e retornar valor
idade = d.pop("idade", None)

# Limpar dicionário
d.clear()

# Copiar dicionário
copia = d.copy()

# setdefault: definir e acessar ao mesmo tempo
# Esse método busca uma chave e retorna seu valor. Se ela não existir, adiciona
# com um valor padrão.
d = {"a": 1}
d.setdefault("a", 0)    # Já existe, retorna 1
d.setdefault("b", 0)    # Não existe, define b = 0
print(d)                # {'a': 1, 'b': 0}

# update: atualizando vários pares ao mesmo tempo
d = {"a": 1}
d.update({"b": 2, "c": 3})
# Também funciona com argumentos nomeados:
d.update(d=4, e=5)

# fromkeys: criar dicionário com chaves fixas
# Cria um dicionário com as chaves de uma coleção e mesmo valor para todas.
# Cuidado se o valor for mutável, como listas: todas as chaves apontarão
# para o mesmo objeto.
chaves = ["a", "b", "c"]
d = dict.fromkeys(chaves, 0)
print(d)  # {'a': 0, 'b': 0, 'c': 0}


# Comparações entre dicionários:
# Dicionários podem ser comparados diretamente. Dois dicts são iguais se
# tiverem as mesmas chaves e os mesmos valores (ordem não importa):
a = {"x": 1, "y": 2}
b = {"y": 2, "x": 1}
print(a == b)  # True


"""
🔹 dict e **kwargs em funções

Dicionários podem ser passados como argumentos nomeados usando **.
"""


def apresentar(nome, idade):
    print(f"{nome} tem {idade} anos")


dados = {"nome": "João", "idade": 18}
apresentar(**dados)


"""
🔹 Dicionário por compreensão (comprehension):
"""

quadrados = {x: x**2 for x in range(5)}
# Resultado: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

"""
🔹 Dicionários aninhados:
"""

aluno = {
    "nome": "João",
    "notas": {
        "matemática": 9.5,
        "história": 8.0
    }
}

# Acessando nota de matemática
print(aluno["notas"]["matemática"])

"""
🔹 Observações importantes:

✔️ As chaves precisam ser objetos **hashables** (como `int`, `str`, `tuple`, `frozenset`, etc.)
❌ Tipos mutáveis como `list`, `dict` e `set` **não podem** ser usados como chave.
✔️ Dicionários são **não ordenados até o Python 3.6**. A partir do Python 3.7, mantêm a **ordem de inserção**.
✔️ Quando você usa a mesma chave duas vezes, o valor mais recente sobrescreve o anterior.
✔️ Dicionários são extremamente rápidos para busca por chave — muito mais que listas, por exemplo.
"""

# Exemplo de sobrescrita:
d = {"a": 1, "a": 2}
print(d)  # {'a': 2}

"""
🔹 Como criar dicionários de forma alternativa:
"""

# Usando construtor dict()
d = dict(nome="João", idade=20)

# A partir de listas de pares
dados = [("nome", "João"), ("idade", 20)]
d = dict(dados)

# Juntando duas listas com zip
chaves = ["nome", "idade"]
valores = ["João", 20]
d = dict(zip(chaves, valores))

# Dicionário invertido
d = {"a": 1, "b": 2}
invertido = {v: k for k, v in d.items()}

# Ordenando um dicionário
d = {"c": 3, "a": 1, "b": 2}
ordenado = dict(sorted(d.items()))
print(ordenado)  # {'a': 1, 'b': 2, 'c': 3}

ordenado_por_valor = dict(sorted(d.items(), key=lambda item: item[1]))
print(ordenado_por_valor)

"""
🔹 Dicionário como "switch case"
"""

# Não existe switch em Python, mas podemos simular com dicionário de funções:


def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


operacoes = {
    "soma": soma,
    "sub": sub
}

print(operacoes["soma"](5, 3))  # 8
