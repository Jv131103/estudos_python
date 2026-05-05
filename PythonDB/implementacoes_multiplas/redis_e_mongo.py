from pymongo import MongoClient
import redis
import hashlib
from textblob import TextBlob
from deep_translator import GoogleTranslator
import os
from dotenv import load_dotenv

load_dotenv()

# ======================
# CONEXÕES
# ======================

# Mongo
acesso = os.getenv("ACESS_MONGO", "mongodb://localhost:27017")
mongo = MongoClient(acesso)
colecao = mongo["FIAP"]["comentarios"]

# Redis (já retorna string)
host = os.getenv("HOST", "localhost")
port = int(os.getenv("PORT", 6379))
db = int(os.getenv("DB", 0))
cache = redis.Redis(host=host, port=port, db=db, decode_responses=True)


# ======================
# FUNÇÃO
# ======================
def analise_sentimento(texto: str) -> str:
    chave = "sent:" + hashlib.sha256(texto.encode()).hexdigest()

    # CACHE
    if cache.exists(chave):
        print("⚡ veio do Redis")
        return cache.get(chave)

    # TRADUZIR (melhora MUITO o resultado)
    try:
        texto_en = GoogleTranslator(source="auto", target="en").translate(texto)
    except Exception:
        texto_en = texto

    # SENTIMENTO
    polaridade = TextBlob(texto_en).sentiment.polarity

    # AJUSTE FINO
    if polaridade > 0.1:
        rotulo = "positivo"
    elif polaridade < -0.1:
        rotulo = "negativo"
    else:
        rotulo = "neutro"

    # CACHE (1 hora)
    cache.setex(chave, 3600, rotulo)

    # SALVAR NO MONGO
    try:
        colecao.insert_one({
            "texto": texto,
            "texto_traduzido": texto_en,
            "polaridade": polaridade,
            "rotulo": rotulo
        })
    except Exception as e:
        print("Erro ao salvar no Mongo:", e)

    return rotulo


# ======================
# TESTE
# ======================
print(analise_sentimento("Gostei muito do atendimento"))
print(analise_sentimento("Péssimo serviço"))
print(analise_sentimento("Gostei muito do atendimento"))  # vem do cache
