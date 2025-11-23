import pandas as pd 
import json


#1. ler o arquivo json usando Pandas
with open("vendas_livros.json", "r", encoding='utf-8') as arq:
    arquivo_vendas_livros = json.load(arq)

df = pd.DataFrame(arquivo_vendas_livros)


#2. Criar uma coluna que indique o valor total de cada venda (quantidae x preço unitário).

df["total_de_vendas"] = df["quantidade"] * df["preco_unitario"]
print(df)

#3. Agrupar as vendas por livros, calculando o total de unidades vendidas de cada um.

agrupado = df.groupby("titulo")["quantidade"].sum().reset_index()
print(agrupado)

#4. Encontre o livro mais vendido em termos de quantidade.
livros_mais_vendidos = agrupado.sort_values(by="quantidade", ascending=False).iloc[0]
print(livros_mais_vendidos)

#5. salvar resultado finais em um aruivo json chamado livro_mais_vendidos.josn, contendo o titulo do livro e a quantidade total vendida.

result = {
    "livros_mais_vendidos": livros_mais_vendidos["titulo"],
    "quantdade_vendida": int(livros_mais_vendidos["quantidade"])
}

with open("livro_mais_vendido.json","w") as arquivo_saida:
    json.dump(result, arquivo_saida, ensure_ascii=False, indent=4)
    print("Arquivo salvo com sucesso.")

