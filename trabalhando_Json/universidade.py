# Json -> Pandas -> Banco de dados
#1) Exercício:
#Crie uma rotina que leia o arquivo aunos.json, carregue.os em uma estrutura de dados do pandas e inseira.os na tabela Alunos do banco de dados.
#Os alunos que já existerem na tabela deverão, então, ser atulizados.

import json 
import pandas as pd
from sqlalchemy import create_engine, null, text
from inserir_alunos_faltantes import inserir_alunos_faltantes
from delete_aluno import deletar_alunos, verificar_alunos_em_curso

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
df = df.rename(columns={"cpf": "xid_cpf"})


#inserir no banco
#df.to_sql("aluno", con=engine, if_exists='append', index=False, chunksize=1000)
#print(f"Inserido os dados na tabela.")

# Inserir/atualizar linha a linha
with engine.begin() as conn:
    for _, row in df.iterrows():
        conn.execute(
            text("""
                INSERT INTO academic.aluno (cpf, nome, datanascimento)
                VALUES (:xid_cpf, :nome, :datanascimento)
                ON CONFLICT (cpf) DO UPDATE
                SET nome = EXCLUDED.nome,
                    datanascimento = EXCLUDED.datanascimento;
            """),
            {"xid_cpf": row["xid_cpf"], "nome": row["nome"], "datanascimento": row["datanascimento"]}
        )
print(f"DADOS INSERIDO COM SUCESSO E ATUALIZADO.")


# CPFs do JSON
df_matriculas = pd.read_json("curso_aluno.json")
df_matriculas.columns = ["xid_curso", "xid_cpf", "datamatricula"]
cpfs_json = set(df_matriculas["xid_cpf"].astype(int))

# CPFs existentes no banco
sql = text("SELECT cpf FROM academic.aluno")
with engine.connect() as conn:
    cpfs_bd = set(pd.read_sql(sql, conn)["cpf"].astype(int))

# CPFs faltantes
cpfs_faltantes = cpfs_json - cpfs_bd

print("TOTAL DE CPFs QUE EXISTEM NO JSON E NÃO EXISTEM NA TABELA aluno:")
print(len(cpfs_faltantes))
print("LISTA DOS CPFs FALTANTES:")
print(cpfs_faltantes)


inserir_alunos_faltantes(engine, cpfs_faltantes)
deletar_alunos(engine)
# Exemplo de chamada
id_do_curso = int(input("Digite o Curso pelo ID: 1,2,3 "))
alunos = verificar_alunos_em_curso(engine, id_do_curso)
for aluno in alunos:
    print(f"Curso: {aluno.curso_nome}, CPF: {aluno.cpf}, Aluno: {aluno.aluno_nome}")
    
    