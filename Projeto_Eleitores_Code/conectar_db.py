# --- 2. Conexão com o Banco de Dados ---
def conectar_bd():
    try:
        cnx = _mysql_connector.connect(**db_config) # Conexão com o banco de dados
        cursor = cnx.cursor()
        return cursor, cnx
    except _mysql_connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        exit()