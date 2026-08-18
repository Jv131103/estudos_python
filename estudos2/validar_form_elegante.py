def validar_formulario(regras, **dados):
    avisos = [f"chave desconhecida '{chave}' será ignorada" for chave in dados if chave not in regras]

    erros = []
    for item in regras:
        if item not in dados and regras[item]["obrigatorio"]:
            erros.append(f"{item} é obrigatório")
        elif item in dados and type(dados[item]) is not regras[item]["tipo"]:
            erros.append(f"{item} deve ser do tipo {regras[item]['tipo'].__name__}")

    return {"valido": not erros, "erros": erros, "avisos": avisos}


regras = {
    "email": {"tipo": str, "obrigatorio": True},
    "idade": {"tipo": int, "obrigatorio": True},
    "newsletter": {"tipo": bool, "obrigatorio": False}
}

print(validar_formulario(regras, email="ana@teste.com", idade=25))

print(validar_formulario(regras, idade="vinte"))
