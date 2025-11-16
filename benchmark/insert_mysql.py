import mysql.connector
import time
from generate_data import gerar_lote
from config import *

conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASS,
    database=MYSQL_DB
)

cursor = conn.cursor()

eventos = gerar_lote(N_REGISTROS)

sql = """
INSERT INTO eventos (
    usuario_id, acao, categoria, subcategoria,
    ts, payload,
    ip, device, sistema_operacional, navegador,
    latitude, longitude,
    valor1, valor2, valor3, valor4, valor5,
    score1, score2, score3,
    flag_ativo, observacoes
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

inicio = time.time()

for e in eventos:
    cursor.execute(sql, (
        e["usuario_id"], e["acao"], e.get("categoria", ""), e.get("subcategoria", ""),
        e["ts"], e["payload"],
        e.get("ip", ""), e.get("device", ""), e.get("sistema_operacional", ""), e.get("navegador", ""),
        e.get("latitude", 0.0), e.get("longitude", 0.0),
        e.get("valor1", 0), e.get("valor2", 0), e.get("valor3", 0), e.get("valor4", 0), e.get("valor5", 0),
        e.get("score1", 0.0), e.get("score2", 0.0), e.get("score3", 0.0),
        e.get("flag_ativo", False), e.get("observacoes", "")
    ))

conn.commit()

fim = time.time()

print(f"MySQL - Inserção de {N_REGISTROS} registros levou {fim - inicio:.2f} segundos")
