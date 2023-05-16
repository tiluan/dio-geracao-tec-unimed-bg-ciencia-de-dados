# Importando a biblioteca
import pandas as pd

# Leitura dos arquivos
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

# Exibindo as 5 primeiras linhas do dataframe df5
print(df5.head())

# Juntando todos os arquivos
df = pd.concat([df1, df2, df3, df4, df5])

# Exibindo as 5 primeiras linhas do dataframe df
print(df.head())

# Exibindo as 5 últimas linhas do dataframe df
print(df.tail())

# Amostra aleatória de 5 linhas do dataframe df
print(df.sample(5))

# Verificando o tipo de dado de cada coluna
print(df.dtypes)

# Alterando o tipo de dado da coluna LojaID para objeto
df["LojaID"] = df["LojaID"].astype("object")

# Verificando o tipo de dado de cada coluna novamente após a alteração
print(df.dtypes)

# Exibindo as 5 primeiras linhas do dataframe df
print(df.head())

"""**Tratando valores faltantes**"""

# Consultando linhas com valores faltantes
print(df.isnull().sum())

# Substituindo os valores nulos da coluna Vendas pela média
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

# Calculando a média das vendas após substituir os valores nulos
print(df["Vendas"].mean())

# Verificando novamente as linhas com valores faltantes
print(df.isnull().sum())

# Amostra aleatória de 15 linhas do dataframe df
print(df.sample(15))

# Substituindo os valores nulos da coluna Vendas por zero
df["Vendas"].fillna(0, inplace=True)

# Apagando as linhas com valores nulos em qualquer coluna
df.dropna(inplace=True)

# Apagando as linhas com valores nulos na coluna Vendas
df.dropna(subset=["Vendas"], inplace=True)

# Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)

"""**Criando colunas novas**"""

# Criando a coluna de receita, multiplicando as colunas Vendas e Qtde
df["Receita"] = df["Vendas"].mul(df["Qtde"])

# Exibindo as 5 primeiras linhas do dataframe df
print(df.head())

# Criando a coluna Receita/Vendas, dividindo a coluna Receita pela coluna Vendas
df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

# Exibindo as 5 primeiras linhas do dataframe df
print(df.head())

# Retornando o valor máximo da coluna Receita
print(df["Receita"].max())

# Retornando o valor mínimo da coluna Receita
print(df["Receita"].min())

# Retornando as 3 maiores receitas
print(df.nlargest(3, "Receita"))

# Retornando as 3 menores receitas
print(df.nsmallest(3, "Receita"))

# Agrupamento por cidade e soma da coluna Receita
print(df.groupby("Cidade")["Receita"].sum())

# Ordenando o dataframe pela coluna Receita em ordem decrescente e exibindo as 10 primeiras linhas
print(df.sort_values("Receita", ascending=False).head(10))

"""#**Trabalhando com datas**"""

# Transformando a coluna Data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

# Verificando o tipo de dado de cada coluna
print(df.dtypes)

# Transformando a coluna Data em tipo data
df["Data"] = pd.to_datetime(df["Data"])

# Verificando o tipo de dado de cada coluna novamente após a transformação
print(df.dtypes)

# Agrupamento por ano e soma da coluna Receita
print(df.groupby(df["Data"].dt.year)["Receita"].sum())

# Criando uma nova coluna Ano_Venda com o ano extraído da coluna Data
df["Ano_Venda"] = df["Data"].dt.year

# Amostra aleatória de 5 linhas do dataframe df
print(df.sample(5))

# Extraindo o mês e o dia da coluna Data e criando colunas separadas
df["mes_venda"], df["dia_venda"] = df["Data"].dt.month, df["Data"].dt.day

# Amostra aleatória de 5 linhas do dataframe df
print(df.sample(5))

# Retornando a data mais antiga da coluna Data
print(df["Data"].min())

# Calculando a diferença de dias entre cada data da coluna Data e a data mais antiga
df["diferenca_dias"] = df["Data"] - df["Data"].min()

# Amostra aleatória de 5 linhas do dataframe df
print(df.sample(5))

# Criando a coluna trimestre a partir da coluna Data
df["trimestre_venda"] = df["Data"].dt.quarter

# Amostra aleatória de 5 linhas do dataframe df
print(df.sample(5))

# Filtrando as vendas do ano de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

# Amostra aleatória de 20 linhas do dataframe vendas_marco_19
print(vendas_marco_19.sample(20))

"""#**Visualização de dados**"""

# Contagem de ocorrências de cada valor na coluna LojaID em ordem decrescente
print(df["LojaID"].value_counts(ascending=False))

# Gráfico de barras da contagem de ocorrências de cada valor na coluna LojaID em ordem decrescente
df["LojaID"].value_counts(ascending=False).plot.bar()

# Gráfico de barras horizontais da contagem de ocorrências de cada valor na coluna LojaID
df["LojaID"].value_counts().plot.barh()

# Gráfico de barras horizontais da contagem de ocorrências de cada valor na coluna LojaID
df["LojaID"].value_counts().plot.barh();

# Gráfico de pizza da soma da coluna Receita agrupada por ano
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

# Contagem de ocorrências de cada valor na coluna Cidade
print(df["Cidade"].value_counts())

#Adicionando um título e alterando o nome dos eixos
import matplotlib.pyplot as plt
# Gráfico de barras da contagem de ocorrências de cada valor na coluna Cidade
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")

# Gráfico de barras da contagem de ocorrências de cada valor na coluna Cidade com cor vermelha
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")

# Alterando o estilo do gráfico para o estilo "ggplot"
plt.style.use("ggplot")

# Gráfico de linha da soma da coluna Qtde agrupada pelo mês de venda
df.groupby(df["mes_venda"])["Qtde"].sum().plot(title="Total Produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()

# Exibindo a soma da coluna Qtde agrupada pelo mês de venda
print(df.groupby(df["mes_venda"])["Qtde"].sum())

# Filtrando apenas as vendas do ano de 2019
df_2019 = df[df["Ano_Venda"] == 2019]

# Exibindo a soma da coluna Qtde agrupada pelo mês de venda apenas para o ano de 2019
print(df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum())

# Gráfico de linha da soma da coluna Qtde agrupada pelo mês de venda para o ano de 2019
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker="o")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()

# Histograma da coluna Qtde
plt.hist(df["Qtde"], color="orangered")

# Gráfico de dispersão da coluna dia_venda em relação à coluna Receita
plt.scatter(x=df_2019["dia_venda"], y=df_2019["Receita"])

# Salvando o gráfico de linha da soma da coluna Qtde agrupada pelo mês de venda para o ano de 2019 em formato PNG
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker="v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()
plt.savefig("grafico QTDE x MES.png")