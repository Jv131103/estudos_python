class ConfigInvalidaError(Exception):
    pass


def criar_config(**kwargs):
    chaves_validas = {"nome", "porta", "debug", "timeout"}
    for chave in kwargs:
        if chave not in chaves_validas:
            print(f"Aviso: chave desconhecida '{chave}' será ignorada.")

    nome = kwargs.get("nome")
    if not isinstance(nome, str) or not nome.strip():
        raise ConfigInvalidaError("nome é obrigatório e deve ser uma string não vazia")

    porta = kwargs.get("porta", 8080)
    if not isinstance(porta, int) or not (1 <= porta <= 65535):
        raise ConfigInvalidaError("porta deve estar entre 1 e 65535")

    debug = kwargs.get("debug", False)
    if not isinstance(debug, bool):
        raise ConfigInvalidaError("debug deve ser um valor booleano")

    timeout = kwargs.get("timeout", 30)
    if not isinstance(timeout, (int, float)) or timeout <= 0:
        raise ConfigInvalidaError("timeout deve ser positivo")

    return {"nome": nome, "porta": porta, "debug": debug, "timeout": timeout}


print(criar_config(nome="MeuApp", porta=3000))
print(criar_config(nome="MeuApp", porta=99999))
print(criar_config(porta=3000))
