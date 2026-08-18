def validar_formulario(regras, **dados):
    for chave in dados:
        if chave not in regras:
            print(f"Aviso: chave desconhecida '{chave}' será ignorada.")

    erros = []
    valido = True
    for item in regras.keys():
        if item not in dados and regras[item]["obrigatorio"]:
            valido = False
            erros.append(f"{item} é obrigatório")
        elif item in dados and regras[item]["tipo"] is not type(dados[item]):
            valido = False
            erros.append(f"{item} deve ser do tipo {regras[item]['tipo'].__name__}")

    return {"valido": valido, "erros": erros}


regras = {
    "email": {"tipo": str, "obrigatorio": True},
    "idade": {"tipo": int, "obrigatorio": True},
    "newsletter": {"tipo": bool, "obrigatorio": False}
}

print(validar_formulario(regras, email="ana@teste.com", idade=25))
# {"valido": True, "erros": []}

print(validar_formulario(regras, idade="vinte"))
# {"valido": False, "erros": ["email é obrigatório", "idade deve ser do tipo int"]}
