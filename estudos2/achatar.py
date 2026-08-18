def achatar(d, prefixo=""):
    if not isinstance(d, dict):
        raise TypeError("O argumento precisa ser um dicionário")

    resultado = {}

    for chave, valor in d.items():
        nova_chave = chave if not prefixo else f"{prefixo}.{chave}"

        if isinstance(valor, dict):
            # valor é um dicionário aninhado -> achata ELE (não o "d" original,
            # não o "resultado" que estamos montando) usando nova_chave como
            # o novo prefixo, e junta o que voltar no nosso resultado
            resultado.update(achatar(valor, nova_chave))
        else:
            # caso base: não é dicionário, guarda direto
            resultado[nova_chave] = valor

    return resultado


dados = {
    "usuario": {
        "nome": "Ana",
        "endereco": {
            "cidade": "São Paulo",
            "coordenadas": {"lat": -23.5, "lon": -46.6}
        }
    },
    "ativo": True
}

print(achatar(dados))
