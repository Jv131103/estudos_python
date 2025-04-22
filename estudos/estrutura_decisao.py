# O if é uma estrutura de controle condicional. Ele serve para tomar decisões
# no programa, ou seja, executar blocos de código se uma condição for
# verdadeira.
# PS: Ele só avalia condições verdadeiras.
# O Python avalia uma expressão (condição) que retorna um valor booleano (True ou False).
#   Se for True, executa o bloco indentado.
#   Se for False, pula o bloco.

# Tradução:
# if ---> se
# elif (el(se)if) ---> senão se
# else ---> senão

# Normas de boas práticas: (Os 4 mandamentos de uma boa condicional)
#   Evite aninhamentos profundos demais
#   Use elif para clareza
#   Prefira ternário apenas em expressões simples
#   Use pattern matching para múltiplos valores (Python 3.10+)

# Estrutura simples
idade = 18

if idade >= 18:  # Repare na identação!
    print("Você é maior de idade")

# Estrutura composta
idade = 16

if idade >= 18:
    print("Maior de idade")
else:  # PS: Um else sempre precisará de um if, mas um if nunca de um else
    print("Menor de idade")

# Estrutura encadeada
nota = 75

if nota >= 90:
    print("A")
elif nota >= 80:  # Um elif sempre precisa de um if, mas nunca de si mesmo abaixo ou de um else
    print("B")
elif nota >= 70:
    print("C")
else:
    print("Reprovado")

# ifs aninhado:
# Regra de Ouro: Evite mais que 2 ou 3 níveis de indentação. Quando chegar nisso,
# pense em refatorar
idade = 20
tem_carteira = True

if idade >= 18:
    if tem_carteira:
        print("Pode dirigir")
    else:
        print("Precisa de carteira")
else:
    print("Menor de idade")

# Hadouken Indentation (O mal aninhamento do if):
# Nunca, jamais, faça isso em seus códigos
usuario = {   # Veja sobre dicionarios em dicionarios.py
    "ativo": True,
    "idade": 18,
    "tem_carteira": False
}
if usuario:
    if usuario["ativo"]:
        if usuario["idade"] >= 18:
            if usuario["tem_carteira"]:
                print("Pode dirigir")               # HADOUKEN!
            else:
                print("Não pode dirigir")
        else:
            print("Usuário menor de idade")
    else:
        print("Usuário inativo!")
else:
    print("Usuário não encontrado!")

# if em linha (ternário)
# Mais avançada, mas é possível de ser feita com python:
idade = 17
status = "maior" if idade >= 18 else "menor"
print(status)

# if com operadores lógicos:
# AND: ambas verdadeiras
if idade >= 18 and tem_carteira:
    print("Pode dirigir")

# OR: uma ou outra
if idade < 18 or not tem_carteira:
    print("Não pode dirigir")

# NOT: inverte o valor
if not tem_carteira:  # Muito útil em casos em que precisamos avaliar se existe ou não algo
    print("Sem carteira")

# Qualquer expressão pode ser usada no if. Ela será convertida para bool.
# Caso queira entender mais, vá em tipos_booleanos_e_operadores_de_comparacao.py
if "abc":  # True, string não vazia
    print("Sim")

if []:  # False, lista vazia
    print("Nunca vou ser exibido")

# if com comparações múltiplas
x = 5

if 1 < x < 10:
    print("x está entre 1 e 10")

# Equivalente:
if 1 < x and x < 10:
    print("x está entre 1 e 10")

# if com pattern matching(Python 3.10+)
# Semelhante ao switch case de outras linguagens de programlção, com ele,
# possível fazer comparações de opção com melhor legibilidade:
match status:
    case "ativo":
        print("Usuário ativo")
    case "inativo":
        print("Usuário inativo")
    case _:
        print("Desconhecido")

# if criativo com lambda ou listas:
# veja mais sobre lambdas em lambdas.py e listas em listas.py:
# usando lambda

# usando lista de funções
funcoes = [lambda: print("Zero"), lambda: print("Um")]
valor = 1
funcoes[valor]()

# Casos curiosos e pegadinhas:
# is vs ==:
x = 1000
y = 1000
print(x == y)  # True
print(x is y)  # False (objetos diferentes em memória)

# Curiosidade:
if True:
    print("Executa")


condicao = True
# NÃO FAÇA ISSO:
if condicao == True:
    print("Executa")

# Nem isso:
if condicao == False:
    print("Não executa")


# parêntesis são opcionais, não são obrigados.
# Entretanto para expressões grandes, ele pode vir bem acalhar

# Perfeitamente válido e comum:
if x > 10 and y < 5:
    print("ok")

# Também válido, se quiser deixar mais claro:
# Os parênteses ajudam na legibilidade, principalmente em expressões
# longas ou com not, and, or misturados.
if (x > 10 and y < 5):
    print("ok")

# Mini if (if de uma linha)
# Não é bem recomendado usá-lo
if True: print("Executa")
