import time
from functools import wraps


# Decorators
def cronometrar(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()

        resultado = func(*args, **kwargs)

        fim = time.perf_counter()

        print(f"⏱ {func.__name__}: {fim - inicio:.4f}s")
        return resultado

    return wrapper


def repetir(n):
    def decorator(func):
        def executar(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return executar
    return decorator


def validar_positivo(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        for valor in args:
            if valor <= 0:
                raise ValueError("Todos os valores devem ser positivos")

        return func(*args, **kwargs)

    return decorator


# Generators
def fibonacci(limite):
    x = 1
    y = 1
    while y < limite:
        yield y
        x, y = y, x + y


def numeros_pares(inicio, fim):
    for n in range(inicio, fim + 1):
        if n % 2 == 0:
            yield n


def ler_em_chunks(arquivo, tamanho):
    chunk = []
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            chunk.append(linha.strip())
            if len(chunk) == tamanho:
                yield chunk  # entrega o pedaço
                chunk = []   # reseta
        if chunk:
            yield chunk      # entrega o que sobrou


@cronometrar
def processar(n):
    return sum(range(n))


@repetir(3)
def saudar(nome):
    print(f"Olá, {nome}!")


@validar_positivo
def calcular_area(largura, altura):
    return largura * altura


processar(1_000_000)
# ⏱ processar: 0.0312s

saudar("João")
# Olá, João!
# Olá, João!
# Olá, João!

try:
    calcular_area(5, -1)
    # ValueError: Argumentos devem ser positivos
except ValueError:
    pass

print(list(fibonacci(100)))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(list(numeros_pares(1, 20)))
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
