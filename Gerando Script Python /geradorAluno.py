import random
import json
from datetime import datetime, timedelta

# Função para gerar CPF aleatório de 11 dígitos
def gerar_cpf():
    return "".join([str(random.randint(0, 9)) for _ in range(11)])

# Função para gerar nome fictício
def gerar_nome():
    primeiros = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Joana", "Lucas", "Mariana", "Nicolas", "Olivia", "Paulo", "Renata", "Sofia", "Thiago", "Valentina", "William"]
    sobrenomes = ["Silva", "Souza", "Costa", "Oliveira", "Pereira", "Rodrigues", "Almeida", "Nascimento", "Santos", "Ferreira", "Martins", "Lima", "Barbosa", "Carvalho", "Mendes", "Gomes", "Teixeira", "Ribeiro", "Correia", "Araújo"]
    return f"{random.choice(primeiros)} {random.choice(sobrenomes)}"

# Função para gerar data de nascimento aleatória (entre 1980 e 2010)
def gerar_data_nascimento():
    start = datetime(1980, 1, 1)
    end = datetime(2010, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")

# Função para gerar lista de alunos
def gerar_alunos(qtd=50):
    alunos = []
    for _ in range(qtd):
        aluno = {
            "cpf": gerar_cpf(),
            "nome": gerar_nome(),
            "datanascimento": gerar_data_nascimento()
        }
        alunos.append(aluno)
    return alunos

# Exemplo de uso
alunos = gerar_alunos(1000)  # gera 50 alunos
with open("alunos.json", "w") as f:
    json.dump(alunos, f, indent=2)

print("Arquivo alunos.json gerado com sucesso! 300 ")