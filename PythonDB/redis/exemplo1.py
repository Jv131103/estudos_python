import hashlib
import os
from dotenv import load_dotenv
import redis
from textblob import TextBlob
from deep_translator import GoogleTranslator

load_dotenv()

host = os.getenv("HOST", "localhost")
port = int(os.getenv("PORT", 6379))
db = int(os.getenv("DB", 0))

r = redis.Redis(host=host, port=port, db=db, decode_responses=True)


def analisar_sentimento(texto_en: str) -> float:
    return TextBlob(texto_en).sentiment.polarity


def sentimento(texto: str, forcar_recalculo=False) -> str:
    chave = "sent:" + hashlib.sha256(texto.encode()).hexdigest()

    # opcional: ignorar cache
    if not forcar_recalculo and r.exists(chave):
        return r.get(chave)

    # tradução mais robusta
    try:
        texto_en = GoogleTranslator(source="pt", target="en").translate(texto)
    except Exception:
        texto_en = texto

    polaridade = analisar_sentimento(texto_en)

    # ajuste melhorado
    if polaridade >= 0.2:
        rotulo = "positivo"
    elif polaridade <= -0.2:
        rotulo = "negativo"
    else:
        rotulo = "neutro"

    r.setex(chave, 3600, rotulo)

    return rotulo


# =========================
# TESTE (FORÇANDO RECÁLCULO)
# =========================
r.flushdb()  # limpa cache para teste

print(sentimento("amei a experiência!", True))
print(sentimento("odiei completamente", True))
print(sentimento("Sei lá", True))
