import time

from main import (ContadorDeCaracteres, contar_unicos_otimizado,
                  contar_unicos_simples)

texto = "a" * 100000 + "b" * 100000 + "c" * 100000

inicio = time.perf_counter()
contar_unicos_simples(texto)  # Tempo: O(n²) (porque in em lista é O(n)) | Espaço: O(n)
fim = time.perf_counter()
print("Simples:", fim - inicio)

inicio = time.perf_counter()
contar_unicos_otimizado(texto)  # Tempo: O(n) | Espaço: O(n)
fim = time.perf_counter()
print("Otimizado:", fim - inicio)

inicio = time.perf_counter()
contador_simples = ContadorDeCaracteres(texto)  # POO (Tempo: O(n²) | Espaço: O(n))
contador_simples.contar_simples()
fim = time.perf_counter()
print("Class Contador Simples:", fim - inicio)

inicio = time.perf_counter()
contador_simples = ContadorDeCaracteres(texto)  # POO (Tempo: O(n) | Espaço: O(n))
contador_simples.contar_otimizado()
fim = time.perf_counter()
print("Class Contador Otimizado:", fim - inicio)
