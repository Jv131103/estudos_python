# Varuiáveis constantes são variáveis que não podem sofrer alterações
# Ou seja, elas se mantém a mesma em todo código...
# DETALHE:
# Em Python, não existe variáveis constantes...
# Porém, existe uma convensão da comunidade:
# - São referenciadas com letras Maúsculas
# - E entende-se que não deve trocar o valor quando está assim
# Apesar de ser possível alterá-la:
#   CONSTANTE = valor  # Lê-se: variavel constante lê/recebe/atribui valor

# Quando usar constantes?

# Tipos Primitivos
# Conceito explicado no arquivo variaveis.py
OPCAO_PADRAO = 0
CONSTANTE_PI = 3.1415
CLIENTE_PRINCIPAL = "Janderson"

# VC PODE MUDAR O VALOR DA CONSTANTE, APESAR DE NÃO SER RECOMENDADO
CONSTANTE_PI = 3.14  # Não é uma boa prática

# Também podemos definir uma CONSTANTE por meio de entrada do usuário
# NÃO E MUITO INTERSSANTE, MAS PODE VIR A CALHAR
VALOR = input("DEFINA A SUA CONSTANTE: ")

# Também podemos representar com saída de dados:
print(VALOR)

NUMERO = input("NUMERO: ")
print("NUMERO:", NUMERO)
