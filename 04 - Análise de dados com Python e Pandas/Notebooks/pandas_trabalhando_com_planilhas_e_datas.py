# Importa a biblioteca Pandas
import pandas as pd

# Lê arquivos de excel de diferentes cidades
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

# Exibe as 5 primeiras linhas do DataFrame
df5.head()

# Concatena os DataFrames em um único DataFrame
df = pd.concat([df1,df2,df3,df4,df5])

# Exibe as 5 primeiras linhas do DataFrame concatenado
df.head()

# Exibe as 5 últimas linhas do DataFrame
df.tail()

# Exibe uma amostra aleatória de 5 linhas do DataFrame
df.sample(5)

# Exibe os tipos de dados de cada coluna
df.dtypes

# Converte a coluna "LojaID" para o tipo objeto
df["LojaID"] = df["LojaID"].astype("object")

# Exibe os tipos de dados de cada coluna
df.dtypes

# Exibe as 5 primeiras linhas do DataFrame
df.head()

""" TRATANDO VALORES FALTANTES """

# Exibe a quantidade de valores nulos em cada coluna
df.isnull().sum()

# Preenche os valores nulos da coluna "Vendas" com a média da coluna "Vendas"
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

# Exibe a média da coluna "Vendas"
df["Vendas"].mean()

# Exibe a quantidade de valores nulos em cada coluna
df.isnull().sum()

# Exibe uma amostra aleatória de 15 linhas do DataFrame
df.sample(15)

# Preenche os valores nulos da coluna "Vendas" com 0
df["Vendas"].fillna(0, inplace=True)

# Remove as linhas que possuem valores nulos
df.dropna(inplace=True)

# Remove as linhas que possuem valores nulos na coluna "Vendas"
df.dropna(subset=["Vendas"], inplace=True)

# Remove as linhas que possuem todos os valores nulos
df.dropna(how="all", inplace=True)


""" CRIANDO NOVAS COLUNAS """ 

# Cria uma nova coluna "Receita" que é o produto da coluna "Vendas" pela coluna "Qtde"
df["Receita"] = df["Vendas"].mul(df["Qtde"])

# Exibe as 5 primeiras linhas do DataFrame
df.head()

# Cria uma nova coluna "Receita/Vendas" que é a razão entre a coluna "Receita" e a coluna "Vendas"
df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

# Exibe as 5 primeiras linhas do DataFrame
df.head()

# Exibe o valor máximo da coluna "Receita"
df["Receita"].max()

# Exibe o valor mínimo da coluna "Receita"
df["Receita"].min()

# Exibe as 3 maiores receitas
df.nlargest(3, "Receita")

# Exibe as 3 menores receitas
df.nsmallest(3, "Receita")

# Exibe as 3 menores receitas
df.nsmallest(3, "Receita")

# Agrupa as receitas por cidade e soma
df.groupby("Cidade")["Receita"].sum()

# Ordena os valores da receita em ordem decrescente e exibe as 10 maiores receitas
df.sort_values("Receita", ascending=False).head(10)

""" TRABALHANDO COM DATAS """

# Converte a coluna de data para o tipo int64
df["Data"] = df["Data"].astype("int64")

# Exibe os tipos de dados do dataframe
df.dtypes

# Converte a coluna de data para o tipo datetime
df["Data"] = pd.to_datetime(df["Data"])

# Exibe os tipos de dados do dataframe após a conversão
df.dtypes

# Agrupa as receitas por ano e soma
df.groupby(df["Data"].dt.year)["Receita"].sum()

# Cria uma nova coluna com o ano da venda
df["Ano_Venda"] = df["Data"].dt.year

# Exibe 5 amostras aleatórias do dataframe
df.sample(5)

# Cria duas novas colunas com o mês e dia da venda
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

# Exibe 5 amostras aleatórias do dataframe
df.sample(5)

# Exibe a data mínima presente no dataframe
df["Data"].min()

# Cria uma nova coluna com a diferença em dias entre a data da venda e a data mínima do dataframe
df["diferenca_dias"] = df["Data"] - df["Data"].min()

# Exibe 5 amostras aleatórias do dataframe
df.sample(5)

# Cria uma nova coluna com o trimestre da venda
df["trimestre_venda"] = df["Data"].dt.quarter

# Exibe 5 amostras aleatórias do dataframe
df.sample(5)

# Seleciona todas as vendas realizadas em março de 2019
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

# Exibe 20 amostras aleatórias do dataframe
vendas_marco_19.sample(20)