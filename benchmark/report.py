import subprocess

def run(cmd):
    return float(subprocess.check_output(cmd, shell=True).decode().split()[-2])

mysql_insert = run("python insert_mysql.py")
cass_insert = run("python insert_cassandra.py")

mysql_read = run("python read_mysql.py")
cass_read = run("python read_cassandra.py")

print("\n===== RESULTADOS =====")
print(f"Inserção MySQL:     {mysql_insert:.2f}s")
print(f"Inserção Cassandra: {cass_insert:.2f}s")
print(f"Leitura MySQL:      {mysql_read:.2f}s")
print(f"Leitura Cassandra:  {cass_read:.2f}s")
