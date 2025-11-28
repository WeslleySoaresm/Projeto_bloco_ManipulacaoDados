import pandas as pd
from sqlalchemy import text
from datetime import datetime
import random


def inserir_alunos_faltantes(engine, cpfs_faltantes):
    """
    Insere na tabela academic.aluno os CPFs que ainda não existem.
    Gera nome e data de nascimento automaticamente.
    """
  
    if not cpfs_faltantes:
        print("Não há CPFs faltantes para inserir.")
        return

    # Criar DataFrame com dados fictícios
    novos_alunos = []
    for cpf in cpfs_faltantes:
        novos_alunos.append({
            "cpf": int(cpf),
            "nome": f"Aluno {cpf}",  # Nome gerado automaticamente
            "datanascimento": datetime(
                random.randint(1980, 2010),   # ano
                random.randint(1, 12),        # mês
                random.randint(1, 28)         # dia
            ).date()
        })

    df_novos = pd.DataFrame(novos_alunos)

    # SQL UPSERT
    sql_upsert = text("""
        INSERT INTO academic.aluno (cpf, nome, datanascimento)
        VALUES (:cpf, :nome, :datanascimento)
        ON CONFLICT (cpf) DO UPDATE SET
            nome = EXCLUDED.nome,
            datanascimento = EXCLUDED.datanascimento;
    """)

    # Inserir no banco
    with engine.begin() as conn:
        conn.execute(sql_upsert, df_novos.to_dict(orient="records"))

    print(f"{len(df_novos)} novos alunos foram criados com sucesso!")
