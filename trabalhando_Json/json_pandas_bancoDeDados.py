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

#criando conexão com o BD PostgresSQL
conx_str = (
    f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}"
    f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
)

engine = create_engine(conx_str)
print("conexão bem sucedida.")

#ler o arquivo curso.json. em JSON  
df = pd.read_json("cursos.json")

#Garantir a correspondecia entre as colunas do dataFrame e do BD
df.columns = ["id_curso", "nome", "descricao"]

#Comendo de UPSERT (INSRT + UPDATE)
tabela = "academic.curso"
pk ="id_curso"

colunas = list(df.columns)
cols_str = ", ".join(colunas) 
vals_str = ", ".join([f":{c}" for c in colunas])
set_str = ", ".join([f"{c}=EXCLUDED.{c}" for c in colunas if c != pk])


sql_upsert = text(f"""
           INSERT INTO {tabela} ({cols_str})
           VALUES ({vals_str}) 
           ON CONFLICT ({pk}) 
           DO UPDATE SET
                {set_str}    
"""
)


#envio massivo de dados

with engine.begin() as conn:
    conn.execute(sql_upsert, df.to_dict(orient="records"))
print("Registro inserido e/ou atulizados com sucesso.")