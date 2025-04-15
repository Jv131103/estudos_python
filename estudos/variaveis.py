# Variáveis são nomes que damos para referenciar valores na memória do
# computador. É como se fossem caixinhas com etiquetas: cada etiqueta tem um
# nome, e dentro dela você pode guardar um valor.

# variavel = valor  # Lê-se: variavel lê/recebe/atribui valor

# Ou seja, eles são endereços e registros que são armazenados na memória do
# nosso computador


# Tipos primitivos são os tipos mais básicos da linguagem.
# Eles armazenam valores simples, como números, texto e booleanos.
# Também são conhecidos como **tipos imutáveis**, ou seja:
# uma vez criado o valor, ele não pode ser alterado — qualquer mudança gera um
# novo valor.
numero = 1  # Inteiro: int() ---> números inteiros, positivos ou negativos
string = "ola"  # String: str() ---> textos, qualquer sequência de caracteres
numero2 = 2.98  # Decimal ou ponto flutuante: float() --> números decimais ou de ponto flutuante
booleano = True  # Booleano: bool() ---> valores lógicos True ou False

# Variáveis podem mudar conforme o tempo ...
x = "x"
x = "y"
x = 2   # O tipo não muda mas a refência do tipo da variável pode mudar

# Aqui realizamos o que chamamos de Swap de variáveis com variável temporária
numero1 = 2
numero2 = 1

numero_troca = numero2      # 1
numero2 = numero1           # 2
numero1 = numero_troca      # 1

# Também pode com o python realizar um swap mais moderno e belo
x = 3
y = 2
z = 1

x, y, z = z, y, x   # x = 2, y = 2, z = 3

# Variáveis podem recber inputs de entrada
nome = input("Digite seu nome: ")  # Por padrão a saída será em formato STRING

# Nomeação de variáveis (identificadores)
# Devem começar com letra ou underscore (_), não podem começar com número.
# Podem conter números, letras e underscores.
# Sensível a maiúsculas e minúsculas:
nome = "João"
Nome = "Maria"
# são variáveis diferentes

# IMPORTANTE:
# Palavras reservadas (não podem ser nomes de variáveis)
# if = 10  # ❌ Erro!

# Atribuição múltipla
a, b = 10, 20  # a = 10, b = 20

# Atribuição em cadeia
a = b = c = 0  # todas valem 0

# Variáveis são referências...
x = 10
y = x  # Você está copiando o valor

# type() para ver o tipo de uma variável
idade = 18
print(type(idade))  # <class 'int'>. Perceba que podemos reerneciar saídas

# Saída com variaveis
x = 10
print(x)

x, y = 1, 23
print("X:", x)
print("y:", y)
