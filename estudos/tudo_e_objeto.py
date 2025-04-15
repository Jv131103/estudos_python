# tudo_e_objeto.py

# Em Python, TUDO é um objeto.
# Isso significa que tudo tem:
# - um tipo (class)
# - atributos e métodos
# - e é derivado de 'object', a superclasse base de tudo

# -----------------------------------------------
# Vamos ver isso em ação com tipos simples:
# -----------------------------------------------

numero = 10
print(type(numero))           # <class 'int'>
print(dir(numero))            # Mostra todos os métodos e atributos do objeto 'int'
print(numero.bit_length())    # Exemplo de método de int → retorna quantos bits são necessários para representar o número

texto = "Olá mundo"
print(type(texto))            # <class 'str'>
print(dir(texto))             # Métodos disponíveis para string
print(texto.upper())          # Transforma em maiúsculas

flutuante = 3.14
print(type(flutuante))         # <class 'float'>
print(flutuante.is_integer())  # Verifica se é um float inteiro (sem parte decimal)


# -----------------------------------------------
# Funções também são objetos!
# -----------------------------------------------

def saudacao(nome):
    return f"Olá, {nome}!"


print(type(saudacao))         # <class 'function'>
print(saudacao.__name__)      # Nome da função
print(saudacao.__doc__)       # Documentação da função (None aqui)

# Podemos até atribuir a função a outra variável:
nova = saudacao
print(nova("João"))           # Funciona igual!


# -----------------------------------------------
# Classes são objetos que criam objetos!
# -----------------------------------------------

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return f"{self.nome} está falando."


p = Pessoa("João")
print(p.falar())              # João está falando
print(isinstance(p, object))  # True → porque tudo é objeto

# A própria classe também é um objeto:
print(type(Pessoa))           # <class 'type'>
print(isinstance(Pessoa, object))  # True também!

# -----------------------------------------------
# Até tipos são objetos do tipo 'type'
# -----------------------------------------------

print(type(int))              # <class 'type'>
print(type(str))              # <class 'type'>
print(type(type))             # mindblow: <class 'type'>

# -----------------------------------------------
# Tudo herda de 'object'
# -----------------------------------------------

print(isinstance(10, object))       # True
print(isinstance("texto", object))  # True
print(isinstance(Pessoa, object))   # True

# -----------------------------------------------
# Podemos verificar atributos comuns de todos os objetos
# -----------------------------------------------

print(object.__doc__)  # Documentação da classe base
print(hasattr(numero, '__class__'))  # True → todo objeto sabe sua classe
