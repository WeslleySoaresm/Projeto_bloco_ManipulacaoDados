import pandas as pd 
import json
from sqlalchemy import create_engine, text



#configuração do Banco de Dados PostgresSQl
db_config = {
    'user': 'postgres',
    'password': '101520',
    'host': 'localhost',
    'database': 'CursoAulaPB',
    'port': 5432
}

# Criand uma Variavel de conexão com DB
conx_str = (
    f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}"
    f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
)

#Conectando com DB 
engine = create_engine(conx_str)
print("conexão bem sucedida.")


#Lendo arquivo em json 
df = pd.read_json("alunos_deletar.json")

#Criando uma lista e cpfs
cpfs = df["xid_cpf"].astype(str).tolist()

def deletar_alunos(engine):
    #deletar primeiro de Curso_aluno tabela intermediaria entre aluno e curso, depois em aluno.

    sql_delete_curso_aluno = text("""
                              delete from academic.curso_aluno 
                              where xid_cpf = any(:cpfs);
                              """)

    sql_delete_aluno = text("""
                              DELETE FROM academic.aluno 
                              WHERE CPF = ANY(:cpfs);
                              """)




    with engine.begin() as conn:
    #1. remover curso_aluno
        conn.execute(sql_delete_curso_aluno, {"cpfs": cpfs})
    #2. remover de aluno
        conn.execute(sql_delete_aluno, {"cpfs": cpfs})

    print("Alunos deletados da tabela curso_aluno e tabela aluno com sucesso.")
    
class CursoNaoEncontradoError(Exception):
    """Exceção para curso inexistente"""
    pass    


def verificar_alunos_em_curso(engine, id_do_curso: int):
    sql = text("""
                SELECT 
            c.id_curso,
            c.nome as curso_nome,
            a.CPF,
            a.nome as aluno_nome
        FROM academic.curso_aluno ca
        JOIN academic.curso c 
            ON ca.xid_curso = c.id_curso
        JOIN academic.aluno a 
            ON ca.xid_cpf = a.CPF
        where id_curso = :id_curso
        ORDER BY c.nome, a.nome;
    """)

    with engine.connect() as conn:
        result = conn.execute(sql, {"id_curso": id_do_curso})
        rows = result.fetchall()

    # Verificação: se não encontrou nada, lança exceção
    if not rows:
        raise CursoNaoEncontradoError(f"O curso com ID {id_do_curso} não existe ou não possui alunos.")
    return rows

