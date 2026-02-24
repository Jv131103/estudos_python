try:
    from .inverso import inverso
    from .tratar import trata_string
except ImportError:
    from inverso import inverso
    from tratar import trata_string


def is_palinder(text):
    if not isinstance(text, str):
        return False

    if not text:
        return False

    editado = trata_string(text)

    return inverso(editado) == editado


def is_palinder_tecnica_ponteiros(text):
    if not isinstance(text, str) or not text:
        return False

    s = trata_string(text)
    i, j = 0, len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


if __name__ == "__main__":
    print(is_palinder("Ame a ema"))
    print(is_palinder("OVO"))
    print(is_palinder("Ame o poema"))
    print(is_palinder("Socorram-me, subi no ônibus em Marrocos."))
