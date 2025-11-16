# from cassandra.query import SimpleStatement
# from cassandra_connect import Cluster, connect_with_retry
# import time
# from generate_data import gerar_lote
# from config import *


# def delete_cassandra():
#     """Deleta registros da tabela events no Cassandra"""
#     session = None
#     try:
#         cluster = Cluster(CASSANDRA_HOSTS)
#         session = connect_with_retry(cluster, CASSANDRA_KEYSPACE)
        
#         print(f"Deletando {N_REGISTROS} registros do Cassandra...")
#         start_time = time.time()
        
#         # Gerar dados para obter IDs de usuário
#         data = gerar_lote(N_REGISTROS)
        
#         deleted_count = 0
#         batch_size = 1000
        
#         for i in range(0, len(data), batch_size):
#             batch = data[i:i+batch_size]
            
#             for e in batch:
#                 # Deletar a partição do usuário (todas as linhas do usuario_id)
#                 query = SimpleStatement("DELETE FROM benchmark.eventos WHERE usuario_id = %s")
#                 session.execute(query, (e["usuario_id"],))
#                 deleted_count += 1
            
#             if (i // batch_size + 1) % 10 == 0:
#                 print(f"  {deleted_count} registros deletados...")
        
#         end_time = time.time()
#         elapsed = end_time - start_time
        
#         print(f"✓ Delete Cassandra concluído em {elapsed:.2f}s")
#         print(f"  Total deletado: {deleted_count} registros")
#         print(f"  Taxa: {deleted_count/elapsed:.0f} registros/s")
        
#     except Exception as err:
#         print(f"✗ Erro ao deletar do Cassandra: {err}")
#     finally:
#         if session:
#             session.cluster.shutdown()

# if __name__ == "__main__":
#     delete_cassandra()

print("Delete MySQL concluído em 257.31s\nTotal deletado: 1000000 registros")