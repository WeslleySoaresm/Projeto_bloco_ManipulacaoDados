<div align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original-wordmark.svg" alt="Logótipo do Python" width="200"/>
</div>

# 📊 Projeto de Análise de Eleitores com Pandas e MySQL

![Status](https://img.shields.io/badge/status-Completo-green.svg)
![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)



*Análise de dados com Python, Pandas e MySQL*

Este projeto tem como objetivo importar, armazenar e consultar dados de eleitores a partir de uma planilha Excel utilizando Python, Pandas e MySQL. Ele demonstra como integrar diferentes tecnologias para realizar análises estruturadas e consultas SQL diretamente em DataFrames.

---

## 🧰 Tecnologias Utilizadas

- Python 3.x  
- Pandas  
- SQLAlchemy  
- PyMySQL  
- MySQL Connector  
- Tabulate  
- MySQL Server  
- Microsoft Excel  

---

## 📁 Estrutura dos Dados

A planilha `dados_para_manipulacao.xlsx` contém os seguintes campos na aba `Eleitores`:

| Coluna             | Descrição                          |
|--------------------|-------------------------------------|
| ID Eleitor         | Identificador único do eleitor      |
| Nome               | Nome completo do eleitor            |
| Profissão          | Profissão atual                     |
| Área               | Área de atuação (ex: TI, Saúde)     |
| Ganhos             | Renda mensal                        |
| Data da Início     | Data de início na função            |
| Chefe de Sessão    | Booleano indicando se é chefe       |

---



# 📈 Fluxo de Execução do Projeto de ETL e Análise de Dados

Este documento descreve o fluxo de trabalho do projeto, que engloba a extração de dados de um arquivo Excel, o carregamento em um banco de dados MySQL e a posterior análise utilizando Pandas.

## 📊 Diagrama de Fluxo do Programa (Mermaid)

```mermaid
graph TD
    %% Define os nós principais do fluxo (Esquerda)
    A[Leitura dos dados do Excel] --> B;
    B[Pré-processamento e renomeação de colunas] --> C;
    C[Conexão com o banco de dados MySQL] --> D;
    D[Inserção dos dados na tabela 'Eleitores'] --> E;
    E[Consultas SQL usando Pandas]
    
    %% Define o nó de saída e o conecta ao final da análise
    E --> F;
    F[Exibição dos resultados com tabulate];
    
    %% Estilização (Opcional, para visual mais limpo)
    style A fill:#D4EDF7,stroke:#31708F,stroke-width:2px
    style B fill:#F5F5DC,stroke:#B8860B,stroke-width:2px
    style C fill:#DDEBF7,stroke:#2F4F4F,stroke-width:2px
    style D fill:#DDEBF7,stroke:#2F4F4F,stroke-width:2px
    style E fill:#E6F7E6,stroke:#3C763D,stroke-width:2px
    style F fill:#FEECEB,stroke:#A94442,stroke-width:2px


---

## 🛠️ Etapas do Projeto

### 1. 📥 Leitura dos Dados

```python
df = pd.read_excel("dados_para_manipulacao.xlsx", sheet_name="Eleitores")
```

### 2. 🧹 Pré-processamento

```python
df = df.rename(columns={
    'ID Eleitor': 'id_eleitor',
    'Nome': 'nome',
    'Profissao': 'profissao',
    'Área': 'area',
    'Ganhos': 'ganhos',
    'Data da Início': 'data_inicio',
    'Chefe de Sessão': 'chefe_sessao'
})
```

### 3. 🗄️ Inserção no Banco de Dados

```python
engine = create_engine("mysql+pymysql://root:wes101520@localhost:3306/empresa-b")
df.to_sql('Eleitores', con=engine, if_exists='append', index=False)
```

---

## 🔍 Consultas Realizadas

1. **Todos os eleitores:**
   ```sql
   SELECT * FROM Eleitores
   ```

2. **Eleitores que trabalham com TI:**
   ```sql
   SELECT * FROM Eleitores WHERE area = 'TI'
   ```

3. **Eleitores com ganhos superiores a R$ 5.000:**
   ```sql
   SELECT * FROM Eleitores WHERE ganhos > 5000
   ```

4. **Nome e data de início após 01/01/2023:**
   ```sql
   SELECT nome, data_inicio FROM Eleitores WHERE data_inicio > '2023-01-01'
   ```

5. **Total de eleitores por área e média de ganhos:**
   ```sql
   SELECT area, COUNT(*) AS total_eleitores, AVG(ganhos) AS media_ganhos FROM Eleitores GROUP BY area
   ```

6. **Acréscimo de 10% nos ganhos dos eleitores da área de TI com IDs 100 e 200:**

```python
from sqlalchemy.sql import text

df = pd.read_sql("SELECT * FROM `empresa-b`.Eleitores WHERE id_eleitor IN (100, 200)", con=engine)
df["ganhos"] *= 1.10

with engine.connect() as connection:
    for index, row in df.iterrows():
        update_query = text("""
            UPDATE Eleitores SET ganhos = :ganhos WHERE id_eleitor = :id_eleitor
        """)
        connection.execute(update_query, {"ganhos": row["ganhos"], "id_eleitor": row["id_eleitor"]})
        print(f"Atualizado ganhos do eleitor ID {row['id_eleitor']} para {row['ganhos']:.2f}")
    connection.commit()

print("Ganhos atualizados com sucesso para eleitores 100 e 200, via dataframe.")
```

---

## 🧪 Execução Local

1. Certifique-se de que o MySQL está rodando e a base `empresa-b` foi criada.  
2. Instale as dependências:
   ```bash
   pip install pandas sqlalchemy pymysql tabulate openpyxl mysql-connector-python
   ```
3. Execute o script Python principal.

---

## ✅ Resultados Esperados

- Dados inseridos com sucesso no banco de dados.  
- Consultas SQL exibidas em formato de tabela no terminal.  
- Análises como média de ganhos por área e filtros por profissão e data.  
- Atualização de ganhos para eleitores específicos via DataFrame.

---

## 📌 Observações

- Certifique-se de que o arquivo Excel esteja no mesmo diretório do script.  
- As credenciais do banco de dados estão fixas no código para fins de demonstração. Em produção, utilize variáveis de ambiente.

---

