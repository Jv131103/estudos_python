"""
Um objeto é hashable se:

    - Tem um valor de hash imutável (produzido pela função hash(obj)).

    - Pode ser usado como chave em dicionários ou elemento de um set.

    - Seu valor de hash não muda durante sua existência (portanto, ele deve ser imutável).

Hashbles:

| Tipo        | Hashable? | Por quê?                                    |
| ----------- | --------- | ------------------------------------------- |
| `int`       | ✅        | Imutável                                    |
| `float`     | ✅        | Imutável                                    |
| `str`       | ✅        | Imutável                                    |
| `tuple`     | ✅        | **Se todos os itens também forem hashable** |
| `frozenset` | ✅        | Versão imutável do set                      |


Não Hashbles:
| Tipo   | Hashable? | Por quê? |
| ------ | --------- | -------- |
| `list` | ❌        | Mutável  |
| `dict` | ❌        | Mutável  |
| `set`  | ❌        | Mutável  |

"""

# Como verificar se algo é hashable?
from collections.abc import Hashable

print(isinstance(42, Hashable))           # True
print(isinstance((1, 2), Hashable))       # True
print(isinstance([1, 2], Hashable))       # False
print(isinstance({1, 2}, Hashable))       # False


# Tuplas só são hashables se seus elementos também forem hashables.
hash((1, 2, "oi"))  # Ok
hash((1, [2, 3]))   # TypeError: unhashable type: 'list'

# O valor de hash() é usado internamente por dicionários e sets para organizar
# e buscar valores com extrema eficiência.
print(hash("banana"))  # Exemplo de hash numérico (varia por execução)
print(hash(123))
