from cassandra_connect import Cluster, connect_with_retry
import time
import uuid
from generate_data import gerar_lote
from config import *
from datetime import datetime


cluster = Cluster(CASSANDRA_HOSTS)
session = connect_with_retry(cluster, CASSANDRA_KEYSPACE)

eventos = gerar_lote(N_REGISTROS)

query = session.prepare("""
INSERT INTO eventos (
    usuario_id, id, acao, categoria, subcategoria,
    ts, payload,
    ip, device, sistema_operacional, navegador,
    latitude, longitude,
    valor1, valor2, valor3, valor4, valor5,
    score1, score2, score3,
    flag_ativo, observacoes
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""")


inicio = time.time()

for e in eventos:
    # Converter timestamp para datetime se for string
    ts = e["ts"]
    if isinstance(ts, str):
        ts = datetime.fromisoformat(ts)
    
    session.execute(query, (
        e["usuario_id"],
        uuid.uuid1(),
        e["acao"],
        e.get("categoria", ""),
        e.get("subcategoria", ""),
        ts,
        e["payload"],
        e.get("ip", ""),
        e.get("device", ""),
        e.get("sistema_operacional", ""),
        e.get("navegador", ""),
        e.get("latitude", 0.0),
        e.get("longitude", 0.0),
        e.get("valor1", 0),
        e.get("valor2", 0),
        e.get("valor3", 0),
        e.get("valor4", 0),
        e.get("valor5", 0),
        e.get("score1", 0.0),
        e.get("score2", 0.0),
        e.get("score3", 0.0),
        e.get("flag_ativo", False),
        e.get("observacoes", "")
    ))

fim = time.time()

print(f"Cassandra - Inserção de {N_REGISTROS} registros levou {fim - inicio:.2f} segundos")
