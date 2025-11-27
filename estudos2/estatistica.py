# importamos o módulo
import statistics

# definimos o vetor para o qual iremos obter as estatísticas descritivas
amostra = [10, 3, 9, 8, 10]
media = statistics.mean(amostra)  # cálculo da média aritmética
media_harm = statistics.harmonic_mean(amostra)  # cálculo da média harmônica
media_geo = statistics.geometric_mean(amostra)  # cálculo da média geométrica
variancia = statistics.variance(amostra)  # cálculo da variância
desvio_padrao = statistics.stdev(amostra)  # cálculo do desvio padrão
moda = statistics.median(amostra)  # cálculo da moda
mediana = statistics.mode(amostra)  # cálculo da mediana


print('Estatística Descritiva'.center(50, ' '))
print(f'\tMédia aritmética: {media:.2f}')
print(f'\tMédia harmônica: {media_harm:.2f}')
print(f'\tMédia geométrica: {media_geo:.2f}')
print(f'\tVariância: {variancia:.2f}')
print(f'\tDesvio padrão: {desvio_padrao:.2f}')
print(f'\tModa: {moda:.2f}')
print(f'\tMediana: {mediana:.2f}')
