def trata_caracteres_especiais(text):
    novo = ""

    for c in text:
        cod = ord(c)

        if (
            65 <= cod <= 90
            or 97 <= cod <= 122
            or 48 <= cod <= 57
        ):
            novo += c

    return novo


def trata_string(text):
    """
    Lembre disso:

        ord('a')  # 97
        ord('A')  # 65

    Existe uma diferença fixa entre elas.

        ord('a') - ord('A')  # quanto dá?

        R: 32

    Agora testa:

        chr(ord('A') + 32)
        chr(ord('a') - 32)

    """
    text = trata_caracteres_especiais(text)

    new = []

    for value in text:
        if 'A' <= value <= 'Z':
            value = chr(ord(value) + 32)

        new.append(value)

    return "".join(new)
