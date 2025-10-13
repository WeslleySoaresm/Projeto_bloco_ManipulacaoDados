import pandas as pd
from datetime import datetime
import mysql.connector as _mysql_connector
from tabulate import tabulate



# --- 1. Configuração do Banco de Dados ---

db_config = {
    'user': 'root',
    'password': 'wes101520',
    'host': 'localhost',
    'database': 'Empresa-A',
    'port': 3306 # Porta padrão do MySQL
}


# --- 1. Leitura do arquivo Excel ---
df = pd.read_excel("dados_para_manipulacao.xlsx", sheet_name="Eleitores") # Lê a planilha 'Eleitores'




# --- 2. Conexão com o Banco de Dados ---
try:
    cnx = _mysql_connector.connect(**db_config) # Conexão com o banco de dados
    cursor = cnx.cursor()
except _mysql_connector.Error as err:
    print(f"Erro ao conectar ao banco de dados: {err}")
    exit()

#formato_entrada_datetime_mysql = "%Y-%m-%d %H:%M:%S" # Formato da data no arquivo Excel


#CONSULTANDO DADOS EM MYSQL COM LINGUAGEM SQL USANDO PANDAS
#1) selecionar todos os registros da tabela eleitores
query = "SELECT * FROM `Eleitores`"
df = pd.read_sql_query(query, cnx)
print(tabulate(df, headers='keys', tablefmt='psql'))

print("DataFrame gravado com sucesso na tabela mysql")

#2) todos os eleitores que trabalham na área de TI
query = "SELECT * FROM `Eleitores` WHERE `Área` = 'TI'"
df = pd.read_sql_query(query, cnx)
print(tabulate(df, headers='keys', tablefmt='psql'))

print("DataFrame gravado com sucesso na tabela mysql")
print("-" * 150)

#3) todos os eleitores que ganham mais de 6500
query = "SELECT * FROM `Eleitores` WHERE `Ganhos` > 6500"
df = pd.read_sql_query(query, cnx)
print(tabulate(df, headers='keys', tablefmt='psql'))    
print("DataFrame gravado com sucesso na tabela mysql")
print("-" * 150)

#4) todos os eleitores que começaram a trabalhar após 01/01/2020
query = "SELECT * FROM `Eleitores` WHERE `data_inicio` > '20200101'"
df = pd.read_sql_query(query, cnx)
print(tabulate(df, headers='keys', tablefmt='psql'))
print("DataFrame gravado com sucesso na tabela mysql")
print("-" * 150)

#5) selecione as áreas e os respectivos ganhos médios dos eleitores
query = "SELECT `Área`, AVG(`Ganhos`) AS `Ganhos Médios` FROM `Eleitores` GROUP BY `Área`"
df = pd.read_sql_query(query, cnx)
print(tabulate(df, headers='keys', tablefmt='psql'))
print("DataFrame gravado com sucesso na tabela mysql")
print("-" * 150)

