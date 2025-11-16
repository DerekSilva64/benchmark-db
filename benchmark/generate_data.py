import random
import uuid
from datetime import datetime
import json

def gerar_evento():
    return {
        "usuario_id": random.randint(1, 1000),
        "acao": random.choice(["login", "logout", "compra", "erro", "view"]),
        "categoria": random.choice(["sistema", "usuario", "transacao", "rede"]),
        "subcategoria": random.choice(["A", "B", "C", "D"]),

        "ts": datetime.utcnow(),
        "payload": json.dumps({"random": random.random()}),

        "ip": f"192.168.{random.randint(0,255)}.{random.randint(0,255)}",
        "device": random.choice(["Android", "iOS", "Windows", "Linux"]),
        "sistema_operacional": random.choice(["Windows", "Linux", "MacOS", "Android", "iOS"]),
        "navegador": random.choice(["Chrome", "Firefox", "Edge", "Safari"]),

        "latitude": random.uniform(-30, 30),
        "longitude": random.uniform(-60, 60),

        "valor1": random.randint(0, 10000),
        "valor2": random.randint(0, 10000),
        "valor3": random.randint(0, 10000),
        "valor4": random.randint(0, 10000),
        "valor5": random.randint(0, 10000),

        "score1": random.random(),
        "score2": random.random(),
        "score3": random.random(),

        "flag_ativo": random.choice([True, False]),
        "observacoes": "Lorem ipsum " + str(uuid.uuid4())[:8]
    }

def gerar_lote(n):
    return [gerar_evento() for _ in range(n)]
