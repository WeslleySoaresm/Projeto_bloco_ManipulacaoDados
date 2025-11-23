import pandas as pd 
import json


#1. ler a arquivo JSON   com pandas
with open("vendas_quadrinhos.json", "r") as file:
     vendas_data = json.load(file)
 
df = pd.DataFrame(vendas_data)


#2. Criar uma coluna com o valor total de cada venda
df["valor_total"] = df["quantidade"]* df["valor_unitario"] #aqui criamos uma coluna valor_total e fizemos a multiplicação
print(df)

#3. Agruoar por quadrinho, além de somar as quantidades que foi vendidas.

agrupado = df.groupby("titulo")["quantidade"].sum().reset_index()#
print(agrupado)

#4. encontrar o quadrinho mais vendido em termo de quantidade
quadrinho_mais_vendido = agrupado.sort_values(by="quantidade", ascending=False).iloc[0]
print(quadrinho_mais_vendido)


#5. salvar o rsultado final em novo arquivo json chamado  resumo_vendas.json, que deve conter p titulo do quadrinho e total vendido.
resultado = {
     "quadrinho_mais_vendido": quadrinho_mais_vendido["titulo"],
     "quantidade_vendida": int(quadrinho_mais_vendido["quantidade"])
}
with open("resumo_vendas.json", "w") as arquivo_saida:
    json.dump(resultado, arquivo_saida, ensure_ascii=False, indent=4)
    print("ARQUIVO SALVO")