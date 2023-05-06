# Importando a biblioteca pandas com o nome de apelido "pd"
import pandas as pd

# Lendo o arquivo CSV do Gapminder e armazenando-o em um DataFrame chamado "df", ignorando linhas com erro e utilizando ";" como separador
df = pd.read_csv(r'D:/OneDrive/Documentos/GitHub/dio-geracao-tec-unimed-bg-ciencia-de-dados/04 - Análise de dados com Python e Pandas/Gapminder.csv', sep=";")

print(df)
# Exibindo as 5 primeiras linhas do DataFrame
print(df.head())

# Renomeando as colunas do DataFrame utilizando um dicionário
df = df.rename(columns={"country":"Pais", "continent": "continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap": "PIB"})

# Exibindo as 10 primeiras linhas do DataFrame com as colunas renomeadas
print(df.head(10))

# Exibindo o número de linhas e colunas do DataFrame
print(df.shape)

# Exibindo as colunas presentes no DataFrame
print(df.columns)

# Exibindo os tipos de dados das colunas do DataFrame
print(df.dtypes)

# Exibindo as 15 últimas linhas do DataFrame
print(df.tail(15))

# Exibindo informações estatísticas do DataFrame
print(df.describe())

# Exibindo os valores únicos presentes na coluna "continente"
print(df["continente"].unique())

# Criando um novo DataFrame apenas com as linhas cujo valor da coluna "continente" é "Oceania"
Oceania = df.loc[df["continente"] == "Oceania"]
print(Oceania.head())

# Exibindo os valores únicos presentes na coluna "continente" do DataFrame Oceania
print(Oceania["continente"].unique())

# Agrupando as linhas do DataFrame por continente e exibindo o número de países em cada continente
print(df.groupby("continente")["Pais"].nunique())

# Agrupando as linhas do DataFrame por ano e exibindo a média da expectativa de vida para cada ano
print(df.groupby("Ano")["Expectativa de vida"].mean())

# Exibindo a média do PIB para todas as linhas do DataFrame
print(df["PIB"].mean())

# Exibindo a soma do PIB para todas as linhas do DataFrame
print(df["PIB"].sum())