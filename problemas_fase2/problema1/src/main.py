def reversao_slicing_manual(string: str) -> str:
    """
    Tempo: O(n²) (concatenação repetida de string: cada += copia o que já foi construído)
    Memória extra: O(n) (resultado final) — mas com muitas alocações intermediárias
    """
    inverso = ""

    for i in range(len(string) - 1, -1, -1):
        inverso += string[i]

    return inverso


def reversao_slicing_manual_pythonico(string: str) -> str:
    """
    Tempo: O(n) (cria a lista em O(n) + join em O(n))

    Memória extra: O(n) para a lista + O(n) para a string final ⇒ no total O(n) (mas com constante grande)
    """
    return "".join([string[i] for i in range(len(string) - 1, -1, -1)])


def reversao_manual_eficiente(s: str) -> str:
    """
    Tempo: O(n) (append O(1) amortizado, join O(n))

    Memória extra: O(n) (lista + string final) ⇒ O(n)
    """
    out = []
    for i in range(len(s) - 1, -1, -1):
        out.append(s[i])
    return "".join(out)


def reversao_tecnica_dois_ponteiros(string: str) -> str:
    """
    Tempo: O(n²) (mesmo motivo: += em string)

    Memória extra: O(n) (resultado) + alocações intermediárias
    """
    inverso = ""
    i = 0
    j = len(string) - 1

    meio = (j + i) // 2

    while i <= j:
        if j >= meio:
            inverso += string[j]
            j -= 1
        else:
            inverso += string[j - i]
            i += 1

    return inverso


def reversao_tecnica_dois_ponteiros_lista(string: str) -> str:
    """
    Tempo: O(n)

    Memória extra: O(n) (a lista + string final) ⇒ O(n)
    """
    lista = list(string)

    i, j = 0, len(lista) - 1

    while i < j:
        lista[i], lista[j] = lista[j], lista[i]   # swap de elementos
        i += 1
        j -= 1

    return "".join(lista)


def reversao_tecnica_slicing_pythonico(string: str) -> str:
    """
    Tempo: O(n)

    Memória extra: O(n) (nova string)
    """
    return string[::-1]


def reversao_tecnica_slicing_reverse(string: str) -> str:
    """
    Tempo: O(n)

    Memória extra: O(n) (nova string; o iterador é O(1))
    """
    return "".join(reversed(string))


def reversao_bytearray_ascii(s: str) -> str:
    """
    Tempo: O(n)

    Memória: O(n) (mas o reverse é in-place no bytearray)

    Atenção: isso não é geral para Unicode (emoji/acentos) se usar UTF-8, porque inverter bytes quebra caracteres multibyte.

    """
    b = bytearray(s, "ascii")   # O(n)
    b.reverse()                 # in-place, O(n)
    return b.decode("ascii")    # O(n)


# ESTRATÉGIA DIVIDE AND CONQUER
def _rev_dc_chunks(s: str, start: int, end: int, out: list[str]) -> None:
    """
    Tempo: Θ(n) (cada caractere é appended uma vez + join final)

    Memória extra: Θ(n) (lista de caracteres/chunks) + stack Θ(log n)
    """
    # adiciona chunks em ordem reversa
    length = end - start
    if length <= 1:
        if length == 1:
            out.append(s[start])
        return

    mid = start + length // 2
    # processa primeiro a metade direita, depois a esquerda
    _rev_dc_chunks(s, mid, end, out)
    _rev_dc_chunks(s, start, mid, out)


def reverse_divide_conquer_join(s: str) -> str:
    out: list[str] = []
    _rev_dc_chunks(s, 0, len(s), out)
    return "".join(out)
