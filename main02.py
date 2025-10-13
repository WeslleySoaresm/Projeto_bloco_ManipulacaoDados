import pandas as pd
from sqlalchemy import create_engine

# Configuração do banco de dados
db_config = {
    'user': 'root',
    'password': 'wes101520',
    'host': 'localhost',
    'database': 'empresa-b',
    'port': 3306
}

# Criando a engine de conexão com o banco de dados MySQL
engine = create_engine(
    f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
)

# Carregando os dados do Excel para DataFrame
df = pd.read_excel("dados_para_manipulacao.xlsx", sheet_name="Eleitores")

# Renomeando colunas para compatibilidade com o banco de dados
df = df.rename(columns={
    'ID Eleitor': 'id_eleitor',
    'Nome': 'nome',
    'Profissao': 'profissao',
    'Área': 'area',
    'Ganhos': 'ganhos',
    'Data da Início': 'data_inicio',
    'Chefe de Sessão': 'chefe_sessao'
})

# Inserindo os dados na tabela 'Eleitores'
df.to_sql('Eleitores', con=engine, if_exists='append', index=False)

print("✅ Dados inseridos com sucesso na tabela 'Eleitores'.")


# Exemplo de consulta para verificar os dados inseridos

#1. todos os eleitores
