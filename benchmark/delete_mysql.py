import mysql.connector
from mysql.connector import Error
import time
from generate_data import gerar_lote
from config import *

def delete_mysql():
    """Deleta registros da tabela events no MySQL"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASS,
            database=MYSQL_DB,
        )
        cursor = connection.cursor()

        print(f"Deletando {N_REGISTROS} registros do MySQL...")
        start_time = time.time()

        # Gerar dados para obter IDs de usuário
        data = gerar_lote(N_REGISTROS)
        
        # Deletar por usuario_id (estratégia: deletar em lotes)
        deleted_count = 0
        batch_size = 1000
        
        for i in range(0, len(data), batch_size):
            batch = data[i:i+batch_size]
            user_ids = [e["usuario_id"] for e in batch]
            
            # Criar placeholders para IN clause
            placeholders = ",".join(["%s"] * len(user_ids))
            sql = f"DELETE FROM eventos WHERE usuario_id IN ({placeholders})"
            
            cursor.execute(sql, user_ids)
            deleted_count += cursor.rowcount
            
            if (i // batch_size + 1) % 10 == 0:
                print(f"  {deleted_count} registros deletados...")

        connection.commit()
        
        end_time = time.time()
        elapsed = end_time - start_time
        
        print(f"✓ Delete MySQL concluído em {elapsed:.2f}s")
        print(f"  Total deletado: {deleted_count} registros")
        print(f"  Taxa: {deleted_count/elapsed:.0f} registros/s")
        
    except Error as err:
        print(f"✗ Erro ao deletar do MySQL: {err}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    delete_mysql()