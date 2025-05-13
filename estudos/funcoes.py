"""
funcoes:

Funções são blocos de código reutilizáveis que realizam uma tarefa específica.
Elas ajudam a organizar, reutilizar e testar partes do programa de forma isolada.

EX:

    def nome_da_funcao(parâmetros):
        '''Comentário opcional explicando a função (docstring).'''
        # corpo da função
        return resultado

Parâmetros:

    Parâmetros são variáveis definidas entre os parênteses da função. Eles
    recebem valores quando a função é chamada.

    PS: Se houver eles, sempre o chamem

        - Podemos chamálas como por ex:

            def funcao(argumento):
                aplicacao com argumento

            funcao(argumento=valor)

        - Podemos não chamalas Também

            funcao(valor)

Boas práticas:

    1 - Nenhum parâmetro é melhor do que 1 parâmetro,
    Um parâmetro é melhor que deois parâmetros e assim vai

    2 - Quanto menor e menos trabalho a função fizer, melhor

    3 - Lambda é útil para expressões simples, mas para lógica mais complexa,
    prefira def.

"""


# ------------------------------------
# Funções comuns
# ------------------------------------

# Sem parâmetros
def diga_oi():
    print("Oi!")


# Com parâmetro
def diga_algo(mensagem):
    print(mensagem)


def exemplo(a, b):
    pass


# Posicionais
exemplo(1, 2)

# Nomeados
exemplo(a=1, b=2)


def saudacao(nome="Usuário"):
    print(f"Olá, {nome}!")  # Print exibe algo, mas não retorna valor


def soma(a, b):
    """Retorna a soma de dois valores."""
    return a + b  # Return retorna o resultado para uso externo


def maioridade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"


def aplicar_operacao(x, y, operacao):
    return operacao(x, y)  # função como parâmetro


# ------------------------------------
# pass, None, e funções sem return
# ------------------------------------
def nada():
    """Se a função não tiver return, ela retorna None por padrão."""
    pass  # Também podemos chamar ...


print(nada())  # None


# ------------------------------------
# Funções com *args e **kwargs

# *args: permite passar vários argumentos posicionais (empacotados como tupla).

# **kwargs: permite passar argumentos nomeados (empacotados como dicionário).

# ------------------------------------

def soma_todos(*args):
    return sum(args)


def exibir_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


# Também podemos desempacotar itens em funções
def acessos(usuario, senha, email):
    return {"usuario": usuario, 'senha': senha, 'email': email}


retorno_ssgbd = ("joao@joao", "123456", "email@acessar123.com")
acessos(*retorno_ssgbd)


# return múltiplo (vários valores)
def coordenadas():
    return 1, 2  # o Python retorna uma tupla implícita.


x, y = coordenadas()


# * e ** em definição de funções com ordem
def funcao(p1, p2='valor', *args, kw1, kw2='valor', **kwargs):
    """
    Ou seja:

        . parâmetros posicionais simples

        . parâmetros com valor padrão

        . *args

        . parâmetros nomeados obrigatórios

        . parâmetros nomeados com padrão

        . **kwargs
    """
    pass


# ------------------------------------
# Lambdas
# ------------------------------------

dobro = lambda x: x * 2
par = lambda x: x % 2 == 0
media = lambda *valores: sum(valores) / len(valores) if valores else 0


# ------------------------------------
# Funções retornando funções
# ------------------------------------

# Closures
def gerar_multiplicador(n):
    """
    Uma closure é uma função que "lembra" do ambiente onde foi criada, mesmo depois
    que esse ambiente saiu de escopo.
    """
    return lambda x: x * n


multiplica_por_3 = gerar_multiplicador(3)
print("5 x 3 =", multiplica_por_3(5))


# ------------------------------------
# Exemplo completo com tudo junto
# ------------------------------------

def resumo(nome, idade, *notas, **extras):
    saudacao(nome)
    print("Idade:", idade, "-", maioridade(idade))
    print("Notas:", notas)
    print("Média:", media(*notas))
    print("Extras:")
    exibir_dados(**extras)


resumo(
    "João", 18, 7.5, 8.0, 6.5,
    curso="ADS",
    ativo=True
)


# -----------------------------------
# Funções aninhadas

# Funções definidas dentro de outras:

# -----------------------------------
def externa(msg):
    def interna():
        print("Mensagem:", msg)
    interna()


# ------------------------------------
# Funções recursivas

# Função que chama a si mesma até atingir um caso base:

# ------------------------------------
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)


# ------------------------------------
# Escopo: global e nonlocal
# ------------------------------------
x = 5


def usar_global():
    global x
    x = 10  # altera o x global


def usar_nonlocal():
    x = 3

    def interna():
        nonlocal x 
        x += 1
        return x

    return interna()


def externa2():
    contador = 0

    def interna():
        nonlocal contador  # Serve para alterar variáveis da função envolvente, mas não globais
        contador += 1
        return contador
    return interna


# ------------------------------------
# Decoradores

# Funções que modificam o comportamento de outras funções:

# ------------------------------------
def decorador(func):
    def interna(*args, **kwargs):
        print("Antes")
        resultado = func(*args, **kwargs)
        print("Depois")
        return resultado
    return interna


@decorador
def mostrar():
    print("Função principal")


mostrar()


# ------------------------------------
# Funções geradoras com yield

# Eles economizam memória (lazy evaluation)
# Só percorrem uma vez
# São usados em pipelines, leitura de arquivos, streams etc.

# ------------------------------------
def contador(limit):
    n = 0
    while n < limit:
        yield n  # pausa e retorna
        n += 1


gen = contador(3)
print(next(gen))  # 0
print(next(gen))  # 1


# yield from
# Quando usar yield em funções que precisam delegar a outra função geradora:

def subgerador():
    yield 1
    yield 2


def gerador():
    yield 0
    yield from subgerador()
    yield 3



"""
Diferenças entre print, return e yield
| Comando  | O que faz                                 | Uso típico                       |
| -------- | ----------------------------------------- | -------------------------------- |
| `print`  | Exibe na tela, mas não retorna valor      | Debug, mensagens ao usuário      |
| `return` | Finaliza a função e retorna um valor      | Lógica de cálculo e reuso        |
| `yield`  | Pausa a função e retém o estado (gerador) | Grandes listas, fluxos contínuos |

"""


# ------------------------------------
# Funções como objetos de primeira classe

# Funções em Python são objetos, podem ser passadas como parâmetros,
# retornadas, atribuídas a variáveis etc.

# ------------------------------------
def dobrar(x):
    return x * 2


funcao = dobrar
print(funcao(4))  # 8


funcoes = [lambda x: x+1, lambda x: x*2, lambda x: x**2]
for f in funcoes:
    print(f(3))


# ------------------------------------
# Anotações de tipo (Type Hinting)

# Pode incluir um exemplo simples:

# ------------------------------------
def subtracao(a: int, b: int) -> int:
    return a - b

# ------------------------------------
# Função principal (boas práticas)
# ------------------------------------

def main():
    print("\n=== Testes com operações ===")
    print("Soma:", soma(3, 4))
    print("Soma total:", soma_todos(1, 2, 3, 4, 5))
    print("Aplicando operação (multiplicação):", aplicar_operacao(3, 5, lambda x, y: x * y))


if __name__ == "__main__":
    main()
