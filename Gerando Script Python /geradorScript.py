import random
import json
from datetime import datetime, timedelta

# Função para gerar CPF aleatório de 11 dígitos
def gerar_cpf():
    return "".join([str(random.randint(0, 9)) for _ in range(11)])

# Função para gerar data aleatória entre 2023 e 2025
def gerar_data():
    start = datetime(2023, 1, 1)
    end = datetime(2025, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")

# Gerar 300 registros
dados = []
for i in range(1000):
    registro = {
        "xid_curso": random.randint(1, 5),   # cursos de 1 a 5
        "xid_cpf": gerar_cpf(),
        "datamatricula": gerar_data()
    }
    dados.append(registro)

# Salvar em JSON
with open("curso_aluno.json", "w") as f:
    json.dump(dados, f, indent=2)

print("Arquivo curso_aluno_extra.json gerado com 300 registros.")