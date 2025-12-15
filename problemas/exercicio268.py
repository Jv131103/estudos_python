def retornar_usuario(nome, idade):
    return {"nome": nome, "idade": idade}


p1 = retornar_usuario("João", 22)
print(p1["idade"])
