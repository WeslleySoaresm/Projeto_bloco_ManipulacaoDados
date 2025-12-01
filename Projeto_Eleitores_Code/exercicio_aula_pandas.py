import pandas as pd
from datetime import datetime

from tabulate import tabulate



#ler o arquivo excel para um dataframe
df = pd.read_excel("dados_para_manipulacao.xlsx", sheet_name="Eleitores") # Lê a planilha 'Eleitores'   
print(tabulate(df, headers='keys', tablefmt='psql'))


# 1. todos os eleitores 
print("\n1. todos os eleitores")
print(tabulate(df, headers='keys', tablefmt='psql'))
print("-" * 150)    

#2. eleitores que trabalham na área de TI
print("\n2. eleitores que trabalham na área de TI")
df_ti = df[df['Área'] == 'TI']
print(tabulate(df_ti, headers='keys', tablefmt='psql'))
print("-" * 150) 

#3. eleitores que trabalham na área de TI e ganham mais de 5000
print("\n3. eleitores que trabalham na área de TI e ganham mais de 5000")
df_ti_5000 = df[(df['Área'] == 'TI') & (df['Ganhos'] > 5000)]
print(tabulate(df_ti_5000, headers='keys', tablefmt='psql'))
print("-" * 150)


#4.nome e data de inicio dos eleitores que iniciaram antes de 2023
print("\n4. eleitores que iniciaram antes de 2023")
df["Data da Início"] = pd.to_datetime(df["Data da Início"])

df_atuais = df[df["Data da Início"] > pd.to_datetime("2023-01-01")]
print(tabulate(df_atuais[["Nome", "Data da Início"]], headers='keys', tablefmt='psql'))
print("-" * 150)


# 5 filtra media de ganhos de cada setor
print("\n5. média de ganhos de cada setor")     
df_media_ganhos = df.groupby("Área")["Ganhos"].mean().reset_index()
df_media_ganhos = df_media_ganhos.rename(columns={"Ganhos": "Média de Ganhos"})
print(tabulate(df_media_ganhos, headers='keys', tablefmt='psql'))
print("-" * 150)    



