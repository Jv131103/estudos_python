class ErrorOptionOutputDictionary(Exception):
    pass


def option(dictionary: dict, output: str = "keys"):
    match (output.lower()):
        case 'keys':
            final_output = dictionary.keys()
        case 'values':
            final_output = dictionary.values()
        case 'all':
            final_output = dictionary.items()
        case _:
            raise ErrorOptionOutputDictionary("OUTPUT INVÁLIDO PARA SAÍDA DE DICIONÁRIO")

    return final_output


def imprimir_dicionario(dictionary: dict, output: str = "keys"):
    final_output = option(dictionary, output)

    for items in final_output:
        if isinstance(items, tuple):
            key, value = items
            print(f"KEY: {key} | VALUE: {value}")
        else:
            print(items)


produto1 = {
    'nome': 'produto1',
    'tipo': 'categoriaA',
    'valor': '50.5',
    'fornecedor': 'ABCD',
}
imprimir_dicionario(produto1, "keys")
print()
imprimir_dicionario(produto1, "values")
print()
imprimir_dicionario(produto1, "all")
print()
imprimir_dicionario(produto1, "X")
