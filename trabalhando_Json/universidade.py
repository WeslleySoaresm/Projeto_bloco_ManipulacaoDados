import pandas as pd 
import json 
from sqlalchemy import create_engine, text

# Configuração do banco de dados
db_config = {
    'user': 'postgres',
    'password': '101520',
    'host': 'localhost',
    'database': 'CursoAulaPB',
    'port': 5432
}

conx_str = (
    f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}"
    f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
)

engine = create_engine(conx_str)
print("conexão bem sucedida.")

#ler o arquivo alunos.json
df = pd.read_json("alunos.json")

#inserir no banco
#df.to_sql("aluno", con=engine, if_exists='append', index=False, chunksize=1000)
#print(f"Inserido os dados na tabela.")

# Inserir/atualizar linha a linha
with engine.begin() as conn:
    for _, row in df.iterrows():
        conn.execute(
            text("""
                INSERT INTO academic.aluno (cpf, nome, dataNascimento)
                VALUES (:cpf, :nome, :dataNascimento)
                ON CONFLICT (cpf) DO UPDATE
                SET nome = EXCLUDED.nome,
                    dataNascimento = EXCLUDED.dataNascimento;
            """),
            {"cpf": row["CPF"], "nome": row["nome"], "dataNascimento": row["dataNascimento"]}
        )
print(f"DADOS INSERIDO COM SUCESSO E ATUALIZADO.")