import time


def cronometrar(func):
    def decorator(*args, **kwargs):
        print(f"Executando '{func.__name__}'...")
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        print(f"Tempo: {fim - inicio:.3f}s")
        return resultado
    return decorator


@cronometrar
def calcular(n):
    return sum(range(n))


calcular(10_000_000)
# Executando 'calcular'...
# Tempo: 0.342s
