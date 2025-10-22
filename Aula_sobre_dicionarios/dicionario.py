pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Terry',
    'Palin': 'Michael'
}

#Criar e/ou atualizar valores a partir de uma chave
pythons['Gilliam'] = 'Gerry' #insert
print(pythons)

pythons['Gilliam'] = 'Terry' #update
print(pythons)

#Converter  sequências em dicionários
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
dicionario = dict(lol)
print(dicionario )


lot = [['g', 'h'], ['i', 'j'], ['k', 'l']]
dicionario_2 =dict(lot)
print(lot)


# Combinar os dicionários
print("-"*120)
dicionario.update(dicionario_2) #fazendo o update do dicionario _2 no dicionario fex um join tbm
print(dicionario)

#%%
sinal_transito = {
    'verde': 'avance',
    'amarelo': 'acelere',
    'vermelho': 'pare'
    
}


#Deletar item o dicionário
del pythons['Palin']
print(pythons)

#Verifiar se uma chave existe em um dict 
print('Chapman' in pythons)

#Acessar valores do dict usando a chave
print(pythons['Cleese'])

# Acessa a chave fazendo o get, caso não esteja no dict retorna um valor default nesse caso (não está do dict)
print(pythons.get('Chapman', 'Não está do dict '))

#Obter todas as chaves do dict 
print(list(sinal_transito.keys()))


#Obter todas os vlores do dict 
print(list(sinal_transito.values()))

#Obter todas os pares chave-valor do dict 
print(list(sinal_transito.items()))


# Copiar um dicionário sem que as alterações no novo dicionário afetem o antigo 

sinal_transito_copia = sinal_transito.copy()

sinal_transito['azul'] = 'confundir todo mundo'

print(sinal_transito)
print(sinal_transito_copia)

#%%

muscicas_classificações = {
    "Canção da amor": 5,
    "Dança da lua": 3,
    "Ritmo da noite": 5,
    "Melodia do sol": 4,
    "Harmonia das estrelas": 5
}

def imprimir_musicas_com_classificacao(classificacao_deejada):
    for musica, classificacao in muscicas_classificações.items():
        if classificacao == classificacao_deejada:
            print(musica)

#Chamada dessa função
imprimir_musicas_com_classificacao(3)
# %%


def invert(dicionario_original):
    dicionario_invertido = {}
    for chave, valor in dicionario_original.items():
        if (valor not in dicionario_invertido):
            dicionario_invertido[valor] = []
        dicionario_invertido[valor].append(chave)
    return dicionario_invertido




#resultado =invert({1:2, 3:4, 5:6})
#resultado_1 =invert({1:2, 2:1, 3:3})
resultado_2 =invert({1:1, 3:1, 5:1})
#print(resultado)
#print(resultado_1)
print(resultado_2)
# %%

def stock(codigo_quantidade):
    """ Codigo do Produto : Quantidade do Produto
    Verificando o estoque com codigo produto e quantidade e retorna o estoque."""
    stock_novo = {}
    for codigo, quantidade in codigo_quantidade.items():
        if (codigo not in stock_novo):
            stock_novo[codigo] = []
        stock_novo[codigo].append(quantidade)
        print("Produto já está no stock")
        return codigo_quantidade
    

stock_1 = stock({1:3, 4:3, 33:45, 1:6})
print(stock_1)
# %%

"""9) Escreva um programa que leia do teclado o código de uma peça e a quantidade
disponível em estoque. Esses dois dados de entrada são números inteiros. Acrescente
o par código:quantidade em um dicionário apenas se o código não estiver presente.
Caso esteja, dê uma mensagem informando essa situação e descarte os dados. O
laço termina quando for fornecido 0 para o código. Exiba na tela os dados do
dicionário, um membro por linha."""
estoque = {}

while True:
    codigo = int(input("Digite o código da peça (0 para sair): "))
    if codigo == 0:
        break
    elif codigo in estoque:
        print("CODIIGO JÁ EXESTENTE NO ESTOQUE. DADOS DESCARTADOS")
        continue
    quantidade = int(input("Digite a quantidade disponível em estoque"))
    estoque[codigo] = quantidade
    print("-"*15 + "Fim da leitura de dados" + "-"*15)
    print("\nDados do dicionário de estoque: ")
    for codigo, quantidade in estoque.items():
        print(f"Código: {codigo}, Quantiade: {quantidade}")

    
    
# %%
"""10) Escreva um programa que leia do teclado o nome de um aluno e sua nota final. O
programa deve armazenar esses dados em um dicionário, onde os nomes dos alunos
serão as chaves e as notas serão os valores. O programa deve permitir a inserção de
novos alunos até que seja fornecido o nome "fim" para terminar a entrada de dados.
Se um nome já existir no dicionário, o programa deve informar que esse aluno já foi
cadastrado e descartar a nova entrada. Após a entrada de dados, o programa deve
exibir a lista de alunos e suas respectivas notas, um por linha."""

alunos_notas ={}

while True:
    nome = str(input("Digite o nome do aluno (Digite 'fim' para sair): "))
    if (nome.lower() == 'fim'):
        break
        #nome em minusculo por conta da compração
    nome_normalizado = nome.lower()
    nota = float(input("Digite a nota final do aluno: "))
    if nome_normalizado in [n.lower() for n in alunos_notas.keys()]:
        print("Aluno já cadastrado. Dados descartados")
    else:
        alunos_notas[nome] = nota 
    

print("\n Dados dos alunos")
for nome, nota in alunos_notas.items():
    print(f"Nome: {nome}, nota: {nota:.2f}")


# %%
