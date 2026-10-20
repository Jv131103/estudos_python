import gtts as g

voz = g.gTTS("Olá, pessoal!", lang="pt")
voz.save("IA/audio/voz.mp3")

from IPython.display import Audio

Audio("IA/audio/voz.mp3")

# Exibindo a lista de línguas
print(g.lang.tts_langs())

arq = open("IA/audio/frases.txt", "r")
for linha in arq.readlines():
    lang, texto = linha.split(";")
    voz = g.gTTS(texto, lang=lang)
    voz.save(f"IA/audio/linha{lang}.mp3")
    print(Audio(f"IA/audio/linha{lang}.mp3"))
