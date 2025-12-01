import mysql.connector as _mysql_connector
from tabulate import tabulate
import pandas as pd
from datetime import datetime
from inserir_dados import *

configuracao_bd()
df = ler_dados_excel()
cursor, cnx = conectar_bd()

#1) selecionar todos os registros da tabela eleitores
query = "SELECT * FROM eleitor"
df = pd.read_sql_query(query, cnx)
print(tabulate(df, headers='keys', tablefmt='psql'))

print("DataFrame gravado com sucesso na tabela mysql")