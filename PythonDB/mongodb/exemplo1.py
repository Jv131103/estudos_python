from datetime import datetime, UTC
from pymongo import MongoClient

client = MongoClient("mongodb://admin:admin123@localhost:27017/?authSource=admin")

db = client["FIAP"]
docs = db["corpus_texto"]

docs.insert_many([
    {"texto": "amei a experiência!", "sentimento": "positivo", "origem": "app", "ts": datetime.now(UTC)},
    {"texto": "péssimo atendimento", "sentimento": "negativo", "ts": datetime.now(UTC)},
    {"texto": "atendeu o que eu precisava", "sentimento": "neutro", "canal": "web", "ts": datetime.now(UTC)},
])

pipeline = [{"$group": {"_id": "$sentimento", "qtd": {"$sum": 1}}}]
print(list(docs.aggregate(pipeline)))
