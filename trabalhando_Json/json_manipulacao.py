import json 
import pandas as pd 

json_data = '''
[
{"name": "Joao", "age": 30, "City": "Sao Paulo"},
{"name": "Maria", "age": 25, "City": "Rio de Janeiro"}

]
'''

data = json.loads(json_data) #transforma em arquivo json 
df = pd.DataFrame(data) #transforma em dataframe
#print(df)


df.to_json("output_recorda.json", orient="records", lines=True) #cria um arquivo json e salva o json_data
df.to_json("output_split.json", orient="split")
df.to_json("output_index.json", orient="index")
print("Arquivo salvo com sucesso")

#%%
import pandas as pd

#Criar um dicionario 

data = {
    "name": "Joao",
    "age": 30,
    "address": {
        "city": "Sa Paulo",
        "zip_code": "01234-567"
    },
    "phones": [
        {"type": "fixo", "number": "1234-5678"},
        {"type": "cell_phone", "number": "9876-9876"}


    ]
}

df = pd.json_normalize(data, "phones", ["name", "age",["address", "city"], ["address", "zip_code"]])
print(df)
# %%
