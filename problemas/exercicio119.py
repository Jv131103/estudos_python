import math

dict_base_log2 = {x: round(math.log2(x), 3) for x in range(2, 21, 2)}
print(dict_base_log2)

dicionario2 = {chr(64 + num): num for num in range(1, 21) if num % 5 == 0 or num % 3 == 0}
print(dicionario2)
