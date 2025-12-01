import pandas as pd
import json 
from sqlalchemy import create_engine, text
from universidade import *

# Configuração do banco de dados
db_config = {
    'user': 'postgres',
    'password': '101520',
    'host': 'localhost',
    'database': 'CursoAulaPB',
    'port': 5432
}

# Criando conexão
conx_str = (
    f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}"
    f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
)
engine = create_engine(conx_str)
print("Conexão bem sucedida.")

# Ler JSON no dataframe
df = pd.read_json("curso_aluno.json")

#Garantir a correspondencia entre as colunas do dataFrame e do BD
df.columns = ["xid_curso", "xid_cpf", "datamatricula"]


inserir_alunos_faltantes(engine, cpfs_faltantes)

# ---------------------------------------
# 1️⃣ Buscar CPFs existentes no BD
# ---------------------------------------

sql_alunos = text("SELECT cpf FROM academic.aluno")
with engine.connect() as conn:
    cpfs_existentes = pd.read_sql(sql_alunos, conn)

cpfs_existentes = set(cpfs_existentes["cpf"].astype(int))

# Filtrar dataframe
df["xid_cpf"] = df["xid_cpf"].astype(int)
df_validos = df[df["xid_cpf"].isin(cpfs_existentes)]
df_invalidos = df[~df["xid_cpf"].isin(cpfs_existentes)]

print(f"Registros válidos: {len(df_validos)}")
print(f"Registros ignorados (CPF inexistente): {len(df_invalidos)}")

# ---------------------------------------
# 2️⃣ Upsert apenas com registros válidos
# ---------------------------------------

tabela = "academic.curso_aluno"
pk_cols = ["xid_curso", "xid_cpf"]

colunas = list(df_validos.columns)
cols_str = ", ".join(colunas)
vals_str = ", ".join([f":{c}" for c in colunas])
set_str = ", ".join([f"{c}=EXCLUDED.{c}" for c in colunas if c not in pk_cols])
pk_str = ", ".join(pk_cols)

df = pd.read_json("curso_aluno.json")
df.columns = ["xid_curso", "xid_cpf", "datamatricula"]

sql_upsert_matricula = text("""
    INSERT INTO academic.curso_aluno (xid_curso, xid_cpf, datamatricula)
    VALUES (:xid_curso, :xid_cpf, :datamatricula)
    ON CONFLICT (xid_curso, xid_cpf) DO UPDATE SET
        datamatricula = EXCLUDED.datamatricula;
""")

with engine.begin() as conn:
    conn.execute(sql_upsert_matricula, df.to_dict(orient="records"))

print("Matrículas inseridas / atualizadas com sucesso.")



