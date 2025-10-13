import pandas as pd
from sqlalchemy import create_engine, text
from tabulate import tabulate

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

#consultando os dados inseridos

#1. consultando todos os eleitores
query_all_eleitores = "SELECT * FROM Eleitores"
result_all_eleitores = pd.read_sql(query_all_eleitores, con=engine) 
print("-"*150)
print("Todos os Eleitores:\n")
print("-"*150)
print(tabulate(result_all_eleitores, headers='keys', tablefmt='psql'))

#2. todos eleitores que trabalha com TI
query_ti_eleitores = "SELECT * FROM Eleitores WHERE area = 'TI'"
result_ti_eleitores = pd.read_sql(query_ti_eleitores, con=engine)
print("-"*150)
print("\nEleitores que trabalham com TI:\n")
print("-"*150)
print(tabulate(result_ti_eleitores, headers='keys', tablefmt='psql'))

#3. todos eleitores que ganham mais de 5000
query_high_earners = "SELECT * FROM Eleitores WHERE ganhos > 5000"
result_high_earners = pd.read_sql(query_high_earners, con=engine)
print("-"*150)
print("\nEleitores que ganham mais de 5000:\n")
print("-"*150)
print(tabulate(result_high_earners, headers='keys', tablefmt='psql') )

#4. nome e data de início dos eleitores após 01/01/2023
query_name_start_date = "SELECT nome, data_inicio FROM Eleitores WHERE data_inicio > '2023-01-01'"
result_name_start_date = pd.read_sql(query_name_start_date, con=engine)
print("-"*150)
print("\nNome e Data de Início dos Eleitores:\n")
print("-"*150)
print(tabulate(result_name_start_date, headers='keys', tablefmt='psql'))

#5 . total de eleitores por área e  media de ganhos
query_total_by_area = "SELECT area, COUNT(*) AS total_eleitores, AVG(ganhos) AS media_ganhos FROM Eleitores GROUP BY area"
result_total_by_area = pd.read_sql(query_total_by_area, con=engine)
print("-"*150)
print("\nTotal de Eleitores por Área:\n")
print("-"*150)
print(tabulate(result_total_by_area, headers='keys', tablefmt='psql'))


#6. acresentando 10% no ganho de eleitores da área de TI
df = pd.read_sql(" SELECT * FROM `empresa-b`.Eleitores WHERE id_eleitor IN (100, 200)", con=engine)
df["ganhos"] *= 1.10

#atualizar (update) os dados no banco do novos ganhos
with engine.connect() as connection:
    for index, row in df.iterrows():
        update_query = text("""
                            UPDATE Eleitores SET ganhos = :ganhos WHERE id_eleitor = :id_eleitor
                           """)

        connection.execute(update_query, {"ganhos": row["ganhos"], "id_eleitor": row["id_eleitor"]})
        print(f"Atualizado ganhos do eleitor ID {row['id_eleitor']} para {row['ganhos']:.2f}")
    connection.commit()

print("Ganhos atualizados com sucesso para eleitores 100 e 200, via dataframe.")