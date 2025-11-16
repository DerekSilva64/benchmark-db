import mysql.connector
import time
import random
from config import *

conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASS,
    database=MYSQL_DB
)

cursor = conn.cursor()

N = 100_000
inicio = time.time()

for _ in range(N):
    uid = random.randint(1, 1000)
    cursor.execute("SELECT latitude, longitude FROM eventos LIMIT 5", (uid,))
    cursor.fetchall()

fim = time.time()

print(f"MySQL - {N} leituras levaram {fim - inicio:.2f} segundos")
