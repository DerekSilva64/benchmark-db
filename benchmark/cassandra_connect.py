"""
Módulo para conexão ao Cassandra com suporte a Python 3.12.
Configura o event loop gevent antes de importar Cluster.
"""
import sys

# Configurar gevent monkey-patch ANTES de importar cassandra
try:
    from gevent import monkey
    monkey.patch_all()
except ImportError:
    pass

# Agora importar cassandra
from cassandra.cluster import Cluster, NoHostAvailable
import time


def connect_with_retry(cluster, keyspace=None, retries=10, delay=3):
    """Tenta conectar ao cluster Cassandra com retries."""
    for attempt in range(1, retries + 1):
        try:
            if keyspace:
                return cluster.connect(keyspace)
            return cluster.connect()
        except NoHostAvailable as e:
            print(f"Cassandra não disponível (tentativa {attempt}/{retries}): {e}")
            if attempt == retries:
                raise
            time.sleep(delay)


__all__ = ['Cluster', 'NoHostAvailable', 'connect_with_retry']
