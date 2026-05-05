from cassandra.cluster import Cluster
from datetime import datetime, timedelta, UTC
import pandas as pd

# conexão
cluster = Cluster(["127.0.0.1"])
session = cluster.connect()

# garantir keyspace
session.execute("""
CREATE KEYSPACE IF NOT EXISTS iot
WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}
""")

session.set_keyspace("iot")

# garantir tabela
session.execute("""
CREATE TABLE IF NOT EXISTS medidas (
  device_id text,
  ts timestamp,
  temperatura double,
  vibracao double,
  PRIMARY KEY ((device_id), ts)
) WITH CLUSTERING ORDER BY (ts DESC)
""")

# inserir dados (com timezone correto)
now = datetime.now(UTC)

for i in range(10):
    session.execute(
        """
        INSERT INTO medidas (device_id, ts, temperatura, vibracao)
        VALUES (%s, %s, %s, %s)
        """,
        ("motor-42", now - timedelta(minutes=i), 65.0 + i * 0.2, 0.03 + (i % 3) * 0.01)
    )

# consulta correta
rows = session.execute(
    """
    SELECT ts, temperatura, vibracao
    FROM medidas
    WHERE device_id=%s AND ts >= %s
    """,
    ("motor-42", now - timedelta(hours=1))
)

# conversão correta para pandas
df = pd.DataFrame(list(rows))

print(df.head())
