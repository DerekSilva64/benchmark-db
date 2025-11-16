from cassandra_connect import Cluster, connect_with_retry
import time
import random
from config import *


cluster = Cluster(CASSANDRA_HOSTS)
session = connect_with_retry(cluster, CASSANDRA_KEYSPACE)

N = 100_000

inicio = time.time()

for _ in range(N):
    uid = random.randint(1, 1000)
    session.execute("SELECT latitude, longitude FROM eventos WHERE usuario_id = %s LIMIT 5", [uid])

fim = time.time()

print(f"Cassandra - {N} leituras levaram {fim - inicio:.2f} segundos")
