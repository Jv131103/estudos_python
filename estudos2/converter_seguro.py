def converter_seguro(valor, tipo_alvo):
    try:
        return tipo_alvo(valor)
    except (ValueError, TypeError):
        print(f"Não foi possível converter {valor!r} para {tipo_alvo.__name__}")
        return None


print(converter_seguro("42", int))
print(converter_seguro("abc", int))
print(converter_seguro("3.14", float))
print(converter_seguro(None, int))
print(converter_seguro("3.14", int))
